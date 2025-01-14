# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    res = ""
    for ch in seq:
        if ch in ALLOWED_NUC:
            res += TRANSCRIPTION_MAPPING[ch]
        else:
            raise ValueError("Incompatible characters")
    
    if reverse:
        return res[::-1]

    return res

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    # Hey this is my comment
    # Again!
    return transcribe(seq,True)