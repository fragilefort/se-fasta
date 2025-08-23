import re


def is_mrna(sequence) :
    sequence = sequence.upper()
    invalid = r'[^AUGC]'
    mrna = True
    if re.search(invalid, sequence) :
        mrna = False
    return mrna


def is_dna(sequence) :
    sequence = sequence.upper()
    invalid = r'[^ATGC]'
    mrna = True
    if re.search(invalid, sequence) :
        mrna = False
    return mrna


def is_valid_sequence(sequence) :
    return (is_mrna(sequence) or is_dna(sequence))
