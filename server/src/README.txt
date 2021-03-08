symbolicPerseusJavaIR package

This package is an extension of the symbolicPerseusJava package to include Information Rewards, as in the POMDP-IR framework [1]. Extension written by:
Tiago Veiga
Instituto de Sistemas e Robótica
Instituto Superior Técnico
Universidade de Lisboa
Portugal
tsveiga@isr.tecnico.ulisboa.pt

The original symbolicPerseusJava package was written in part by:
Jesse Hoey
School of Computer Science
University of Waterloo
Waterloo, Ontario, Canada
N2L 1Y4
(519)-888-4567x37744
jhoey@cs.uwaterloo.ca

The original symbolicPerseusJava can be found here: https://cs.uwaterloo.ca/~jhoey/research/spudd/index.php

The solver uses the SPUDD format for input models. An example of a patrolling agent with IR actions is with the package.

To use:

1. To compile
> javac *java

2. ensure your CLASSPATH includes ./


3. To show a list of input options :
> java Solver 

4. To solve for a policy using 500 belief points and 2 rounds
> java Solver patrol.dat -g -b 500 -r 2

5. To simulate the policy for 100 rounds manually:
> java Solver patrol.dat -i coffee3po.pomdp -s 100

For larger domains, use the -Xmx and -Xms options to java

[1] Spaan, M. T.; Veiga, T. S.; and Lima, P. U. 2015. Decision-theoretic planning under uncertainty with information rewards for active cooperative perception. Autonomous Agents and Multi-Agent Systems 29(6): 1157–1185. ISSN 15737454. doi:10.1007/s10458-014-9279-8.
