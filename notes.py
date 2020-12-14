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

#chord

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
    ["Sixth", "大六和弦", "6", "M6"],
    ["Suspended 4", "掛留四和弦", "sus4", "sus"],
    ["Suspended 2", "掛留二和弦", "sus2"],
]

chordListAlt = [
    ["major", "大調", "三和弦", "大三和弦", "3", "大三", "大3", "大 3"],
    ["major 7", "七和弦", "大七", "maj7", "maj 7"],
    ["major 9", "九和弦", "大九", "maj9", "maj 9"],
    ["minor", "小調", "小三和弦", "小三", "小3", "小 3"],
    ["minor 7", "小七", "小7", "小 7"],
    ["minor major 7", "mmaj7", "mm7", "-大7", "小Δ7", "小大七", "小大7", "mmaj 7", "mm 7", "-大 7" "小大 7"],
    ["minor 9", "小九", "小9", "小 9"],
    ["dominant 7", "屬七", "屬7", "屬 7", "七", "7"],
    ["dominant 9", "屬九", "屬9", "屬 9", "九", "9"],
    ["half diminished 7", "半減七", "半減7", "半減 7", "小七降五", "小7降5", "小七b5", "小七 b5", "half diminish","半減"],
    ["diminished 7", "diminish 7", "diminish", "減七", "減7", "減 7"],
    ["augmented", "增", "增三", "增3", "增 3"],
    ["augmented 7", "增七和弦", "增屬七", "增七", "增7", "增 7", "增屬7", "增屬 7"],
    ["augmented major 7", "增大七", "增大7", "增大 7", "大7升5", "大七升五"],
    ["sixth", "大六", "大6", "大 6", "六", "Δ6"],
    ["suspended 4", "suspended", "suspend 4", "suspend", "掛留四", "掛留4", "掛四", "掛4", "sus 4", "sus"],
    ["suspended 2", "suspend 2", "掛留二", "掛留2", "掛二", "掛2", "sus 2"],
]

