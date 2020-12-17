import os
import json

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, FlexSendMessage, TextSendMessage, CarouselTemplate, CarouselColumn, MessageTemplateAction, TemplateSendMessage, ConfirmTemplate
from notes import chordList, scaleList

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(str(channel_access_token))

def send_text_message(reply_token, text):
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text, quick_reply = None))

    return "OK"

def send_menu_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="主選單",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="和弦名稱",
                    text="輸入音符名稱，\n查詢它們能組成哪個和弦。",
                    thumbnail_image_url="https://lh3.googleusercontent.com/pw/ACtC-3fDYPTuUWEr3gCzNRi03e3Zz8D_TcM8uqPlMsML3oheMeU8YZ0NczCSgCshJGr3EDContWiVbuPHFmzunhqVupRrvjwBNpTMQ9_wLYWjFBNfuh5ppJUFhMs4Zof7c6tj-jYMHn90GcgpS2BLln9foE=w640-h424-no",
                    actions=[
                        MessageTemplateAction(
                            label="查詢",
                            text="查和弦"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="和弦組成音",
                    text="輸入和弦名稱，\n查詢它是由什麼音符組成的。",
                    thumbnail_image_url="https://lh3.googleusercontent.com/pw/ACtC-3e3KEAfiuly_yOk8-A4ruQA_ska8PNCKCyDEWWI5zEj8xA20CDthHGLBD6YYVYvfbQnp2xi5xH7iJs7Vx-Bj3AZU6gTtWsLEDDRfL1m7UdAiFKPoY_OTPN33GFGbP0v_8djnmpYbuIBCpsAeD3VgLI=w640-h427-no",
                    actions=[
                        MessageTemplateAction(
                            label="查詢",
                            text="查和弦組成音"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="音階名稱",
                    text="輸入音符名稱，\n查詢它們能組成哪個音階。",
                    thumbnail_image_url="https://lh3.googleusercontent.com/pw/ACtC-3e9Hc2L-DP-jkWjvJdR05dBIgRetl97uVp7hBbsdy2QLorC2Uqwtk8XELrdhkcgRcxI_C6dwe4q4yGqyRWKnT8A3qQajYdvLoF5yTcnwEogAoUE6EBq7JflzNOr6zFES-53A0EqKDrxDV7vitQ4rdY=w640-h426-no",
                    actions=[
                        MessageTemplateAction(
                            label="查詢",
                            text="查音階"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="音階組成音",
                    text="輸入音階名稱，\n查詢它是由什麼音符組成的。",
                    thumbnail_image_url="https://lh3.googleusercontent.com/pw/ACtC-3fNrIahKLEUxHhV_zQBqDH8XUIx_Wg0bdlCGb4dSypatImBndP9viXi_rzxc2Wa1tB8APwureSFN1huiZHUh4m-Da_TszEKtJq0HqlgiOeQrZnvWHo5agtaUGpekWftAc-qKd8RrR1hLQyP33idsh8=w640-h427-no",
                    actions=[
                        MessageTemplateAction(
                            label="查詢",
                            text="查音階組成音"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

def send_go_to_menu_button(reply_token):
    confirm_template = TemplateSendMessage(
        alt_text="前往選單",
        template=ConfirmTemplate(
            text="不知道要幹嘛嗎？不如前往「選單」查看各項功能 😉",
            actions=[
                MessageTemplateAction(
                    label="前往「選單」",
                    text="選單"
                ),
                MessageTemplateAction(
                    label="一定要嗎",
                    text="選單"
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, confirm_template)
    return "OK"

def send_chord(reply_token, root_note, whichChord):
    symbol = ""
    for i in range(2, len(chordList[whichChord])):
        symbol = str(symbol) + root_note + chordList[whichChord][i] + ("、" if i is not len(chordList[whichChord])-1 else "")
    line_bot_api.reply_message(reply_token, 
        FlexSendMessage(
            "查詢和弦結果",
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "找到的和弦...",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": str(root_note) + " " + str(chordList[whichChord][0]),
                        "weight": "bold",
                        "wrap": True,
                        "size": "xxl",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": str(root_note) + " " + str(chordList[whichChord][1]),
                        "size": "xs",
                        "wrap": True,
                        "color": "#999999"
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "和弦代號",
                            "size": "sm",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": symbol
                        }
                        ],
                        "spacing": "sm",
                        "margin": "xxl"
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "text",
                        "text": "你可以直接在此繼續查詢，或是回到「選單」。",
                        "size": "sm",
                        "wrap": True,
                        "margin": "xxl"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "回到「選單」",
                        "text": "選單"
                        },
                        "height": "sm"
                    }
                    ]
                },
                "styles": {
                    "footer": {
                    "separator": True
                    }
                }
            }
        )
    )
    return "OK"

def send_not_found(reply_token):
    line_bot_api.reply_message(reply_token, 
        FlexSendMessage(
            "找...找不到",
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "找到的和弦...",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "找...找不到",
                        "weight": "bold",
                        "size": "xxl",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": "OAO",
                        "size": "xs",
                        "wrap": True,
                        "color": "#999999"
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "增加找到的機率？！",
                            "size": "sm",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "→ 音符用大寫字母 A 到 G",
                            "wrap": True,
                        },
                        {
                            "type": "text",
                            "text": "→ 升降記號擺在音符後面（A#、Bb）",
                            "wrap": True,
                        },
                        {
                            "type": "text",
                            "text": "→ 音符由低音排到高音",
                            "wrap": True,
                        },
                        {
                            "type": "text",
                            "text": "→ 加不加入空白或頓號是沒關係的，不過還是可以適度分隔音符，特別是降記號的部分",
                            "wrap": True,
                        },
                        ],
                        "spacing": "sm",
                        "margin": "xxl"
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "text",
                        "text": "你可以直接在此繼續查詢，或是回到「選單」。",
                        "size": "sm",
                        "wrap": True,
                        "margin": "xxl"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "回到「選單」",
                        "text": "選單"
                        },
                        "height": "sm"
                    }
                    ]
                },
                "styles": {
                    "footer": {
                    "separator": True
                    }
                }
            }
        )
    )
    return "OK"

