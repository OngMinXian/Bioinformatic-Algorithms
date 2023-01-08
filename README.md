This is a list of bioinformatic tools I wrote during my study in Computational Biology in NUS to apply my understanding of bioinformatic algorithms in a more practical aspect.
The Main.py file can be used to run any of the tools, along with examples that have been included. 
The following is the list of algorithms and calculators I wrote, occasionally with steps to aid in education purposes:
  * Global/Local alignment
  * BLOSUM
  * Sum of Pair Scoring for Multiple Sequence Alignment
  * Hidden Markov Model
  * Jukes Cantor Distance
  * Neighbor Joining
  * UPGMA
  
Most of the tools here are used for educational purposes and quite realistic to be used for real world scenarios.
If you spotted errors or have suggestions, feel free to reach out to me here! I do plan to update this as I learn of more algorithms.

==Global/Local alignment==
Calculates the global/local alignment problem given 2 sequences, an indel penalty, a gap extension penalty and scoring matrix.
The table is calculated and the highest score along with a possible optimal alignment is printed out.
To do:
  * Better graphic output which includes arrows and all the possible optimal alignments
  
==BLOSUM==
Showcases how BLOSUM matrices can be calculated given inputs. Workings are shown for educational purposes.

==Sum of Pair Scoring for Multiple Sequence Alignment==
Given any number of sequences of more than 1, calculates the sum of pair scoring given a scoring matrix and indel penalty. 
The bl package allows users to choose a desired scoring matrix.

==Hidden Markov Model==
Generates a hidden markov model given the states, alphabets emitted from each states, initial, transitions and emission probabilities.
The HMM can then be used to calculate the forward, backwards and viterbi algorithm.
Steps are printed out for educational purposes.
Final result and table is also printed out.

==Jukes Cantor Distance==
Simply calculates the Jukes Cantor distance given two sequences.

==UPGMA==
Constructs a rooted tree given leaves/states and their pairwise distance.
Steps are printed out for educational purposes.
Final tree is printed out using Matplotlib.

==Neighbor Joining==
Constructs an unrooted tree given leaves/states and their pairwise distance.
Steps are printed out for educational purposes.
Final tree is printed out using Matplotlib. However, the tree looks to have a root. Simply remove the root and join the 2 adjacent branches to form an unrooted tree.








