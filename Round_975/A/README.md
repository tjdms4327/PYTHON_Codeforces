# A. Max Plus Size

### LIMIT
time limit per test: 1 second

memory limit per test: 256 megabytes

### PROBLEM
You are given an array a1,a2,…,an
 of positive integers.

You can color some elements of the array red, but there cannot be two adjacent red elements (i.e., for 1≤i≤n−1
, at least one of ai
 and ai+1
 must not be red).

Your score is the maximum value of a red element plus the number of red elements. Find the maximum score you can get.

### Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤500
). The description of the test cases follows.

The first line of each test case contains a single integer n
 (1≤n≤100
) — the length of the array.

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤1000
) — the given array.

### Output
For each test case, output a single integer: the maximum possible score you can get after coloring some elements red according to the statement.
