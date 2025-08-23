def g_content(sequence) :
    sequence = sequence.upper()
    counter = 0
    for base in sequence :
        if (base == 'G') :
            counter += 1
    G_content = round((counter / len(sequence)) * 100, 3)
    return G_content

def c_content(sequence) :
    sequence = sequence.upper()
    counter = 0
    for base in sequence :
        if (base == 'C') :
            counter += 1
    C_content = round((counter / len(sequence)) * 100, 3)
    return C_content


def t_content(sequence) :
    sequence = sequence.upper()
    counter = 0
    for base in sequence :
        if (base == 'T') :
            counter += 1
    T_content = round((counter / len(sequence)) * 100, 3)
    return T_content



def a_content(sequence) :
    sequence = sequence.upper()
    counter = 0
    for base in sequence :
        if (base == 'A') :
            counter += 1
    A_content = round((counter / len(sequence)) * 100, 3)
    return A_content


def n_content(sequence) :
    sequence = sequence.upper()
    counter = 0
    for base in sequence :
        if (base == 'N') :
            counter += 1
    N_content = round((counter / len(sequence)) * 100, 3)
    return N_content


def gc_content(sequence) :
    GC_content = g_content(sequence) + c_content(sequence) 
    return GC_content

def at_content(sequence) :
    AT_content = round(100 - (gc_content(sequence) + n_content(sequence)), 3) 
    return AT_content

def AT_GC_ratio(sequence) :
    ratio = round(at_content(sequence) / gc_content(sequence), 2) 
    return ratio

def seq_length(sequence) :
    return len(sequence)

