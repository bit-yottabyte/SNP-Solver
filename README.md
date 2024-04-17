# SNPSolver

## Overview
SNPSolver is a Python program designed to solve SNP (Single Nucleotide Polymorphism) puzzles of sizes 3x3 or 4x4. The program employs iterative deepening search and iterative deepening A* search algorithms to find the optimal solution path to reach the specified goal state. The heuristic utilized for both searches is the Hamming distance.

## Features
- Solves SNP puzzles of sizes 3x3 and 4x4.
- Implements iterative deepening search algorithm.
- Implements iterative deepening A* search algorithm.
- Provides a comparison of the minimal solution paths produced by both search algorithms.

## How to Use
1. **Clone the Repository**: Clone this repository to your local machine.

2. **Navigate to the Directory**: Move into the directory where you cloned the repository.

3. **Run the Program**: Execute the Python script with the desired input puzzle size (3 or 4) and the initial state of the puzzle.

ex:
3
1 2 3
x 8 6
4 5 7

## Dependencies
- Python 3.0+

## Acknowledgments
- This project was inspired by the concept of SNP puzzles and the application of search algorithms in solving them.
