# B. Different Distances

### Limit
time limit per test: 2 seconds

memory limit per test: 512 megabytes

### Problem
Construct an array of 4⋅n
 integers such that:

- each number 1,2,…,n
 appears in the array exactly 4
 times;
- let px,i
 be the position of the i
-th occurrence of number x
 in the array; then, for each x
 from 1
 to n
, the numbers (px,2−px,1),(px,3−px,2),(px,4−px,3)
 must be pairwise distinct.

For example, for n=3
, one possible array is [1,1,2,1,2,3,1,3,2,2,3,3]
, because: 

- p1,2−p1,1=1,p1,3−p1,2=2,p1,4−p1,3=3
 — all numbers are distinct;
- p2,2−p2,1=2,p2,3−p2,2=4,p2,4−p2,3=1
 — all numbers are distinct;
- p3,2−p3,1=2,p3,3−p3,2=3,p3,4−p3,3=1
 — all numbers are distinct.

### Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤200
). The description of the test cases follows.

The only line of each test case contains one integer n
 (2≤n≤200
).

### Output
For each test case, output the required array. If there are several suitable arrays, output any of them. It can be shown that at least one suitable array always exists under the constraints of the problem.
