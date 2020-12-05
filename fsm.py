from transitions.extensions import GraphMachine

from utils import send_text_message, send_menu_carousel


class TocMachine():
    def __init__(self):
        self.machine = GraphMachine(
            model=self, 
            **{
                "states":["start", "menu", "user", "state1"],
                "transitions":[
                    {
                        "trigger": "advance",
                        "source": "start",
                        "dest": "menu",
                        "conditions": "is_going_to_menu",
                    },
                    {
                        "trigger": "advance",
                        "source": "user",
                        "dest": "state1",
                        "conditions": "is_going_to_state1",
                    },
                ],
                "initial":"start",
                "auto_transitions":False,
                "show_conditions":True,
            }
        )

    def is_going_to_menu(self, event):
        text = event.message.text
        return "主選單" == text

    def on_enter_menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        send_menu_carousel(reply_token)

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")

    def on_exit_state1(self, event):
        print("Leaving state1")