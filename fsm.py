from transitions.extensions import GraphMachine

from utils import send_text_message, send_menu_carousel


class TocMachine():
    def __init__(self):
        self.machine = GraphMachine(
            model=self, 
            **{
                "states":["start", "menu", "chord", "chordNote"],
                "transitions":[
                    {
                        "trigger": "advance",
                        "source": "start",
                        "dest": "menu",
                        "conditions": "is_going_to_menu",
                    },
                    {
                        "trigger": "advance",
                        "source": "menu",
                        "dest": "chord",
                        "conditions": "is_going_to_chord",
                    },
                    {
                        "trigger": "advance",
                        "source": "menu",
                        "dest": "chordNote",
                        "conditions": "is_going_to_chordNote",
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

    def is_going_to_chord(self, event):
        text = event.message.text
        return "查和弦" in text

    def is_going_to_chordNote(self, event):
        text = event.message.text
        return "查和弦組成音" in text

    def on_enter_menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        send_menu_carousel(reply_token)