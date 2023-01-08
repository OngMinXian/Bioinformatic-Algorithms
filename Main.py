import blosum as bl

from GlobalAlignment import GlobalAlign
from LocalAlignment import LocalAlign
from BLOSUM import bl_calculate
from SumOfPairScoringMSA import sop_calculate
from HMM import forwardAlgo, backwardAlgo, viterbiAlgo
from JukesCantorDistance import jc_distance
from UPGMA import upgma
from NeighborJoining import neighborJoining

########################################################################################################
# Global alignment
########################################################################################################

#seq1 is top sequence, seq2 is left sequence
g_seq1 = "ATTTGTTACCGGT"
g_seq2 = "ATTGGCCTTAGCCT"

g_indel_penalty = 2
g_gap_extension = 2

g_scoring = {
"AA": 2, "AT": -1, "AG": -1, "AC": -1,
"TA": -1, "TT": 2, "TG": -1, "TC": -1,
"GA": -1, "GT": -1, "GG": 2, "GC": -1,
"CA": -1, "CT": -1, "CG": -1, "CC": 2,
}

# scoring = bl.BLOSUM(62, default=float('-inf'))

###################################### Run the following function ######################################
# GlobalAlign(g_seq1, g_seq2, g_scoring, g_indel_penalty, g_gap_extension, True)

########################################################################################################
# Local alignment
########################################################################################################

#seq1 is top sequence, seq2 is left sequence
l_seq1 = "ATTTGTTACCGGT"
l_seq2 = "ATTGGCCTTAGCCT"

l_indel_penalty = 2
l_gap_extension = 2

l_scoring = {
"AA": 2, "AT": -1, "AG": -1, "AC": -1,
"TA": -1, "TT": 2, "TG": -1, "TC": -1,
"GA": -1, "GT": -1, "GG": 2, "GC": -1,
"CA": -1, "CT": -1, "CG": -1, "CC": 2,
}

# scoring = bl.BLOSUM(62, default=float('-inf'))

###################################### Run the following function ######################################
# LocalAlign(l_seq1, l_seq2, l_scoring, l_indel_penalty, l_gap_extension, True)

########################################################################################################
# BLOSUM
########################################################################################################

bl_sequences = [
'BABA',
'AACA',
'AACC',    
'AABA',
'AABC',
'AABB',
]

###################################### Run the following function ######################################
# bl_calculate(bl_sequences)

########################################################################################################
# Sum of Pair Scoring for MSA
########################################################################################################

sequences = [
'---FGFLKG',
'FPHF-HLS-',
'DPHFGHLS-',    
'FDDFKHLK-',
]

scoring = bl.BLOSUM(62, default=float('-inf'))

indel_penalty = 2

###################################### Run the following function ######################################
# sop_calculate(sequences, scoring, indel_penalty)

########################################################################################################
# Hidden Markov Model
########################################################################################################

states = ['1', '2', '3']
alphabets = ['a', 't', 'c', 'g']

initial_probabilities = {
'1': 0.4,
'2': 0.2,
'3': 0.4,
}

transitions = {
'11': 0.3, '12': 0.2, '13': 0.5,
'21': 0.5, '22': 0.2, '23': 0.3,
'31': 0.4, '32': 0.2, '33': 0.4,
}

emissions = {
'1': {'a': 0.2, 't': 0.4, 'c': 0.2, 'g': 0.2},
'2': {'a': 0.2, 't': 0.4, 'c': 0.0, 'g': 0.4},
'3': {'a': 0.2, 't': 0.1, 'c': 0.3, 'g': 0.4},
}

###################################### Run the following function ######################################
# forwardAlgo('acgt', states, alphabets, initial_probabilities, transitions, emissions)
# backwardAlgo('acgt', states, alphabets, initial_probabilities, transitions, emissions)
# viterbiAlgo('atct', states, alphabets, initial_probabilities, transitions, emissions)

########################################################################################################
# Jukes-Cantor Distance
########################################################################################################

seq1 = "ATAT"
seq2 = "AGAA"

###################################### Run the following function ######################################
# jc_distance(seq1, seq2)

########################################################################################################
# UPGMA
########################################################################################################

upgma_leaves = ['A', 'B', 'C', 'D', 'E']
upgma_pairwise_dist = [
[0,7,8,7,12],
[7,0,3,5,7],
[8,3,0,5,7],
[7,5,5,0,3],
[12,7,7,3,0],
]

###################################### Run the following function ######################################
# upgma(upgma_leaves, upgma_pairwise_dist)

########################################################################################################
# Neighbor Joining
########################################################################################################

nj_leaves = ['A', 'B', 'C', 'D', 'E']
nj_pairwise_dist = [
[0,7,8,7,12],
[7,0,3,5,7],
[8,3,0,5,7],
[7,5,5,0,3],
[12,7,7,3,0],
]

###################################### Run the following function ######################################
# neighborJoining(nj_leaves, nj_pairwise_dist)
