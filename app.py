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

line_bot_api = LineBotApi('Lc784A6vOQ68FRGL+hPMY2pcLN0N7Ixg3iLIF+jq3Khz33+WrFU6H/mSf1GbZ3HXqbFikCICKgj2N2CnFFh6QthxlMrzJ0f1h2jMyHea0DXORloKKp7IchYafX4B7fK11uOsfguxawp4y5+xV+CtVwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3803b1d0d78a4ba602ef3585337cc7fe')

line_bot_api.push_message('U36aee765eb76dd68a7940fd75243a994', TextSendMessage(text='你可以開始了'))

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
        image_message = ImageSendMessage(
            original_content_url='https://as.chdev.tw/web/article/5/8/4/585d040b-89f5-489b-8e32-ad1797bb748e1645430126.jpg',
            preview_image_url='https://as.chdev.tw/web/article/5/8/4/585d040b-89f5-489b-8e32-ad1797bb748e1645430126.jpg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
        line_bot_api.reply_message(event.reply_token, TextSendMessage('請評論上圖'))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('請打「開始」來評論圖片'))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
