# A. Make it White

### LIMIT
time limit per test: 2 seconds

memory limit per test: 256 megabytes

### PROBLEM
You have a horizontal strip of n
 cells. Each cell is either white or black.

You can choose a continuous segment of cells once and paint them all white. After this action, all the black cells in this segment will become white, and the white ones will remain white.

What is the minimum length of the segment that needs to be painted white in order for all n
 cells to become white?

### Input
The first line of the input contains a single integer t
 (1≤t≤104
) — the number of test cases. The descriptions of the test cases follow.

The first line of each test case contains a single integer n
 (1≤n≤10
) — the length of the strip.

The second line of each test case contains a string s
, consisting of n
 characters, each of which is either 'W' or 'B'. The symbol 'W' denotes a white cell, and 'B' — a black one. It is guaranteed that at least one cell of the given strip is black.

### Output
For each test case, output a single number — the minimum length of a continuous segment of cells that needs to be painted white in order for the entire strip to become white.
