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

#Channel Access Token
line_bot_api = LineBotApi('Lc784A6vOQ68FRGL+hPMY2pcLN0N7Ixg3iLIF+jq3Khz33+WrFU6H/mSf1GbZ3HXqbFikCICKgj2N2CnFFh6QthxlMrzJ0f1h2jMyHea0DXORloKKp7IchYafX4B7fK11uOsfguxawp4y5+xV+CtVwdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('3803b1d0d78a4ba602ef3585337cc7fe')

line_bot_api.push_message('U36aee765eb76dd68a7940fd75243a994', TextSendMessage(text='歡迎來到食尚共享，請輸入『開始』來尋找美食'))

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
            title='食尚共享',
            text='食尚共享',
            actions=[
                MessageAction(
                    label='美食推薦',
                    text='美食推薦'
                ),
                MessageAction(
                    label='美食分類',
                    text='美食分類'
                ),
                MessageAction(
                    label='網站',
                    text='網站'
                ),
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    elif re.match('美食推薦',message):
        buttons_template_message = TemplateSendMessage(
        alt_text='美食推薦',
        template=ButtonsTemplate(
            thumbnail_image_url='https://as.chdev.tw/web/article/5/8/4/585d040b-89f5-489b-8e32-ad1797bb748e1645430126.jpg',
            title='食尚共享',
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
            title='食尚共享',
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
        flex_message = FlexSendMessage(
            alt_text='美食推薦-台式',
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
            "size": "sm",
            "wrap": True
            },
            {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
              },
              {
                "type": "text",
                "text": "4.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
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
                "size": "sm",
                "wrap": True
            },
            {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "sm",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
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
            "size": "sm"
            },
            {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "sm",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
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
            alt_text='美食推薦-日式',
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
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
              },
              {
                "type": "text",
                "text": "4.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
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
                    "text": "寿司",
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
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "sm",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
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
                    "text": "ラーメン",
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
            "size": "sm"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "sm",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
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
                    "text": "ざるそば",
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
            alt_text='美食推薦-韓式',
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
              "size": "sm",
              "wrap": True
            },
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
              },
              {
                "type": "text",
                "text": "4.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
              ]
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
                    "text": "비빔밥",
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
                "size": "sm",
                "wrap": True
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                {
                  "type": "icon",
                  "size": "xs",
                  "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                },
                {
                  "type": "icon",
                  "size": "xs",
                  "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                },
                {
                  "type": "icon",
                  "size": "xs",
                  "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                },
                {
                  "type": "icon",
                  "size": "xs",
                  "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                },
                {
                  "type": "icon",
                  "size": "xs",
                  "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                },
                {
                  "type": "text",
                  "text": "5.0",
                  "size": "sm",
                  "color": "#8c8c8c",
                  "margin": "md",
                  "flex": 0
                }
                ]
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
                      "text": "냉면",
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
                  "size": "sm"
                },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                {
                  "type": "icon",
                  "size": "xs",
                  "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                },
                {
                  "type": "icon",
                  "size": "xs",
                  "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                },
                {
                  "type": "icon",
                  "size": "xs",
                  "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                },
                {
                  "type": "icon",
                  "size": "xs",
                  "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                },
                {
                  "type": "icon",
                  "size": "xs",
                  "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                },
                {
                  "type": "text",
                  "text": "5.0",
                  "size": "sm",
                  "color": "#8c8c8c",
                  "margin": "md",
                  "flex": 0
                }
                ]
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
                      "text": "부대찌개",
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
            alt_text='美食推薦-美式',
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
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
              },
              {
                "type": "text",
                "text": "4.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
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
                    "text": "hamburger",
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
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "sm",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
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
                    "text": "pizza",
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
            "size": "sm"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "sm",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
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
                    "text": "steak",
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
