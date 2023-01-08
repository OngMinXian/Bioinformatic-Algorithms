from math import log

def jc_distance(seq1, seq2):

    if (len(seq1) != len(seq2)):
        print("Length of sequences not the same")
    
    columns = len(seq1)
    mismatches = 0
    for i in range(columns):
        mismatches += 1 if seq1[i] != seq2[i] else 0

    d = mismatches/columns

    K = (-3/4) * (log(1 - (4/3) * d))
    V = (d * (1-d)) / (columns * ((1 - (4/3) * d)**2))


    print("Genetic distance is:", K)
    print("Variance of genetic distance is:", V)

    return (K, V)
