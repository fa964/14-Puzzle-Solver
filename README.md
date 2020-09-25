# 14-Puzzle-Solver
This program solves 14 puzzle problems in the shortest amount of moves. It uses A* Graph Search strategy to accomplish this. 
To use this program, create an input text file in the same directory named "board.txt" with the initial board configuration 
and final board configuration in the following format: 

a b c d  
e f g h  
i j k l  
m n o p  

q r s t
u v w x
y z a1 a2
a3 a4 a5 a6

The output will be created in a separate text file in the same directory. 14-puzzle problem: On a 4 x 4 board there are 14 
tiles numbered from 1 to 14 and two blank positions. A tile can slide into any of the two blank positions if it is horizontally
or vertically adjacent to the blank position. Given a start board configuration and a goal board configuration, find a sequence
of moves to reach the goal configuration from the start configuration.
