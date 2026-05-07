# A. Desorting

### LIMIT
time limit per test: 1 second

memory limit per test: 256 megabytes

### PROBLEM
Call an array a
 of length n
 sorted if a1≤a2≤…≤an−1≤an
.

Ntarsis has an array a
 of length n
.

He is allowed to perform one type of operation on it (zero or more times):

- Choose an index i
 (1≤i≤n−1
).
- Add 1
 to a1,a2,…,ai
.
- Subtract 1
 from ai+1,ai+2,…,an

The values of a
 can be negative after an operation.

Determine the minimum operations needed to make a
 not sorted.

### Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤100
). The description of the test cases follows.

The first line of each test case contains a single integer n
 (2≤n≤500
) — the length of the array a
.

The next line contains n
 integers a1,a2,…,an
 (1≤ai≤109
) — the values of array a
.

It is guaranteed that the sum of n
 across all test cases does not exceed 500
.

### Output
Output the minimum number of operations needed to make the array not sorted.
