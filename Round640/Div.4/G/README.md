# G. Special Permutation

### Limit
time limit per test: 2 seconds

memory limit per test: 256 megabytes

### Problem
A permutation of length n
 is an array p=[p1,p2,…,pn]
, which contains every integer from 1
 to n
 (inclusive) and, moreover, each number appears exactly once. For example, p=[3,1,4,2,5]
 is a permutation of length 5
.

For a given number n
 (n≥2
), find a permutation p
 in which absolute difference (that is, the absolute value of difference) of any two neighboring (adjacent) elements is between 2
 and 4
, inclusive. Formally, find such permutation p
 that 2≤|pi−pi+1|≤4
 for each i
 (1≤i<n
).

Print any such permutation for the given integer n
 or determine that it does not exist.

### Input
The first line contains an integer t
 (1≤t≤100
) — the number of test cases in the input. Then t
 test cases follow.

Each test case is described by a single line containing an integer n
 (2≤n≤1000
).

### Output
Print t
 lines. Print a permutation that meets the given requirements. If there are several such permutations, then print any of them. If no such permutation exists, print -1.
