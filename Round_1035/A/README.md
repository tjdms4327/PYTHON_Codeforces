# A. Add or XOR

### LIMIT
time limit per test: 1 second

memory limit per test: 256 megabytes

### PROBLEM
You are given two non-negative integers a,b
. You can apply two types of operations on a
 any number of times and in any order:

a←a+1
. The cost of this operation is x
;
a←a⊕1
, where ⊕
 denotes the bitwise XOR operation. The cost of this operation is y
.
Now you are asked to make a=b
. If it's possible, output the minimum cost; otherwise, report it.

### Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤104
). The description of the test cases follows.

The only line of each test case contains four integers a,b,x,y
 (1≤a,b≤100,1≤x,y≤107
) — the two integers given to you and the respective costs of two types of operations.

### Output
For each test case, output an integer — the minimum cost to make a=b
, or −1
 if it is impossible.
