from notes import containNotes, noteToNumber, notesToChord, chordList, chordToNote, chordListAlt, notesToScale, scaleList, scaleListAlt, scaleToNote
from transitions.extensions import GraphMachine
from utils import send_text_message, send_menu_carousel, send_chord, send_not_found, send_chord_note, send_scale, send_scale_note, send_fsm, send_demo


class TocMachine():
    def __init__(self):
        self.notes = []
        self.chord = -1
        self.scale = -1
        self.machine = GraphMachine(
            model=self, 
            **{
                "states":["start", "menu", "chord", "chordResult", "chordNote", "chordNoteRootnote", "chordNoteType"
                , "scale", "scaleResult", "scaleNote", "scaleNoteRootnote", "scaleNoteType", "fsm", "demo"],
                "transitions":[
                    {
                        "trigger": "advance",
                        "source": "*",
                        "dest": "fsm",
                        "conditions": "is_going_to_fsm",
                    },
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
                    {
                        "trigger": "advance",
                        "source": "chordNoteType",
                        "dest": "chordNoteType",
                        "conditions": "is_going_to_chordNoteType",
                    },
                    {
                        "trigger": "advance",
                        "source": "chordNoteType",
                        "dest": "chordNoteRootnote",
                        "conditions": "is_going_to_chordNoteRootnote",
                    },
                    {
                        "trigger": "advance",
                        "source": "menu",
                        "dest": "scale",
                        "conditions": "is_going_to_scale",
                    },
                    {
                        "trigger": "advance",
                        "source": "menu",
                        "dest": "scaleNote",
                        "conditions": "is_going_to_scaleNote",
                    },
                    {
                        "trigger": "advance",
                        "source": "scale",
                        "dest": "scaleResult",
                        "conditions": "is_going_to_scaleResult",
                    },
                    {
                        "trigger": "advance",
                        "source": "scaleResult",
                        "dest": "scaleResult",
                        "conditions": "is_going_to_scaleResult",
                    },
                    {
                        "trigger": "advance",
                        "source": "scaleNote",
                        "dest": "scaleNoteRootnote",
                        "conditions": "is_going_to_scaleNoteRootnote",
                    },
                    {
                        "trigger": "advance",
                        "source": "scaleNoteRootnote",
                        "dest": "scaleNoteType",
                        "conditions": "is_going_to_scaleNoteType",
                    },
                    {
                        "trigger": "advance",
                        "source": "scaleNoteType",
                        "dest": "scaleNote",
                        "conditions": "is_going_back_to_scaleNote",
                    },
                    {
                        "trigger": "advance",
                        "source": "scaleNoteType",
                        "dest": "scaleNoteType",
                        "conditions": "is_going_to_scaleNoteType",
                    },
                    {
                        "trigger": "advance",
                        "source": "scaleNoteType",
                        "dest": "scaleNoteRootnote",
                        "conditions": "is_going_to_scaleNoteRootnote",
                    },
                    {
                        "trigger": "advance",
                        "source": "chordNoteType",
                        "dest": "chordNote",
                        "conditions": "is_going_to_change_rootNote",
                    },
                    {
                        "trigger": "advance",
                        "source": "chordNoteType",
                        "dest": "chordNoteRootnote",
                        "conditions": "is_going_to_change_type",
                    },
                    {
                        "trigger": "advance",
                        "source": "scaleNoteType",
                        "dest": "scaleNote",
                        "conditions": "is_going_to_change_rootNote",
                    },
                    {
                        "trigger": "advance",
                        "source": "scaleNoteType",
                        "dest": "scaleNoteRootnote",
                        "conditions": "is_going_to_change_type",
                    },
                    {
                        "trigger": "advance",
                        "source": "fsm",
                        "dest": "menu",
                        "conditions": "is_going_to_menu",
                    },
                    {
                        "trigger": "advance",
                        "source": "menu",
                        "dest": "demo",
                        "conditions": "is_going_to_demo",
                    },
                    {
                        "trigger": "advance",
                        "source": "demo",
                        "dest": "menu",
                        "conditions": "is_going_to_menu",
                    },
                ],
                "initial":"start",
                "auto_transitions":False,
                "show_conditions":True,
            },
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
        return "和弦" in text and "組成音" in text

    def is_going_to_chordResult(self, event):
        print("!" + str(self.notes))
        text = event.message.text
        if(len(containNotes(text)) != 0): self.notes = containNotes(text)
        return len(containNotes(text)) != 0

    def is_going_to_chordNoteRootnote(self, event):
        text = event.message.text
        if(len(containNotes(text)) != 0): self.notes = containNotes(text)
        return len(containNotes(text)) != 0

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
        if self.chord == -1:
            for i in range(len(chordListAlt)):
                for j in range(len(chordListAlt[i])):
                    if str(text).lower() == chordListAlt[i][j]:
                        self.chord = i
                        break
                else:
                    continue
                break
        return self.chord != -1

    def is_going_back_to_chordNote(self, event):
        text = event.message.text
        return "重來" in text or "再來" in text or "重查" in text

    def is_going_to_scale(self, event):
        text = event.message.text
        return "音階" in text and "組成音" not in text

    def is_going_to_scaleNote(self, event):
        text = event.message.text
        return "音階" in text and "組成音" in text

    def is_going_to_scaleResult(self, event):
        text = event.message.text
        if(len(containNotes(text)) != 0): self.notes = containNotes(text)
        return len(containNotes(text)) != 0

    def is_going_to_scaleNoteRootnote(self, event):
        text = event.message.text
        if(len(containNotes(text)) != 0): self.notes = containNotes(text)
        return len(containNotes(text)) != 0

    def is_going_to_scaleNoteType(self, event):
        self.scale = -1
        text = event.message.text
        text = text.strip()
        for i in range(len(scaleList)):
            for j in range(len(scaleList[i])):
                if text == scaleList[i][j]:
                    self.scale = i
                    break
            else:
                continue
            break
        if self.scale == -1:
            for i in range(len(scaleListAlt)):
                for j in range(len(scaleListAlt[i])):
                    if str(text).lower() == scaleListAlt[i][j]:
                        self.scale = i
                        break
                else:
                    continue
                break
        return self.scale != -1

    def is_going_back_to_scaleNote(self, event):
        text = event.message.text
        return "重來" in text or "再來" in text or "重查" in text

    def is_going_to_change_rootNote(self, event):
        text = event.message.text
        return "更改" in text and "根音" in text

    def is_going_to_change_type(self, event):
        text = event.message.text
        return "更改" in text and "種類" in text

    def is_going_to_fsm(self, event):
        text = event.message.text
        return "fsm" in str(text).lower()

    def is_going_to_demo(self, event):
        text = event.message.text
        return "demo" in str(text).lower()

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
        text = "請先輸入和弦的「根音」，或點選下方常用音符。"
        send_text_message(reply_token, text, "note")

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
        text = "請輸入和弦「種類」，或點選下方常用和弦。"
        send_text_message(reply_token, text, "chord")

    def on_enter_chordNoteType(self, event):
        print("I'm entering chordNoteType")
        reply_token = event.reply_token
        print(self.notes)
        text = chordToNote(self.notes, self.chord)
        send_chord_note(reply_token, self.notes[0], self.chord, text)

    def on_enter_scale(self, event):
        print("I'm entering scale")
        reply_token = event.reply_token
        text = "請輸入數個音符（A~G，可搭配升降記號）。我會想辦法告訴你他們可以組成的音階。"
        send_text_message(reply_token, text)
    
    def on_enter_scaleNote(self, event):
        print("I'm entering scaleNote")
        reply_token = event.reply_token
        text = "請先輸入音階的「根音」，或點選下方常用音符。"
        send_text_message(reply_token, text, "note")

    def on_enter_scaleResult(self, event):
        print("I'm entering scaleResult")
        reply_token = event.reply_token
        print(self.notes)
        root_note, whichScale = notesToScale(self.notes)
        if whichScale > -1:
            send_scale(reply_token, root_note, whichScale)
        else:
            send_not_found(reply_token)

    def on_enter_scaleNoteRootnote(self, event):
        print("I'm entering scaleNoteRootnote")
        reply_token = event.reply_token
        text = "請輸入音階「種類」，或點選下方常用音階。"
        send_text_message(reply_token, text, "scale")

    def on_enter_scaleNoteType(self, event):
        print("I'm entering chordNoteType")
        reply_token = event.reply_token
        print(self.notes)
        text = scaleToNote(self.notes, self.scale)
        send_scale_note(reply_token, self.notes[0], self.scale, text)

    def on_enter_fsm(self, event):
        print("I'm entering fsm")
        reply_token = event.reply_token
        send_fsm(reply_token)

    def on_enter_demo(self, event):
        print("I'm entering demo")
        reply_token = event.reply_token
        send_demo(reply_token)