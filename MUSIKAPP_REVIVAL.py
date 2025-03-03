import re

class ChordAnalyser:

    sharp_flat_notes = {
        "sharp": ['C#', 'D#', 'F#', 'G#', 'A#', 'B#'],
        "flat": ['Db', 'Eb', 'Gb', 'Ab', 'Bb'],
        "natural": ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    }
    
    
    @staticmethod
    def is_valid_chord(chord):
        pattern = r"^[A-Ga-g](m|maj7|7|maj|sus[1-4])?(\/[A-Ga-g])?$"
        if re.match(pattern, chord):
            return True
        else:
            return False
    
    @staticmethod
    def chord_root(chord):
        if len(chord) > 1 and (chord[1] == '#' or chord[1] == 'b'):
            return chord[0:1]
        else:
            return chord[0]
   
    @staticmethod
    def is_minor(chord):
        if len(ChordAnalyser.chord_root(chord)) == 1 and len(chord) > 1 and chord[1] == 'm': # if natural root
            return True
        elif len(ChordAnalyser.chord_root(chord)) == 2 and len(chord) > 2 and chord[2] == 'm' # if sharp or flat root
            return True
        else:
            return False
    
    @staticmethod
    def is_sharp(chord):
        if ChordAnalyser.chord_root(chord) in ChordAnalyser.sharp_flat_notes["sharp"]:
            return True
        else:
            return False
    
    @staticmethod
    def chord_info(chord):
        
        print("Chord analysis: ")
        print(f"Root: {ChordAnalyser.chord_root(chord)}")
        print("Minor/Major: ", end=" ")
        print("Minor") if ChordAnalyser.is_minor(chord) else print("Major")
        print("#/b: ", end=" ")
        print("Sharp") if ChordAnalyser.is_sharp(chord) else print("Flat")
        



while 1:
    chord = input("Chord: ")
    ChordAnalyser.chord_info(chord)
    ChordAnalyser.is_minor(chord)
