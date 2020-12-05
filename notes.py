import re

note = r"([A-G])([#|x|b|bb])?"

noteNumDict = {
    "C"  : "0",
    "B#" : "0",
    "Dbb": "0",
}

def noteToNumber(note):
    return noteNumDict.get(note, -1)

def containNotes(text):
    return re.search(note, text)