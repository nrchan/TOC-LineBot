import re

note = r"[A-G]#?b{0,2}"

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

diffList = [
    [4,3],
]

chordList = [
    "Major"
]

#convert note to corresponding number, starting from C = 0, B = 11
def noteToNumber(note):
    return noteNumDict.get(note, -1)

#return all notes in text
def containNotes(text):
    return re.findall(note, text)

def notesToChord(noteList):
    numList = []
    for i in range(len(noteList)):
        numList.append(noteToNumber(noteList[i]))
    for i in range(1, len(numList)):
        if numList[i] < numList[0]:
            numList[i] = (numList[i] + 12) % 12
    diff = []
    for i in range(1, len(numList)):
        diff.append(numList[i] - numList[i-1])
    whichChord = -1
    for i in range(len(diffList)):
        if whichChord != -1:
            whichChord -= 1
            break
        if len(diff) != len(diffList[i]):
            continue
        for j in range(len(diffList[i])):
            if diff[j] != diffList[i][j]:
                continue
            if j == len(diffList[i])-1:
                whichChord = i
                break
    if whichChord < len(chordList):
        result = noteList[0] + " " + chordList[whichChord]
    else:
        result = "找...找不到"
    return result
    