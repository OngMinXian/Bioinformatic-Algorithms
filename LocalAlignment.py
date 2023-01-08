def LocalAlign(seq1, seq2, scoring, indel_penalty, gap_extension, *toPrint):

    graph = {}

    if toPrint != ():
        toPrint = toPrint[0]
    else:
        toPrint = False

    dp = [] 
    for i in range(len(seq2)+1):
        tempRow = []
        for j in range(len(seq1)+1):
            if i == 0 or j == 0:    
                tempRow.append(0)
            else:
                tempRow.append(-1)
        dp.append(tempRow)

    highest = 0
    position_of_highest = (0, 0)

    for i in range(1, len(seq2)+1):
        for j in range(1, len(seq1)+1):
            topLeft = scoring[seq1[j-1] + seq2[i-1]]
            if graph.get((0, j-1)) == (0, j-2):
                left = -gap_extension
            else:
                left = -indel_penalty
            if graph.get((i-1, 0)) == (i-2, 0):
                left = -gap_extension
            else:
                top = -indel_penalty
            nextScore = max(0, dp[i-1][j-1] + topLeft, dp[i][j-1] + left, dp[i-1][j] + top)
            if nextScore == dp[i-1][j-1] + topLeft:
                graph[(i, j)] = (i-1, j-1)
            if nextScore == dp[i][j-1] + left:
                graph[(i, j)] = (i, j-1)
            if nextScore == dp[i-1][j] + top:
                graph[(i, j)] = (i-1, j)
            if nextScore > highest:
                highest = nextScore
                position_of_highest = (i, j)
            dp[i][j] = nextScore

    topStr = "      "
    for i in seq1:
        topStr += "    " + i
    print(topStr) if toPrint else 1
    print() if toPrint else 1

    count = -1
    for i in dp:
        tempString = ""
        if count != -1:
            tempString += seq2[count]
        else:
            tempString += " "
        count += 1
        for j in i:
            tempString += " " * (5 - len(str(j)))
            tempString += str(j)
        print(tempString) if toPrint else 1
        print() if toPrint else 1

    print(f"highest local alignment score {highest} at {position_of_highest}") if toPrint else 1

    current = position_of_highest
    prev = None
    seq1Aligned = ''
    seq2Aligned = ''
    while True:
        if prev != None:
            ic, jc = current
            ip, jp = prev
            if ic == ip:
                seq1Aligned = seq1[jc] + seq1Aligned
                seq2Aligned = '-' + seq2Aligned
            elif jc == jp:
                seq1Aligned = '-' + seq1Aligned
                seq2Aligned = seq2[ic] + seq2Aligned
            else:
                seq1Aligned = seq1[jc] + seq1Aligned
                seq2Aligned = seq2[ic] + seq2Aligned
        current, prev = graph.get(current), current
        if current == None:
            break

    print(seq1Aligned + '\n' + seq2Aligned) if toPrint else 1
    print()
    
    return (highest, seq1Aligned, seq2Aligned)