diffSeven = [
    #major
    [2,2],
    [2,2,2],
    [2,2,2,2],
    #minor
    [2,2],
    [2,2,2],
    [2,2,2],
    [2,2,2,2],
    #domiant
    [2,2,2],
    [2,2,2,2],
    #half dim
    [2,2,2],
    #dim
    [2,2,2],
    #aug
    [2,2],
    [2,2,2],
    [2,2,2],
    #6
    [2,2,1],
    #sus4
    [3,1],
    #sus2
    [1,3],
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

def chordToNote(noteList, whichChord):
    sevenRootnote = notesToSevenNum(noteList[0])
    sevenList = [sevenRootnote]
    for i in range(len(diffSeven[whichChord])):
        sevenRootnote = (sevenRootnote + diffSeven[whichChord][i])%7
        sevenList.append(sevenRootnote)
    rootnote = noteToNumber(noteList[0])
    notes = [rootnote]
    for i in range(len(diffList[whichChord])):
        rootnote = (rootnote + diffList[whichChord][i])%12
        notes.append(rootnote)
    print("whichChord = " + str(whichChord) + " seven = " + str(sevenList) + " notesnum = " + str(notes))
    result = str(sevenNumToNote(sevenList[0], notes[0]))
    for i in range(1,len(notes)):
        result = result + "、" + str(sevenNumToNote(sevenList[i], notes[i]))
    return result
    
def notesToSevenNum(note):
    note = note[0]
    return {
        "C" : 0,
        "D" : 1,
        "E" : 2,
        "F" : 3,
        "G" : 4,
        "A" : 5,
        "B" : 6,
    }.get(note, -1)

def sevenNumToNote(seven, note):
    if seven == 0:
        if   note == 0: return "C"
        elif note == 1: return "C#"
        elif note == 2: return "Cx"
        elif note ==11: return "Cb"
        elif note ==10: return "Cbb"
    elif seven == 1:
        if   note == 2: return "D"
        elif note == 3: return "D#"
        elif note == 4: return "Dx"
        elif note == 1: return "Db"
        elif note == 0: return "Dbb"
    elif seven == 2:
        if   note == 4: return "E"
        elif note == 5: return "E#"
        elif note == 6: return "Ex"
        elif note == 3: return "Eb"
        elif note == 2: return "Ebb"
    elif seven == 3:
        if   note == 5: return "F"
        elif note == 6: return "F#"
        elif note == 7: return "Fx"
        elif note == 4: return "Fb"
        elif note == 3: return "Fbb"
    elif seven == 4:
        if   note == 7: return "G"
        elif note == 8: return "G#"
        elif note == 9: return "Gx"
        elif note == 6: return "Gb"
        elif note == 5: return "Gbb"
    elif seven == 5:
        if   note == 9: return "A"
        elif note ==10: return "A#"
        elif note ==11: return "Ax"
        elif note == 8: return "Ab"
        elif note == 7: return "Abb"
    elif seven == 6:
        if   note ==11: return "B"
        elif note == 0: return "B#"
        elif note == 1: return "Bx"
        elif note ==10: return "Bb"
        elif note == 9: return "Bbb"

#scale

scaleDiffList = [
    #modern modes
    [2,2,1,2,2,2],
    [2,1,2,2,2,1],
    [1,2,2,2,1,2],
    [2,2,2,1,2,2],
    [2,2,1,2,2,1],
    [2,1,2,2,1,2],
    [1,2,2,1,2,2],
    #two more minor
    [2,1,2,2,1,3],
    [2,1,2,2,2,2],
    #modern modes with accidentals
    [2,1,3,1,2,1],
    [1,2,2,2,2,1],
    [2,1,2,1,2,2],
    [1,2,2,1,3,1],
    [3,1,2,1,2,2],
    [2,2,2,1,2,1],
    [2,2,1,2,1,2],
    [1,3,1,2,1,2],
    #whole tone
    [2,2,2,2,2],
    #altered
    [1,2,1,2,2,2],
    [1,2,1,2,2,1],
    #diminished
    [1,2,1,2,1,2,1],
    [2,1,2,1,2,1,2],
    #pentatonic
    [2,2,3,2],
    [2,3,2,3],
    [3,2,3,2],
    [2,3,2,2],
    [3,2,2,3],
]

scaleList = [
    ["Ionian", "大調"],
    ["Dorian", "Dor."],
    ["Phrygian", "Phry."],
    ["Lydian", "Lyd."],
    ["Mixolydian", "Mixo."],
    ["Aeolian", "自然小音階"],
    ["Locrian", "Loc."],
    ["Harmonic minor", "和聲小音階"],
    ["Melodic minor", "旋律小音階"],
    ["Dorian #4", "Dor. #4"],
    ["Dorain b2", "Dor. b2"],
    ["Locrian 2", "Loc. 2"],
    ["Locrian 6", "Loc. 6"],
    ["Lydian #9", "Lyd. #9"],
    ["Lydian b7", "Lyd. b7"],
    ["Mixolydian b6", "Mixo. b6"],
    ["Mixolydian b2, b6", "Mixo. b2 b6"],
    ["Whole tone", "全音音階"],
    ["Altered", "alt."],
    ["Altered bb7", "alt. bb7"],
    ["Diminished (Half-Whole)", "半全音階"],
    ["Diminished (Whole-Half)", "全半音階"],
    ["Major pentatonic", "宮調式"],
    ["Egyptian", "商調式"],
    ["", "角調式"],
    ["", "徵調式"],
    ["Minor pentatonic", "羽調式"],
]

scaleListAlt = [
    ["Ionian", "大調"],
    ["Dorian", "Dor."],
    ["Phrygian", "Phry."],
    ["Lydian", "Lyd."],
    ["Mixolydian", "Mixo."],
    ["Aeolian", "自然小音階"],
    ["Locrian", "Loc."],
    ["Harmonic minor", "和聲小音階"],
    ["Melodic minor", "旋律小音階"],
    ["Dorian #4", "Dor. #4"],
    ["Dorain b2", "Dor. b2"],
    ["Locrian 2", "Loc. 2"],
    ["Locrian 6", "Loc. 6"],
    ["Lydian #9", "Lyd. #9"],
    ["Lydian b7", "Lyd. b7"],
    ["Mixolydian b6", "Mixo. b6"],
    ["Mixolydian b2, b6", "Mixo. b2 b6"],
    ["Whole tone", "全音音階"],
    ["Altered", "alt."],
    ["Altered bb7", "alt. bb7"],
    ["Diminished (Half-Whole)", "半全音階"],
    ["Diminished (Whole-Half)", "全半音階"],
    ["Major pentatonic", "宮調式"],
    ["Egyptian", "商調式"],
    ["", "角調式"],
    ["", "徵調式"],
    ["Minor pentatonic", "羽調式"],
]

def notesToScale(noteList):
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
    whichScale = -100
    for i in range(len(scaleDiffList)):
        if whichScale != -100:
            break
        if len(diff) != len(scaleDiffList[i]):
            continue
        for j in range(len(scaleDiffList[i])):
            if diff[j] != scaleDiffList[i][j]:
                break
            if j == len(scaleDiffList[i])-1:
                whichScale = i
                break
    
    print("whichScale = " + str(whichScale) + " diff = " + str(diff))
    if whichScale >= len(scaleList) or whichScale <= -1:
        whichScale = -1
    return noteList[0], whichScale
