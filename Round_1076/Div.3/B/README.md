# B. Reverse a Permutation

### Limit
time limit per test: 2 seconds

memory limit per test: 256 megabytes

### Problem
A permutation of length n
 is an array consisting of n
 distinct integers from 1
 to n
 in arbitrary order. For example, [2,3,1,5,4]
 is a permutation, but [1,2,2]
 and [1,3,4]
 are not permutations.

You are given a permutation p
 of length n
. You can perform the following operation exactly once:

Choose two integers l,
 r
 (1≤l≤r≤n
).
Reverse the segment [l,r]
 in the permutation p
.
Your task is to output the lexicographically maximum permutation that can be obtained by performing this operation. A permutation a
 is lexicographically greater than a permutation b
 if for the first position i
 where they differ, it holds that ai>bi
.

### Input
Each test consists of several test cases. The first line contains a single integer t
 (1≤t≤104
) — the number of test cases. The description of the test cases follows.

The first line of each test case contains the number n
 (1≤n≤2⋅105
).

The second line of each test case contains n
 distinct integers p1,p2,...,pn
 (1≤pi≤n)
.

It is guaranteed that the sum of the values of n
 across all test cases does not exceed 2⋅105
.

### Output
For each test case, output the lexicographically maximum permutation that can be obtained with one operation.
