from math import log2

def bl_calculate(sequences):

    length = len(sequences[0])
    for seq in sequences[1:]:
        if len(seq) != length:
            print('sequences not same length')
            return 

    pair_count = {}
    total_pairs = 0
    letter_count = {}
    total_letters = 0
    for l in range(length):
        for i in range(len(sequences)):
            for j in range(i+1, len(sequences)):
                i_char = sequences[i][l]
                j_char = sequences[j][l]
                i_j_pair = (i_char + j_char) if i_char < j_char else (j_char + i_char)
                pair_count[i_j_pair] = pair_count.get(i_j_pair, 0) + 1
                total_pairs += 1
                letter_count[i_char] = letter_count.get(i_char, 0) + 1
                letter_count[j_char] = letter_count.get(j_char, 0) + 1
                total_letters += 2

    print('i-j table\n===============')
    for k, v in pair_count.items():
        print(k, v, '/', total_pairs)
    print()

    print('i table\n===============')
    for k, v in letter_count.items():
        print(k, v, '/', total_letters)
    print()

    for k, v in pair_count.items():
        pair_count[k] = v / total_pairs
    for k, v in letter_count.items():
        letter_count[k] = v / total_letters

    print('scores\n===============')
    all_char = sorted(list(letter_count.keys()))
    for i in range(len(all_char)):
        for j in range(i, len(all_char)):
            i_char = all_char[i]
            j_char = all_char[j]
            i_j_pair = (i_char + j_char) if i_char < j_char else (j_char + i_char)
            sij = log2(pair_count[i_j_pair] / ((letter_count[i_char] * letter_count[j_char]) if (i_char == j_char) else (2 * letter_count[i_char] * letter_count[j_char])))
            print(i_j_pair, round(2 * sij, 2))
    