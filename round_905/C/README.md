# C. Raspberries

### LIMIT
time limit per test: 2 seconds

memory limit per test: 256 megabytes

### PROBLEM
You are given an array of integers a1,a2,…,an
 and a number k
 (2≤k≤5
). In one operation, you can do the following:

- Choose an index 1≤i≤n
,
- Set ai=ai+1
.

Find the minimum number of operations needed to make the product of all the numbers in the array a1⋅a2⋅…⋅an
 divisible by k
.

### Input
Each test consists of multiple test cases. The first line contains a single integer t
 (1≤t≤104
) — the number of test cases. Then follows the description of the test cases.

The first line of each test case contains two integers n
 and k
 (2≤n≤105
, 2≤k≤5
) — the size of the array a
 and the number k
.

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤10
).

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.

### Output
For each test case, output the minimum number of operations needed to make the product of all the numbers in the array divisible by k
.
