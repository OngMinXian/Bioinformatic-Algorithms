def sop_calculate(sequences, scoring, indel_penalty):

    length = len(sequences[0])
    for seq in sequences[1:]:
        if len(seq) != length:
            print('sequences not same length')
            return 

    score = 0

    for l in range(length):
        col_score = 0
        equation = ''
        for i in range(len(sequences)):
            for j in range(i+1, len(sequences)):
                i_char = sequences[i][l]
                j_char = sequences[j][l]
                if i_char == '-' and j_char == '-':
                    continue
                elif i_char == '-' or j_char == '-':
                    col_score -= indel_penalty
                    score -= indel_penalty
                    equation += str(-2) + ' '
                    continue 
                i_j_pair = (i_char + j_char) if i_char < j_char else (j_char + i_char)
                col_score += scoring[i_j_pair]
                score += scoring[i_j_pair]
                equation += str(scoring[i_j_pair]) + ' '
        print(f'col {l+1}:', equation + '=',col_score)

    print('score is', score)
