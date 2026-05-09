# A. XOR Mixup

### LIMIT
time limit per test: 1 second

memory limit per test: 256 megabytes

### PROBLEM
There is an array a
 with n−1
 integers. Let x
 be the bitwise XOR of all elements of the array. The number x
 is added to the end of the array a
 (now it has length n
), and then the elements are shuffled.

You are given the newly formed array a
. What is x
? If there are multiple possible values of x
, you can output any of them.

### Input
The input consists of multiple test cases. The first line contains an integer t
 (1≤t≤1000
) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer n
 (2≤n≤100
) — the number of integers in the resulting array a
.

The second line of each test case contains n
 integers a1,a2,…,an
 (0≤ai≤127
) — the elements of the newly formed array a
.

Additional constraint on the input: the array a
 is made by the process described in the statement; that is, some value of x
 exists.

### Output
For each test case, output a single integer — the value of x
, as described in the statement. If there are multiple possible values of x
, output any of them.
