# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:16:35 2021

@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Line Bot聊天機器人
第四章 選單功能
按鈕樣板TemplateSendMessage
"""
#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('Lc784A6vOQ68FRGL+hPMY2pcLN0N7Ixg3iLIF+jq3Khz33+WrFU6H/mSf1GbZ3HXqbFikCICKgj2N2CnFFh6QthxlMrzJ0f1h2jMyHea0DXORloKKp7IchYafX4B7fK11uOsfguxawp4y5+xV+CtVwdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('3803b1d0d78a4ba602ef3585337cc7fe')

line_bot_api.push_message('U36aee765eb76dd68a7940fd75243a994', TextSendMessage(text='歡迎來到美食探勘家，請輸入『開始』來尋找美食'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('開始',message):
        buttons_template_message = TemplateSendMessage(
        alt_text='主選單',
        template=ButtonsTemplate(
            thumbnail_image_url='https://as.chdev.tw/web/article/5/8/4/585d040b-89f5-489b-8e32-ad1797bb748e1645430126.jpg',
            title='美食探勘家',
            text='美食探勘家',
            actions=[
                MessageAction(
                    label='美食推薦',
                    text='美食推薦'
                ),
                MessageAction(
                    label='美食分類',
                    text='美食分類'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    elif re.match('美食推薦',message):
        buttons_template_message = TemplateSendMessage(
        alt_text='美食推薦',
        template=ButtonsTemplate(
            thumbnail_image_url='https://as.chdev.tw/web/article/5/8/4/585d040b-89f5-489b-8e32-ad1797bb748e1645430126.jpg',
            title='美食探勘家',
            text='美食推薦',
            actions=[
                MessageAction(
                    label='台式美食',
                    text='台式美食'
                ),
                MessageAction(
                    label='日式美食',
                    text='日式美食'
                ),
                MessageAction(
                    label='韓式美食',
                    text='韓式美食'
                ),
                MessageAction(
                    label='美式美食',
                    text='美式美食'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    elif re.match('美食分類',message):
        buttons_template_message = TemplateSendMessage(
        alt_text='美食分類',
        template=ButtonsTemplate(
            thumbnail_image_url='https://as.chdev.tw/web/article/5/8/4/585d040b-89f5-489b-8e32-ad1797bb748e1645430126.jpg',
            title='美食探勘家',
            text='美食分類',
            actions=[
                MessageAction(
                    label='台式美食',
                    text='台式美食'
                ),
                MessageAction(
                    label='日式美食',
                    text='日式美食'
                ),
                MessageAction(
                    label='韓式美食',
                    text='韓式美食'
                ),
                MessageAction(
                    label='美式美食',
                    text='美式美食'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    elif re.match('台式美食',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage('很讚'))
    elif re.match('日式美食',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage('喔伊西'))
    elif re.match('韓式美食',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage('馬西搜有'))
    elif re.match('美式美食',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage('delicious'))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('請打「開始」來評論圖片'))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
