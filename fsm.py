from notes import containNotes, noteToNumber, notesToChord
from transitions.extensions import GraphMachine
from utils import send_text_message, send_menu_carousel


class TocMachine():
    def __init__(self):
        self.notes = []
        self.machine = GraphMachine(
            model=self, 
            **{
                "states":["start", "menu", "chord", "chordResult", "chordNote"],
                "transitions":[
                    {
                        "trigger": "advance",
                        "source": "*",
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
                    {
                        "trigger": "advance",
                        "source": "chord",
                        "dest": "chordResult",
                        "conditions": "is_going_to_chordResult",
                    },
                    {
                        "trigger": "advance",
                        "source": "chordResult",
                        "dest": "chordResult",
                        "conditions": "is_going_to_chordResult",
                    },
                ],
                "initial":"start",
                "auto_transitions":False,
                "show_conditions":True,
            }
        )

    #condition
    def is_going_to_menu(self, event):
        text = event.message.text
        return "選單" in text

    def is_going_to_chord(self, event):
        text = event.message.text
        return "和弦" in text and "組成音" not in text

    def is_going_to_chordNote(self, event):
        text = event.message.text
        return "組成音" in text

    def is_going_to_chordResult(self, event):
        text = event.message.text
        self.notes = containNotes(text)
        return len(self.notes) is not 0

    #on enter
    def on_enter_menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        send_menu_carousel(reply_token)

    def on_enter_chord(self, event):
        print("I'm entering chord")
        reply_token = event.reply_token
        text = "請輸入數個音符（A~G，可搭配升降記號）。我會想辦法告訴你他們可以組成的和弦。"
        send_text_message(reply_token, text)
    
    def on_enter_chordNote(self, event):
        print("I'm entering chordNote")
        reply_token = event.reply_token
        text = "請輸入和弦的英文名稱，我會想辦法告訴你他是由什麼音符組成的。"
        send_text_message(reply_token, text)

    def on_enter_chordResult(self, event):
        print("I'm entering chordResult")
        reply_token = event.reply_token
        print(self.notes)
        text = notesToChord(self.notes)
        send_text_message(reply_token, text)