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

line_bot_api.push_message('U36aee765eb76dd68a7940fd75243a994', TextSendMessage(text='歡迎來到美食探勘家，請輸入『開始』或是下方選單來尋找美食'))

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

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
                    label='熱門美食',
                    text='熱門美食'
                ),
                MessageAction(
                    label='美食查詢',
                    text='美食查詢'
                ),
                MessageAction(
                    label='網站',
                    text='網站'
                ),
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    elif re.match('熱門美食',message):
        buttons_template_message = TemplateSendMessage(
        alt_text='熱門美食',
        template=ButtonsTemplate(
            thumbnail_image_url='https://as.chdev.tw/web/article/5/8/4/585d040b-89f5-489b-8e32-ad1797bb748e1645430126.jpg',
            title='美食探勘家',
            text='熱門美食',
            actions=[
                MessageAction(
                    label='麵包',
                    text='麵包'
                ),
                MessageAction(
                    label='乳製品',
                    text='乳製品'
                ),
                MessageAction(
                    label='甜點',
                    text='甜點'
                ),
                MessageAction(
                    label='蛋類',
                    text='蛋類'
                ),
                 MessageAction(
                    label='炸物',
                    text='炸物'
                ),
                 MessageAction(
                    label='肉類',
                    text='肉類'
                ),
                 MessageAction(
                    label='麵類',
                    text='麵類'
                ),
                 MessageAction(
                    label='飯類',
                    text='飯類'
                ),
                 MessageAction(
                    label='海鮮',
                    text='海鮮'
                ),
                 MessageAction(
                    label='湯品',
                    text='湯品'
                ),
                 MessageAction(
                    label='蔬菜',
                    text='蔬菜'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    elif re.match('美食查詢',message):
        buttons_template_message = TemplateSendMessage(
        alt_text='美食查詢',
        template=ButtonsTemplate(
            thumbnail_image_url='https://as.chdev.tw/web/article/5/8/4/585d040b-89f5-489b-8e32-ad1797bb748e1645430126.jpg',
            title='美食探勘家',
            text='美食查詢',
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
        flex_message = FlexSendMessage(
            alt_text='熱門美食-台式',
            contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://angelala.tw/wp-content/uploads/img/20170201210716_49.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "臭豆腐",
            "weight": "bold",
            "size": "xl",
            "wrap": True
          },
          {
            "type": "text",
            "text": "臭豆腐",
            "size": "xs"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "台式美食",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://cc.tvbs.com.tw/img/program/upload/2022/10/03/20221003162350-04e23b19.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "牛肉麵",
            "weight": "bold",
            "size": "xl",
            "wrap": True
          },
          {
            "type": "text",
            "text": "牛肉麵",
            "size": "xs"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "台式美食",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://tokyo-kitchen.icook.network/uploads/recipe/cover/407415/925ffeec2b1f9747.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "鹹酥雞",
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "text",
            "text": "鹹酥雞",
            "size": "xs"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "台式美食",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    }
  ]
} 
        )
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('日式美食',message):
        flex_message = FlexSendMessage(
            alt_text='熱門美食-日式',
            contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://d10pyp7ylo9bub.cloudfront.net/2017/01/2017sushiiiiiipic-1.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "壽司",
            "weight": "bold",
            "size": "xl",
            "wrap": True
          },
          {
            "type": "text",
            "text": "寿司",
            "size": "xs"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "日式美食",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://www.upmedia.mg/upload/article/20200815095538790340._ラーメンゼロ",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "拉麵",
            "weight": "bold",
            "size": "xl",
            "wrap": True
          },
          {
            "type": "text",
            "text": "ラーメン",
            "size": "xs"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "日式美食",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://www.menu-tokyo.jp/tradition/img/soba.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "蕎麥麵",
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "text",
            "text": "ざるそば",
            "size": "xs"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "日式美食",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    }
  ]
} 
        )
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('韓式美食',message):
        flex_message = FlexSendMessage(
            alt_text='熱門美食-韓式',
            contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://storage.googleapis.com/crossing-cms-cwg-tw/article/202202/article-6204ea39d454e.jpeg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "韓式拌飯",
            "weight": "bold",
            "size": "xl",
            "wrap": True
          },
          {
            "type": "text",
            "text": "비빔밥",
            "size": "xs"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "韓式美食",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://www.hanchao.com/varimg/cate/2169_guide_big.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "冷麵",
            "weight": "bold",
            "size": "xl",
            "wrap": True
          },
          {
            "type": "text",
            "text": "냉면",
            "size": "xs"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "韓式美食",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://a.ksd-i.com/a/2017-07-28/96760-528725.png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "部隊鍋",
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "text",
            "text": "부대찌개",
            "size": "xs"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "韓式美食",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    }
  ]
} 
        )
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('美式美食',message):
        flex_message = FlexSendMessage(
            alt_text='熱門美食-美式',
            contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSrXvhgm_YNnmyxghOa6umhwTnE251wazqOg&usqp=CAU",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "漢堡",
            "weight": "bold",
            "size": "xl",
            "wrap": True
          },
          {
            "type": "text",
            "text": "hamburger",
            "size": "xs"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "美式美食",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://www.foodnext.net/dispPageBox/getFile/GetImg.aspx?FileLocation=%2FPJ-FOODNEXT%2FFiles%2F&FileName=photo-22144-i.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "披薩",
            "weight": "bold",
            "size": "xl",
            "wrap": True
          },
          {
            "type": "text",
            "text": "pizza",
            "size": "xs"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "美式美食",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://image.cache.storm.mg/styles/smg-800x533-fp/s3/media/image/2019/12/29/20191229-104307_U8366_M581233_d0be.png?itok=6XNbHkO4",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "牛排",
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "text",
            "text": "steak",
            "size": "xs"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "美式美食",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    }
  ]
} 
        )
        line_bot_api.reply_message(event.reply_token, flex_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('請輸入『開始』來尋找美食'))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
