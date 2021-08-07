import pychord
from pychord import Chord

class generator:
    def __init__(self, start, length, end=None, majmin="maj", note="A"):
        self.start = start
        self.end = end
        self.length = length
        self.chords = []
        self.majmin = majmin
        if type(self.majmin) != str:
            raise AssertionError("Type of majmin must be a string")
        self.note = note
        self.trans_maj = [1, 3, 6, 4, 5] # tune to liking
        self.trans_min = [1, 7, 3, 6, 4, 5] # tune to liking
        if self.end is not None and type(self.end) == int:
            self.length -= self.end
        self.init_progression()

    def __repr__(self) -> str:
        return self.start, self.end, self.length

    def note_append(self, num):
        factors = list("ABCDEFG")
        return str(factors[num]) + self.majmin

    def init_progression(self):
        if self.majmin == "maj":
            trans = self.trans_maj
        elif self.majmin == "min":
            trans = self.trans_min
        else:
            raise AssertionError("Unsupported key")
        for i in range(self.start, self.length):
            this_chord_degree = trans[i]
            this_chord = Chord.from_note_index(
                note=this_chord_degree,
                quality=self.majmin,
                scale=self.note_append(i)
            )
            self.chords.append(this_chord)
    
    def next_chord(self):
        next = self.chords.pop(0)
        return next

    def transpose(self, degree):
        newchords = []
        for eachchord in self.chords:
            transposed = eachchord.transpose(degree)
            newchords.append(transposed)
        
        self.chords = newchords