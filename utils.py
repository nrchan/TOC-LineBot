import os
import json

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, FlexSendMessage, TextSendMessage, CarouselTemplate, CarouselColumn, MessageTemplateAction, TemplateSendMessage, ConfirmTemplate, QuickReply, QuickReplyButton, MessageAction, ImageSendMessage
from notes import chordList, scaleList

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(str(channel_access_token))

def send_text_message(reply_token, text, quickReplyType = None):
    if quickReplyType == "note":
        quick_reply = QuickReply(items=[
                QuickReplyButton(action = MessageAction(label='C', text='C')),
                QuickReplyButton(action = MessageAction(label='D', text='D')),
                QuickReplyButton(action = MessageAction(label='E', text='E')),
                QuickReplyButton(action = MessageAction(label='F', text='F')),
                QuickReplyButton(action = MessageAction(label='G', text='G')),
                QuickReplyButton(action = MessageAction(label='A', text='A')),
                QuickReplyButton(action = MessageAction(label='B', text='B')),
                QuickReplyButton(action = MessageAction(label='Db', text='Db')),
                QuickReplyButton(action = MessageAction(label='Eb', text='Eb')),
                QuickReplyButton(action = MessageAction(label='Gb', text='Gb')),
                QuickReplyButton(action = MessageAction(label='Ab', text='Ab')),
                QuickReplyButton(action = MessageAction(label='Bb', text='Bb')),
                QuickReplyButton(action = MessageAction(label='C#', text='C#')),
            ])
    elif quickReplyType == "chord":
        quick_reply = QuickReply(items=[
                QuickReplyButton(action = MessageAction(label='Maj', text='Maj')),
                QuickReplyButton(action = MessageAction(label='Maj9', text='Maj9')),
                QuickReplyButton(action = MessageAction(label='m', text='m')),
                QuickReplyButton(action = MessageAction(label='m7', text='m7')),
                QuickReplyButton(action = MessageAction(label='-Δ7', text='-Δ7')),
                QuickReplyButton(action = MessageAction(label='7', text='7')),
                QuickReplyButton(action = MessageAction(label='ø(m7b5)', text='ø')),
                QuickReplyButton(action = MessageAction(label='+', text='+')),
                QuickReplyButton(action = MessageAction(label='+7', text='+7')),
                QuickReplyButton(action = MessageAction(label='6', text='6')),
                QuickReplyButton(action = MessageAction(label='sus', text='sus')),
                QuickReplyButton(action = MessageAction(label='sus2', text='sus2')),
            ])
    elif quickReplyType == "scale":
        quick_reply = QuickReply(items=[
                QuickReplyButton(action = MessageAction(label='大調', text='大調')),
                QuickReplyButton(action = MessageAction(label='小調(自然小音階)', text='小調')),
                QuickReplyButton(action = MessageAction(label='和聲小音階', text='和聲小音階')),
                QuickReplyButton(action = MessageAction(label='旋律小音階', text='旋律小音階')),
                QuickReplyButton(action = MessageAction(label='全音音階', text='全音音階')),
                QuickReplyButton(action = MessageAction(label='五聲音階(宮調式)', text='宮調式')),
            ])
    else:
        quick_reply = None
    
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text, quick_reply = quick_reply))

    return "OK"

def send_menu_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="主選單",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="🎧 和弦名稱",
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
                    title="🎶 和弦組成音",
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
                    title="🎻 音階名稱",
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
                    title="🎹 音階組成音",
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
                    },
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
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "我要更改根音",
                        "text": "更改根音"
                        },
                        "height": "sm"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "我要更改和弦種類",
                        "text": "更改和弦種類"
                        },
                        "height": "sm"
                    },
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
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "我要更改根音",
                        "text": "更改根音"
                        },
                        "height": "sm"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "我要更改音階種類",
                        "text": "更改音階種類"
                        },
                        "height": "sm"
                    },
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

def send_fsm(reply_token):
    line_bot_api.reply_message(
        reply_token,
        ImageSendMessage(
            original_content_url="https://lh3.googleusercontent.com/pw/ACtC-3dv0dTn-45EryPyNIWrarZAj0aD35QyV0CPNu1nTkQP1tdY5q8EvpGFuJFegz9Pkr0Le8pe6p2kNcXvHwLPAlOVJ1YvnuTlAeZoSGTwb50NGKfksvFIiYalFEEfBCssWHwDFYIl5xC_3cQn_4Ls0GE=w2258-h772-no?authuser=2",
            preview_image_url="https://lh3.googleusercontent.com/pw/ACtC-3dv0dTn-45EryPyNIWrarZAj0aD35QyV0CPNu1nTkQP1tdY5q8EvpGFuJFegz9Pkr0Le8pe6p2kNcXvHwLPAlOVJ1YvnuTlAeZoSGTwb50NGKfksvFIiYalFEEfBCssWHwDFYIl5xC_3cQn_4Ls0GE=w2258-h772-no?authuser=2",
            quick_reply=QuickReply(items=[QuickReplyButton(action = MessageAction(label='回到「選單」', text='選單'))])
            )
        )
    return "OK"

def send_demo(reply_token):
    line_bot_api.reply_message(
        reply_token,
        TextSendMessage(
            text="Hello world ~",
            quick_reply=QuickReply(items=[QuickReplyButton(action = MessageAction(label='回到「選單」', text='選單'))])
            )
        )
    return "OK"