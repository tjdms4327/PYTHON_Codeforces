# A. Unit Array

### Limit
time limit per test: 1 second

memory limit per test: 256 megabytes

### Problem
Given an array a
 of length n
, which elements are equal to −1
 and 1
. Let's call the array a
 good if the following conditions are held at the same time:

- a1+a2+…+an≥0
;

- a1⋅a2⋅…⋅an=1
.

In one operation, you can select an arbitrary element of the array ai
 and change its value to the opposite. In other words, if ai=−1
, you can assign the value to ai:=1
, and if ai=1
, then assign the value to ai:=−1
.

Determine the minimum number of operations you need to perform to make the array a
 good. It can be shown that this is always possible.

### Input
Each test consists of multiple test cases. The first line contains a single integer t
 (1≤t≤500
) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n
 (1≤n≤100
) — the length of the array a
.

The second line of each test case contains n
 integers a1,a2,…,an
 (ai=±1
) — the elements of the array a
.

### Output
For each test case, output a single integer — the minimum number of operations that need to be done to make the a
 array good.
