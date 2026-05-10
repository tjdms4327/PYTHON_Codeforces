# A. Submission Bait

### LIMIT
time limit per test: 1 second

memory limit per test: 256 megabytes

### PROBLEM
Alice and Bob are playing a game in an array a
 of size n
.

They take turns to do operations, with Alice starting first. The player who can not operate will lose. At first, a variable mx
 is set to 0
.

In one operation, a player can do:

- Choose an index i
 (1≤i≤n
) such that ai≥mx
 and set mx
 to ai
. Then, set ai
 to 0
.

Determine whether Alice has a winning strategy.

### Input
The first line contains an integer t
 (1≤t≤103
) — the number of test cases.

For each test case:

- The first line contains an integer n
 (2≤n≤50
) — the size of the array.
- The second line contains n
 integers a1,a2,…,an
 (1≤ai≤n
) — the elements of the array.

### Output
For each test case, if Alice has a winning strategy, output "YES". Otherwise, output "NO".

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
