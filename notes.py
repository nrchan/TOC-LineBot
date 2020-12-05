import re

noteBB = r"[A-G][#|x|bb]?"
noteB = r"[A-G][#|x|b]?"

noteNumDict = {
    "C"  : 0,
    "B#" : 0,
    "Dbb": 0,
    "Bx" : 1,
    "C#" : 1,
    "Db" : 1,
    "Cx" : 2,
    "D"  : 2,
    "Ebb": 2,
    "D#" : 3,
    "Eb" : 3,
    "Fbb": 3,
    "Dx" : 4,
    "E"  : 4,
    "Fb" : 4,
    "E#" : 5,
    "F"  : 5,
    "Gbb": 5,
    "Ex" : 6,
    "F#" : 6,
    "Gb" : 6,
    "Fx" : 7,
    "G"  : 7,
    "Abb": 7,
    "G#" : 8,
    "Ab" : 8,
    "Gx" : 9,
    "A"  : 9,
    "Bbb": 9,
    "A#" :10,
    "Bb" :10,
    "Cbb":10,
    "Ax" :11,
    "B"  :11,
    "Cb" :11,
}

#convert note to corresponding number, starting from C = 0, B = 11
def noteToNumber(note):
    return noteNumDict.get(note, -1)

#return all notes in text
def containNotes(text):
    BB = re.findall(noteBB, text)
    B = re.findall(noteB, text)
    print(BB)
    print(B)
    result = []
    for i in range(len(B)):
        if(BB[i] == B[i]):
            result.append(BB[i])
        elif(BB[i][0:1] == B[i][0:1]):
            result.append(BB[i])
        else:
            result.append(B[i])
            B.remove(B[i])
    return result

def notesToChord(noteList):
    numList = []
    for i in noteList:
        numList.append(noteToNumber(noteList[i]))