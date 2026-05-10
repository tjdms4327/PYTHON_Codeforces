# C. Game of Mathletes

### LIMIT
time limit per test: 2 seconds

memory limit per test: 256 megabytes

### PROBLEM
Alice and Bob are playing a game. There are n
 (n
 is even) integers written on a blackboard, represented by x1,x2,…,xn
. There is also a given integer k
 and an integer score that is initially 0
. The game lasts for n2
 turns, in which the following events happen sequentially:

- Alice selects an integer from the blackboard and erases it. Let's call Alice's chosen integer a
.
- Bob selects an integer from the blackboard and erases it. Let's call Bob's chosen integer b
.
- If a+b=k
, add 1
 to score.

Alice is playing to minimize the score while Bob is playing to maximize the score. Assuming both players use optimal strategies, what is the score after the game ends?

### Input
The first line contains an integer t
 (1≤t≤104
) — the number of test cases.

The first line of each test case contains two integers n
 and k
 (2≤n≤2⋅105,1≤k≤2⋅n
, n
 is even).

The second line of each test case contains n
 integers x1,x2,…,xn
 (1≤xi≤n
) — the integers on the blackboard.

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.

### Output
For each test case, output the score if both players play optimally.
