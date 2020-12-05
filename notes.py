import re

note = r"([A-G])([#|x|b|bb])?"

noteNumDict = {
    "C"  : "0",
    "B#" : "0",
    "Dbb": "0",
    "Bx" : "1",
    "C#" : "1",
    "Db" : "1",
    "Cx" : "2",
    "D"  : "2",
    "Ebb": "2",
    "D#" : "3",
    "Eb" : "3",
    "Fbb": "3",
}

#convert note to corresponding number, starting from C = 0, B = 12
def noteToNumber(note):
    return noteNumDict.get(note, -1)

#return all notes in text
def containNotes(text):
    return re.findall(note, text)