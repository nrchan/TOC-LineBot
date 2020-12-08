import os
import json

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, FlexSendMessage, TextSendMessage, CarouselTemplate, CarouselColumn, MessageTemplateAction, TemplateSendMessage, ConfirmTemplate
from notes import chordList

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
                    text="輸入音符名稱，\n查詢它們能組成哪個和弦。",
                    thumbnail_image_url="https://lh3.googleusercontent.com/haIKfpovbWl9BiaFSrHeepSL0d24dVozHgzxr0D5CrSe14qzAYwc1ZUhEEXTO_Zd6djSLqATVHVUbynWvsrRFn02Li3Y8qb3ChzE0V311mqNFcYGFW7ks9Uui-5cQuyWjg9ptaMv4NULn8Sfc17iQ4N59hOR4CHSlvtLd17iNt8DBydfRiN9k8qdeCgzjUuKLBTlYTdmA-DUbskoyv8iBQ6-71lTPFJZOgY-NOSXVWjRfJML-aDUH_pR8beigvmDkjYhF7x0EnS1I6eb18oKfxcTJfy1B8OHPgkRMd5M7MfA0729sYWQ_mSvCaHZsSI8IVDhWJdzSAN78X_yNLzp0Gc17HrzDRcCgsYvWE1ffCVOSt5Fvlb20EkaHu922OD2qz8xLyJiBfe3Ea2VbXtQizjEtSrvdAjWyC8JiO_2Pe6Ig5SuYCP0DwWbvAcLiUabvd8euceWouy30TLuR3Zmd8azbuarcu-IJQ20Dg9hXFm7jrOv6YCzZe72J4JUTL0YS7ZCd8TMQP9iYPllqpnsrDKTAjwVi3I6rlN6wpc-7fPejHmF9UNzqvq53dVs38QLFck0Hc3vDxkqOZJOFtl6miaceEW4YWAYJ3Bo7T-YyocebLixTocq5hDY0yRjBRHlNCbB-cYeaptJf1gI7cImkCR6G1MOajcy0LMe0sinKVxIB56gKTWvtYl6oYAZ=w640-h427-no?authuser=2",
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
                    thumbnail_image_url="https://lh3.googleusercontent.com/RhoIywtAz17h9neSDvC88sHUfjw1ZY553j-6g6SP_VWjpcWJCsTWkaQxhBssCOXkSpW7mRipMVtBmugKpSsVjhgpT79xca2b_kYl6a6xIArK9QVxwkueGoe3e2J_MiQ4m9BnQ26ejepXopsYnFlyfKr-Rs8JyonbjOlEAOoZKUJWza-OYJD5bi5jOs1Nvc_cXQvarpasQ1q9C2s03WsLZKiDOHA1KIQLAqtyvILiQI2zB4BB3r7qKvLoEtJG3z4g-wRLO1mNTRsLa8qkQZl7MXCDk_RjUewWCfDXlGbpsJ3CDEICR_hyETo3ImldGXwtAqTtJ-Wr3fl48NSrjV5PJbFVVdhsv5n41LR6nf5mP3EYzVl_r2EgY45R2J-H_ANEIzTwiNK0YbG3xtEoGzZgEzADYifejPVLEL_T1AtrLU13c9fTae1L9Ns19NWZ1s8LKJgtew7SuEokE-v-XuiFrC4LlA2GeX2FhlXs-1aR2RJcyEUGWnWy9r5S5NGLczON89D4vHl7L3iP3XW1vnNFVypg7OPQKHrQ1ujc7YelEQtRNxDhM7HOlWCe_iIViYXl7SfH_TkY0TATRn6jCrpwk1Xy64ev1EQpEiAjWrOEwyTD_-bFF0EUTb1dmxWh7ftAxsDqPNsN6JmAQm2GafRbrzE3lMFMw9CpODlrHNeChdHoS1uR9_X4Why7nXT2=w640-h426-no?authuser=2",
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
                    thumbnail_image_url="https://lh3.googleusercontent.com/1_D9MINB-WoJ41KoGb-oX16SvOzPQJOZcEoqtXP0idOgoRkdKVYJTS4ttjr34QPAzMjus1SjIbra0-9A6-TUcQLB7JbitIN4DfCl35So1b1Ra3f-oNVYqGiXSkd3LocvwNdzdOYlfbVQs0pUdNXV04k-KTtItucn3nVT82guv9ZDDDVF9uKtsO4pXEDz_SB-5rzsE2v-CGfRnJsTWbnH-4aDnuwNc2V1zKEoTtsbtVTEJn0kz7rfbUp0xGP59olRUDq9ptCTKX0w1dczmFFt1mH327H0hBz2c1kJSeLw9_uQ5fSxNRup5bPjrOah5SgcvpxY6msi9QeopE1Kv9mv7rV9dOaOSg8cePCFs_RVKVRoyfl6kvmIpxTp5Mmtcchu9VlBicZ9RELJpctJSI45UTPIEghEAMzu0tzSYiOnmNTb2kkU_bqLE8I5R6CvuL_HV1Zs3-qjSnkgC1Pv5KLKtF1c3rS4fAyrVS5dPggvCkMOewkegXJDfB6f5PqHvgV1LOUT2shLwkmBrtbe3YakzI4WsMDio7w4ylgmKF8NcdErcS6E0dA5ndz-YjVL7TKBLacKcdMKFcKuEUmAIyE-SB3qGCMPO2uYaiaO7GKirX2b-aFFUJgjV2T14TZGNd7iDJiBUWktGvRDZlS9my5KwB7saOfaj_vk2OtqR4Y3u24Xm4lNG6zYQvQIPmoU=w640-h427-no?authuser=2",
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
                    thumbnail_image_url="https://lh3.googleusercontent.com/O1OvFITs2p4OxD32zYHIDrCd7FYqHiqTZ9z9zzWNf9Yftjaj2KotLYVrE5FWgvS6g21YLdsERIrEWmieMeReG4KVPHxATn4VNhCJDvmwVyLJU5KK-qPSN0VY4wjwOXkqcu4TI6CiiniH13C2JWv3pncRZVWqDMy0VSW8iCHlOkdnj5jr7yYdmxdOmaXsfzOOo5DMqoezONNLNz0odJ-5eQr3aoDOLG7Nt2ov3DN1mR5VCdhH71pkD_Oo6TIRDN4_-ZsunModA7ZPHpS_yl-LY4829bAQ8SgMo9qz4uhpebo1eYandcEmlXoaManT7ZyJBi-M6SvtX1d5BFqNc8vi0n1bfPUQkEts37UwZ61eIQ30fSohEwJ_iIBClkJFnu9xC0ZBoesMlEOg-7Q13GeCe-j7UkgLQvb8Fy6hSygWuQWRzFtc93j8INVjUnWSJDh_UIOoLbbXCJcUhR7ROTZsyrtgTHRsPJOCynDxZasZA7lqzE-duFmLyUt9LTjiRYqS1utqDspUh7ILJA-j7mYx4mRb8F-nEfgK_LYD1lrNKQzLQ9JYugP0xVLBdOcfMr9CZYcPzpeq1aY-A1yCYvkj_K97wZLs6_T5oy0n8MC4BYviQbt1LcrYucFfkMDqFzeN-R1zHWfGOOmLVCLVbcs1w53nkYN8vJLCM9n4Ni4RuSwkK9LYRSD1yyBxxOW3=w640-h424-no?authuser=2",
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