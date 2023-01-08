from Table import printTable

def forwardAlgo(seq, states, alphabets, initial_probabilities, transitions, emissions):

    table = []
    for i in range(len(states)):
        tempRow = []
        for j in range(len(seq)):
            current_state = states[i]
            if j == 0:
                print(current_state+':', initial_probabilities[current_state], '*', emissions[current_state][seq[0]])
                tempRow.append(round(initial_probabilities[current_state] * emissions[current_state][seq[0]], 7))
            else:
                tempRow.append(0)
        
        table.append(tempRow)

    printTable(states, list(seq), table, 10)
    print()

    counter = 1
    while counter != len(seq):

        for i in range(len(states)):
            print(i, counter)
            nextState = states[i]
            p = 0
            for j in range(len(states)):
                current_state = states[j]
                print(current_state+'->'+nextState+':', transitions[current_state+nextState],'*', emissions[nextState][seq[counter]], '*', table[j][counter-1])
                p += (transitions[current_state+nextState] * emissions[nextState][seq[counter]] * table[j][counter-1])
            print(p)
            print()
            table[i][counter] = round(p, 7)
        
        printTable(states, list(seq), table, 10)
        print()
        counter += 1

    final_p = 0 
    for i in range(len(states)):
        final_p += table[i][-1]

    print('final probability =', final_p)

def backwardAlgo(seq, states, alphabets, initial_probabilities, transitions, emissions):

    table = []
    for i in range(len(states)):
        tempRow = []
        for j in range(len(seq)):
            if j == len(seq) - 1:
                tempRow.append(1)
            else:
                tempRow.append(0)
        table.append(tempRow)

    counter = len(seq) - 2
    while counter != -1:

        for i in range(len(states)):
            print(i, counter)
            current_state = states[i]
            p = 0
            for j in range(len(states)):
                nextState = states[j]
                print(current_state+'->'+nextState+':', transitions[current_state+nextState],'*', emissions[nextState][seq[counter+1]], '*', table[j][counter+1])
                p += (transitions[current_state+nextState] * emissions[nextState][seq[counter+1]] * table[j][counter+1])
            print(p)
            print()
            table[i][counter] = round(p, 7)
        
        printTable(states, list(seq), table, 10)
        print()
        counter -= 1

    final_p = 0 
    for i in range(len(states)):
        current_state = states[i]
        print(current_state+':', initial_probabilities[current_state], '*', table[i][0])
        final_p += initial_probabilities[current_state] * table[i][0] * emissions[current_state][seq[0]]

    print('final probability =', final_p)

def viterbiAlgo(seq, states, alphabets, initial_probabilities, transitions, emissions):

    table = []
    for i in range(len(states)):
        tempRow = []
        for j in range(len(seq)):
            current_state = states[i]
            if j == 0:
                print(current_state+':', initial_probabilities[current_state], '*', emissions[current_state][seq[0]])
                tempRow.append(round(initial_probabilities[current_state] * emissions[current_state][seq[0]], 7))
            else:
                tempRow.append(0)
        
        table.append(tempRow)

    printTable(states, list(seq), table, 10)
    print()

    graph = {}
    counter = 1
    while counter != len(seq):

        for i in range(len(states)):
            print(i, counter)
            nextState = states[i]
            p = []
            for j in range(len(states)):
                current_state = states[j]
                calc_p = transitions[current_state+nextState] * emissions[nextState][seq[counter]] * table[j][counter-1]
                print(current_state+'->'+nextState+':', transitions[current_state+nextState],'*', emissions[nextState][seq[counter]], '*', table[j][counter-1], '=', calc_p)
                p.append(calc_p)
            print(max(p))
            print()
            graph[(i, counter)] = (p.index(max(p)), counter-1)
            table[i][counter] = round(max(p), 7)
        
        printTable(states, list(seq), table, 10)
        print()
        counter += 1

    highest = (list(map(lambda x: x[-1], table)).index(max(map(lambda x: x[-1], table))), len(seq)-1)
    order = ''
    while True:
        order = states[highest[0]] + order
        highest = graph.get(highest, None)
        if highest == None:
            break
    print('Most probable state sequence:', order, 'with probability', max(map(lambda x: x[-1], table)))
