import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, CarouselTemplate, CarouselColumn, MessageTemplateAction, TemplateSendMessage


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
                    thumbnail_image_url="https://lh3.googleusercontent.com/vN8XGBLZLmI7R2f1xY8Sp1Zu_qoJdDSkb7I-pvY04NUJ_Z8U0cAYVaRRH6hJfa0eiw3qMYV9kmvP6xhR-KtrfS74SCV1s-vum7PjoX7Q44yquFB58-NXqARlCbk05_I3bVuzckhdSFz-vI_Fpzfo3WIcnWOkRNNquDXYs6EBEob0KnGUm8gCyaptr4qEK3pO2-YLcYfvDEJhZBfr7iJVTAICaL64H5-eujLGq0RToYybu6B-jhOEpd8jNDZeolvXQLqXjfG6aI6kkNRtA7lFLCBTtrbc0_aN01TFq-ESQGQ27LBKGCB1DyPMKkVuXzJoQ0k-kg-6Bgj_UijC9nzooqrxpaMzZm_Peq_0hQKDRz8utdThO8GJta1ORi_2fDhfK9ft23CwhugdS0r2SJj1Og-wpsqbWDc6x844-20edEHYs4F02kPehXcol_Ue3wVdvy53P_WfyngezCdLIPQrUJqkolNPwmnqJO5QyTNs9EMCC2WnCo4FQopWqNeP0KFHa6cVSHfT0BhPI9hjwISI5SH6CFe--VTIW9YFmBo_lcwe8e2BT3adHF2kr--ULhVGimEcHHdK6ZM4J4Psi93xY6lWuMGONBxxPL42GIXY1OKyQrlrEkb4152zfqb50NYd4FfbehJ9wSnvvwZ61RW0662x3nA1x4Z63NiJjrrj-MPz0VosqhFHGkeLaCUQ=w640-h384-no?authuser=2",
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
                    thumbnail_image_url="https://lh3.googleusercontent.com/rNgF3mEDpaxpODit5sMYnWYzJRU30nZ4A8o05IhxSpSxin_qTtf8kD9x16dQMPthJvCyfbwldocqKlaH97XdC1wErJqEH9pP2xwOkRUWNNwTsTU0mK4vmuiB8ndexWV9ZK85-qRLqCxIDCjLFFTgt-Fn5Ggz_ppk5tPJgqMt8s95zfgrutXV_m1l0Z_-uQyiHLyVWlpsyB0zTwCkTl4E2ErN8U3niFW9Xd_RmBAupMfG1sqeYR4LwdbIaykYA45en0Q0YLc-gpyC5tkZffa3bj5_utymySZgqdTL6CJ8n-1UKyFRPS7UY0t4jpWb3e3HYY6Wyz6KRJmqEPORRaIRTaL6iVUOB6dKO_ejK1UiDVwAYBFEfT4SOkNd-hq4aQ85rco87QAFm1vAfbJErZ9YTq5bql2pJG8DoblyY7B5XI59nhC5iPy7Q0s2Q2QrQc4xiBrCAaIRZ5l7EbDxA-I0xcspJrnTVJnDKkPNMdH2is-tZVx10R5M8qj74NFqz0L0U5adA1qXeG9KZRpilXKhLNL4uOhS-FPDp5ESbRLWudh9NXDRQzQdknYnGvtIAwTHKtVsOwnCsXfoyj3I8HnWayOSIsR95_fACJ80TJ22GV3K0t8nahvSnTRLuq2Ns8ziEHeI2vIbcdVQ9x7i86R5HXFPonTi8EjYrAwZDv8SvulxBRUxQDeXthKmUK3h=w640-h384-no?authuser=2",
                    actions=[
                        MessageTemplateAction(
                            label="查詢",
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