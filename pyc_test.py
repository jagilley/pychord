import pychord
from pychord import Chord

for i in range(1,9):
    print(Chord.from_note_index(note=i, quality="", scale="Cdor"))