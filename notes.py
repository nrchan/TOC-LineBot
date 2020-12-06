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
    #major
    [4,3],
    [4,3,4],
    [4,3,4,3],
    #minor
    [3,4],
    [3,4,3],
    [3,4,4],
    [3,4,3,4],
    #domiant
    [4,3,3],
    [4,3,3,4],
    #half dim
    [3,3,4],
    #dim
    [3,3,3],
    #aug
    [4,4],
    [4,4,2],
    [4,4,3],
    #6
    [4,3,2],
    #sus4
    [5,2],
    #sus2
    [2,5],
]

chordList = [
    ["Major", "大和弦", ""],
    ["Major 7", "大七和弦", "Maj", "Maj7", "M7", "Δ7"],
    ["Major 9", "大九和弦", "9", "Maj9", "M9", "Δ9"],
    ["Minor", "小和弦", "m", "-"],
    ["Minor 7", "小七和弦", "m7", "-7"],
    ["Minor Major 7", "小大七和弦", "mmaj7", "mM7", "-Δ7"],
    ["Minor 9", "小九和弦", "m9", "-9"],
    ["Dominant 7", "屬七和弦", "7"],
    ["Dominant 9", "屬九和弦", "9"],
    ["Half diminished 7", "半減七和弦", "ø", "m7(b5)"],
    ["Diminished 7", "減七和弦", "dim", "o"],
    ["Augmented", "增和弦", "aug", "+"],
    ["Augmented 7", "增屬七和弦", "aug7", "+7"],
    ["Augmented Major 7", "增大七和弦", "augM7", "+Δ7", "M7(#5)"],
    ["6", "六和弦", "6"],
    ["Suspended 4", "掛留四和弦", "sus4", "sus"],
    ["Suspended 2", "掛留二和弦", "sus2"],
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
            numList[i] = numList[i] + 12
    numList = numList[0:1] + sorted(numList[1:])
    diff = []
    for i in range(1, len(numList)):
        diff.append(numList[i] - numList[i-1])
    whichChord = -100
    for i in range(len(diffList)):
        if whichChord != -100:
            break
        if len(diff) != len(diffList[i]):
            continue
        for j in range(len(diffList[i])):
            if diff[j] != diffList[i][j]:
                break
            if j == len(diffList[i])-1:
                whichChord = i
                break
    
    print("whichChord = " + str(whichChord) + " diff = " + str(diff))
    if whichChord >= len(chordList) or whichChord <= -1:
        whichChord = -1
    return noteList[0], whichChord
    