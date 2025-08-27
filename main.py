from fasta_utils import (entropy, is_valid, reverse_complement, search_orf,
                         stats)

sequence_parts = []
with open('./ms2.fasta') as fa:
    for line in fa:
        if not line.startswith('>'):  # skip headers
            sequence_parts.append(line.strip())  # strip removes \n

sequence = "".join(sequence_parts)
if not is_valid.is_valid_sequence(sequence) :
    raise ValueError("Sequence is not valid - DNA or RNA is accepted ")

gc_content = stats.gc_content(sequence)
print(gc_content)

entropy = round(entropy.entropy(sequence), 3)
print(entropy)

orfs = search_orf.search_for_orf(sequence)
print(orfs)

print(reverse_complement.rev_complement_dna(sequence))
