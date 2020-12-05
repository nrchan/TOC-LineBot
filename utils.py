import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, CarouselTemplate, CarouselColumn, MessageTemplateAction


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(channel_access_token)

def send_text_message(reply_token, text):
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_menu_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="主選單",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="和弦名稱",
                    text="輸入音符名稱，查詢它們能組成哪個和弦",
                    actions=[
                        MessageTemplateAction(
                            label="查詢"",
                            text="查和弦"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="和弦組成音",
                    text="輸入和弦名稱，查詢它是由什麼音組成的",
                    actions=[
                        MessageTemplateAction(
                            label=查詢",
                            text="查和弦組成音"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"
"""
def send_image_url(id, img_url):
    pass
def send_button_message(id, text, buttons):
    pass
"""