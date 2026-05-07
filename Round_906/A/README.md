# A. Doremy's Paint 3

### LIMIT
time limit per test: 1 second

memory limit per test: 256 megabytes

### PROBLEM
An array b1,b2,…,bn
 of positive integers is good if all the sums of two adjacent elements are equal to the same value. More formally, the array is good if there exists a k
 such that b1+b2=b2+b3=…=bn−1+bn=k
.

Doremy has an array a
 of length n
. Now Doremy can permute its elements (change their order) however she wants. Determine if she can make the array good.

### Input
The input consists of multiple test cases. The first line contains a single integer t
 (1≤t≤100
) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n
 (2≤n≤100
) — the length of the array a
.

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤105
).

There are no constraints on the sum of n
 over all test cases.

### Output
For each test case, print "Yes" (without quotes), if it is possible to make the array good, and "No" (without quotes) otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
