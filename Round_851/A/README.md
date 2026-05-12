# A. One and Two

### LIMIT
time limit per test: 1 second

memory limit per test: 256 megabytes

### PROBLEM
You are given a sequence a1,a2,…,an
. Each element of a
 is 1
 or 2
.

Find out if an integer k
 exists so that the following conditions are met.

- 1≤k≤n−1
, and
- a1⋅a2⋅…⋅ak=ak+1⋅ak+2⋅…⋅an
.

If there exist multiple k
 that satisfy the given condition, print the smallest.

### Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤100
). Description of the test cases follows.

The first line of each test case contains one integer n
 (2≤n≤1000
).

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤2
).

### Output
For each test case, if there is no such k
, print −1
.

Otherwise, print the smallest possible k
.
