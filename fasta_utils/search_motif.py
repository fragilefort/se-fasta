# This should allow users to search for a particular motif in a sequence
# well, it should give how many occurances, and where and list them
# It will be done using regex using the re built-in package 
# It can accept both DNA and RNA sequences so the main script will handle the validation


import re


def search_for_motif(sequence, motif) :
    it = re.finditer(motif, sequence)
    matches = [] 
    for match in it :
        pair= (match.span(0))
        matches.append(pair)
    return matches



def count_motif(sequence, motif) :
    it = re.finditer(motif.upper(), sequence.upper())
    matches = [] 
    for match in it :
        pair= (match.span(0))
        matches.append(pair)
    return len(matches)


