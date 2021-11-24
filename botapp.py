from __future__ import unicode_literals
import os
from flask import Flask, request, abort,render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, messages

import configparser

import random

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        # print(body, signature)
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'
    

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
    eventmessages = event.message.text
    if eventmessages.split(" ",2)[0] == "說":
        returnmessage = eventmessages.split(" ",1)[1]
    # print(eventmessages)
        if returnmessage == "CPU":
            returnmessage = """中央處理器 （英語：Central Processing Unit，縮寫：CPU）是電腦的主要裝置之一，功能主要是解釋電腦指令以及處理電腦軟體中的資料。電腦的可程式化性主要是指對中央處理器的編程。1970年代以前，中央處理器由多個獨立單元構成，後來發展出由積體電路製造的中央處理器，這些高度收縮的元件就是所謂的微處理器，其中分出的中央處理器最為複雜的電路可以做成單一微小功能強大的單元，也就是所謂的核心。
                中央處理器廣義上指一系列可以執行複雜的電腦程式的邏輯機器。這個空泛的定義很容易地將在「CPU」這個名稱被普遍使用之前的早期電腦也包括在內。無論如何，至少從1960年代早期開始(Weik 1961)，這個名稱及其縮寫已開始在電腦產業中得到廣泛應用。儘管與早期相比，「中央處理器」在物理形態、設計製造和具體任務的執行上有了極大的發展，但是其基本的操作原理一直沒有改變。
                早期的中央處理器通常是為大型及特定應用的電腦而客製化。但是，這種昂貴的為特定應用客製化CPU的方法很大程度上已經讓位於開發便宜、標準化、適用於一個或多個目的的處理器類。這個標準化趨勢始於由單個電晶體組成的大型電腦和微機年代，隨著積體電路的出現而加速。IC使得更為複雜的中央處理器可以在很小的空間中設計和製造（在微米的數量級）。中央處理器的標準化和小型化都使這一類電子零件在現代生活中的普及程度越來越高。現代處理器出現在包括從汽車、手機到兒童玩具在內的各種物品中。
            """
        elif returnmessage == "GPU":
            returnmessage = """圖形處理器（英語：Graphics Processing Unit，縮寫：GPU；又稱顯示核心、顯示卡、視覺處理器、顯示晶片或繪圖晶片）是一種專門在個人電腦、工作站、遊戲機和一些行動裝置（如平板電腦、智慧型手機等）上執行繪圖運算工作的微處理器。
            圖形處理器是NVIDIA公司（NVIDIA）在1999年8月發表NVIDIA GeForce 256（GeForce 256）繪圖處理晶片時首先提出的概念，在此之前，電腦中處理影像輸出的顯示晶片，通常很少被視為是一個獨立的運算單元。而對手冶天科技（ATi）亦提出視覺處理器（Visual Processing Unit）概念。圖形處理器使顯示卡減少對中央處理器（CPU）的依賴，並分擔部分原本是由中央處理器所擔當的工作，尤其是在進行三維繪圖運算時，功效更加明顯。圖形處理器所採用的核心技術有硬體座標轉換與光源、立體環境材質貼圖和頂點混合、紋理壓縮和凹凸對映貼圖、雙重紋理四像素256位彩現引擎等。
            圖形處理器可單獨與專用電路板以及附屬組件組成顯示卡，或單獨一片晶片直接內嵌入到主機板上，或者內建於主機板的北橋晶片中，現在也有內建於CPU上組成SoC的。個人電腦領域中，在2007年，90%以上的新型桌上型電腦和筆記型電腦擁有嵌入式繪圖晶片，但是在效能上往往低於不少獨立顯示卡。[1]但2009年以後，AMD和英特爾都各自大力發展內建於中央處理器內的高效能整合式圖形處理核心，它們的效能在2012年時已經勝於那些低階獨立顯示卡，[2]這使得不少低階的獨立顯示卡逐漸失去市場需求，兩大個人電腦圖形處理器研發巨頭中，AMD以AMD APU產品線取代旗下大部分的低階獨立顯示核心產品線。[3]而在手持裝置領域上，隨著一些如平板電腦等裝置對圖形處理能力的需求越來越高，不少廠商像是高通（Qualcomm）、PowerVR、ARM、NVIDIA等，也在這個領域「大顯身手」。
            GPU不同於傳統的CPU，如Intel i5或i7處理器，其核心數量較少，專為通用計算而設計。相反，GPU是一種特殊類型的處理器，具有數百或數千個核心，經過最佳化，可並列執行大量計算。雖然GPU在遊戲中以3D彩現而聞名，但它們對執行分析、深度學習和機器學習演算法尤其有用。GPU允許某些計算比傳統CPU上執行相同的計算速度快10倍至100倍。
            """
    elif eventmessages == "XD":
        returnmessage = "笑三小?????"
    # elif event.source.user_id != "U7b1955002bf5c36b59d9703e7983b2a1":
    #     # Phoebe 愛唱歌
    #     pretty_note = '♫♪♬'
    #     returntext = ''
        
    #     for i in event.message.text:
    #         returntext += i
    #         returntext += random.choice(pretty_note)
    
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=returnmessage)
        )
@app.route('/', methods=['GET', 'POST'])
def index():
    return "<h1>Welcome to CodingX</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])