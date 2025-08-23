# Open reading frame is defined as spans of DNA sequences between start and end codon
# This program will only accepts mRNA sequence



import re

import is_valid


def search_for_orf(sequence) :
    if not is_valid.is_mrna(sequence) :
        raise ValueError('Invalid mRNA sequence')
    orfs_spans = {}
    sequence = sequence.upper()
    valid_orf = 'AUG(?:[AUGC]{3})*?(UAA|UAG|UGA)'
    for match in re.finditer(valid_orf, sequence):
        orfs_spans.update({match.group(0) : match.span(0)}) # end of this loop we should have a dictionary of orfs and their span
    if not orfs_spans :
        return None
    longest_orf = max(orfs_spans.keys(), key = len)
    return longest_orf, orfs_spans[longest_orf]

