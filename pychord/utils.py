# -*- coding: utf-8 -*-
if __name__!="__main__":
    from .constants import NOTE_VAL_DICT, SCALE_VAL_DICT

def roman_numeral_parser(string):
    def romanToInt(s):
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      # TODO: add this dict to the constants files
      i = 0
      num = 0
      while i < len(s):
         if i+1<len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]]
            i+=2
         else:
            #print(i)
            num+=roman[s[i]]
            i+=1
      return num
    numbrz = [str(i) for i in list(range(0,10))]
    chords = string.split("-")
    ret_list = []
    for chord in chords:
        prs_chord = chord
        quality = ""
        for numbr in numbrz:
            if numbr in prs_chord:
                prs_chord = prs_chord.replace(numbr, "")
                quality = numbr
        ret_list.append((romanToInt(prs_chord), quality))
    return ret_list

def note_to_val(note):
    """ Convert note to int

    >>> note_to_val("C")
    0
    >>> note_to_val("B")
    11

    :type note: str
    :rtype: int
    """
    if note not in NOTE_VAL_DICT:
        raise ValueError("Unknown note {}".format(note))
    return NOTE_VAL_DICT[note]


def val_to_note(val, scale="C"):
    """ Convert int to note

    >>> val_to_note(0)
    "C"
    >>> val_to_note(11, "D")
    "D#"

    :type val: int
    :param str scale: key scale
    :rtype: str
    """
    val %= 12
    return SCALE_VAL_DICT[scale][val]


def transpose_note(note, transpose, scale="C"):
    """ Transpose a note

    :param str note: note to transpose
    :type transpose: int
    :param str scale: key scale
    :rtype: str
    :return: transposed note
    """
    val = note_to_val(note)
    val += transpose
    return val_to_note(val, scale)


def display_appended(appended):
    # TODO: Implement this
    return ""


def display_on(on_note):
    if on_note:
        return "/{}".format(on_note)
    return ""

if __name__=="__main__":
    print(roman_numeral_parser("I-IV-V7-I"))