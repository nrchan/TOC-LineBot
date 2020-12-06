from notes import containNotes, noteToNumber, notesToChord, chordList, chordToNote
from transitions.extensions import GraphMachine
from utils import send_text_message, send_menu_carousel, send_chord, send_not_found


class TocMachine():
    def __init__(self):
        self.notes = []
        self.chord = -1
        self.machine = GraphMachine(
            model=self, 
            **{
                "states":["start", "menu", "chord", "chordResult", "chordNote", "chordNoteRootnote", "chordNoteType"],
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
                    {
                        "trigger": "advance",
                        "source": "chordNote",
                        "dest": "chordNoteRootnote",
                        "conditions": "is_going_to_chordNoteRootnote",
                    },
                    {
                        "trigger": "advance",
                        "source": "chordNoteRootnote",
                        "dest": "chordNoteType",
                        "conditions": "is_going_to_chordNoteType",
                    },
                    {
                        "trigger": "advance",
                        "source": "chordNoteType",
                        "dest": "chordNote",
                        "conditions": "is_going_back_to_chordNote",
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

    def is_going_to_chordNoteRootnote(self, event):
        text = event.message.text
        self.notes = containNotes(text)
        return len(self.notes) is not 0

    def is_going_to_chordNoteType(self, event):
        self.chord = -1
        text = event.message.text
        text = text.strip()
        for i in range(len(chordList)):
            for j in range(len(chordList[i])):
                if text == chordList[i][j]:
                    self.chord = i
                    break
            else:
                continue
            break
        return self.chord is not -1

    def is_going_back_to_chordNote(self, event):
        text = event.message.text
        return "重來" in text or "再來" in text or "重查" in text

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
        text = "請先輸入和弦的「根音」。"
        send_text_message(reply_token, text)

    def on_enter_chordResult(self, event):
        print("I'm entering chordResult")
        reply_token = event.reply_token
        print(self.notes)
        root_note, whichChord = notesToChord(self.notes)
        if whichChord > -1:
            send_chord(reply_token, root_note, whichChord)
        else:
            send_not_found(reply_token)

    def on_enter_chordNoteRootnote(self, event):
        print("I'm entering chordNoteRootnote")
        reply_token = event.reply_token
        text = "請輸入和弦「種類」。"
        send_text_message(reply_token, text)

    def on_enter_chordNoteType(self, event):
        print("I'm entering chordNoteType")
        reply_token = event.reply_token
        text = chordToNote(self.notes, self.chord)
        send_text_message(reply_token, text)