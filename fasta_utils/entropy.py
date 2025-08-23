import math

from fasta_utils import is_valid


def entropy(sequence) :
    if not is_valid.is_dna(sequence) :
        raise ValueError('Must input a valid DNA sequence')
    sequence = sequence.upper()
    # Calculate the proportion of bases in the sequence
    counts = [
        sequence.count('A'),
        sequence.count('G'),
        sequence.count('T'),
        sequence.count('C'),
    ] 
    seq_length = len(sequence)
    entropy = 0
    for count in counts : 
        if count > 0 : # Avoid log(0) because it is undefined
            p = count / seq_length
            entropy -= p * math.log2(p)
    return entropy
