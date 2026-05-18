# D. Distinct Split

### LIMIT
time limit per test: 2 seconds

memory limit per test: 256 megabytes

### PROBLEM
Let's denote the f(x)
 function for a string x
 as the number of distinct characters that the string contains. For example f(abc)=3
, f(bbbbb)=1
, and f(babacaba)=3
.

Given a string s
, split it into two non-empty strings a
 and b
 such that f(a)+f(b)
 is the maximum possible. In other words, find the maximum possible value of f(a)+f(b)
 such that a+b=s
 (the concatenation of string a
 and string b
 is equal to string s
).

### Input
The input consists of multiple test cases. The first line contains an integer t
 (1≤t≤104
) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer n
 (2≤n≤2⋅105
) — the length of the string s
.

The second line contains the string s
, consisting of lowercase English letters.

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.

### Output
For each test case, output a single integer  — the maximum possible value of f(a)+f(b)
 such that a+b=s
.