def send_chord_note(reply_token, root_note, whichChord, notes):
    line_bot_api.reply_message(reply_token,
        FlexSendMessage(
            "查詢和弦結果",
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "和弦的組成音...",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": notes,
                        "weight": "bold",
                        "size": "xxl",
                        "wrap": True,
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": str(root_note) + " " + str(chordList[whichChord][1]),
                        "size": "xs",
                        "wrap": True,
                        "color": "#999999"
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "text",
                        "text": "你可以直接在此輸入新的和弦根音，或以目前根音繼續查詢其他和弦。也可以點擊下方回到「選單」。",
                        "size": "sm",
                        "wrap": True,
                        "margin": "xxl"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "回到「選單」",
                        "text": "選單"
                        },
                        "height": "sm"
                    }
                    ]
                },
                "styles": {
                    "footer": {
                    "separator": True
                    }
                }
            }
        )
    )
    return "OK"

def send_scale(reply_token, root_note, whichScale):
    line_bot_api.reply_message(reply_token, 
        FlexSendMessage(
            "查詢音階結果",
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "找到的音階...",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": str(root_note) + " " + str(scaleList[whichScale][0]),
                        "weight": "bold",
                        "size": "xxl",
                        "wrap": True,
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": str(root_note) + " " + str(scaleList[whichScale][1]),
                        "size": "xs",
                        "wrap": True,
                        "color": "#999999"
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "text",
                        "text": "你可以直接在此繼續查詢，或是回到「選單」。",
                        "size": "sm",
                        "wrap": True,
                        "margin": "xxl"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "回到「選單」",
                        "text": "選單"
                        },
                        "height": "sm"
                    }
                    ]
                },
                "styles": {
                    "footer": {
                    "separator": True
                    }
                }
            }
        )
    )
    return "OK"

def send_scale_note(reply_token, root_note, whichScale, notes):
    line_bot_api.reply_message(reply_token,
        FlexSendMessage(
            "查詢音階結果",
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "音階的組成音...",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": notes,
                        "weight": "bold",
                        "size": "xxl",
                        "wrap": True,
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": str(root_note) + " " + str(scaleList[whichScale][1]),
                        "size": "xs",
                        "wrap": True,
                        "color": "#999999"
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "text",
                        "text": "你可以直接在此輸入新的音階根音，或以目前根音繼續查詢其他音階。也可以點擊下方回到「選單」。",
                        "size": "sm",
                        "wrap": True,
                        "margin": "xxl"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "回到「選單」",
                        "text": "選單"
                        },
                        "height": "sm"
                    }
                    ]
                },
                "styles": {
                    "footer": {
                    "separator": True
                    }
                }
            }
        )
    )
    return "OK"