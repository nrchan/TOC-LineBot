from transitions.extensions import GraphMachine

from utils import send_text_message, send_menu_carousel


class TocMachine():
    def __init__(self):
        self.machine = GraphMachine(
            model=self, 
            **{
                "states":["start", "menu"],
                "transitions":[
                    {
                        "trigger": "advance",
                        "source": "start",
                        "dest": "menu",
                        "conditions": "is_going_to_menu",
                    },
                ],
                "initial":"start",
                "auto_transitions":False,
                "show_conditions":True,
            }
        )

    def is_going_to_menu(self, event):
        text = event.message.text
        return "選單" in text

    def on_enter_menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        send_text_message(reply_token, "選擇想要的功能吧！😉")
        send_menu_carousel(reply_token)