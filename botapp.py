from __future__ import unicode_literals
import os
from flask import Flask, request, abort,render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, messages
from for_CPU import *

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
    return render_template(
            "index.html",
    )


if __name__ == "__main__":
    app.run()