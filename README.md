# Bioinformatic Tools<br>
This is a list of bioinformatic tools I wrote during my study in Computational Biology in NUS to apply my understanding of bioinformatic algorithms in a more practical aspect.<br>
The Main.py file can be used to run any of the tools, along with examples that have been included.<br>
The following is the list of algorithms and calculators I wrote, occasionally with steps to aid in education purposes:
  * Global/Local alignment
  * BLOSUM
  * Sum of Pair Scoring for Multiple Sequence Alignment
  * Hidden Markov Model
  * Jukes Cantor Distance
  * Neighbor Joining
  * UPGMA
  
Most of the tools here are used for educational purposes and quite realistic to be used for real world scenarios.<br>
If you spotted errors or have suggestions, feel free to reach out to me here! I do plan to update this as I learn of more algorithms.<br>

***
### Global/Local alignment<br>
Calculates the global/local alignment problem given 2 sequences, an indel penalty, a gap extension penalty and scoring matrix.<br>
The table is calculated and the highest score along with a possible optimal alignment is printed out.<br>
To do:
  * Better graphic output which includes arrows and all the possible optimal alignments

***
### BLOSUM<br>
Showcases how BLOSUM matrices can be calculated given inputs. Workings are shown for educational purposes.<br>

***
### Sum of Pair Scoring for Multiple Sequence Alignment<br>
Given any number of sequences of more than 1, calculates the sum of pair scoring given a scoring matrix and indel penalty. <br>
The bl package allows users to choose a desired scoring matrix.<br>

***
### Hidden Markov Model<br>
Generates a hidden markov model given the states, alphabets emitted from each states, initial, transitions and emission probabilities.<br>
The HMM can then be used to calculate the forward, backwards and viterbi algorithm.<br>
Steps are printed out for educational purposes.<br>
Final result and table is also printed out.<br>

***
### Jukes Cantor Distance<br>
Simply calculates the Jukes Cantor distance given two sequences.<br>

***
### UPGMA<br>
Constructs a rooted tree given leaves/states and their pairwise distance.<br>
Steps are printed out for educational purposes.<br>
Final tree is printed out using Matplotlib.<br>

***
### Neighbor Joining<br>
Constructs an unrooted tree given leaves/states and their pairwise distance.<br>
Steps are printed out for educational purposes.<br>
Final tree is printed out using Matplotlib. However, the tree looks to have a root. Simply remove the root and join the 2 adjacent branches to form an unrooted tree.<br>








