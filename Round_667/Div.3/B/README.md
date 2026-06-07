# B. Minimum Product

### Limit
time limit per test: 1 second

memory limit per test: 256 megabytes

### Problem
You are given four integers a
, b
, x
 and y
. Initially, a≥x
 and b≥y
. You can do the following operation no more than n
 times:

- Choose either a
 or b
 and decrease it by one. However, as a result of this operation, value of a
 cannot become less than x
, and value of b
 cannot become less than y
.

Your task is to find the minimum possible product of a
 and b
 (a⋅b
) you can achieve by applying the given operation no more than n
 times.

You have to answer t
 independent test cases.

### Input
The first line of the input contains one integer t
 (1≤t≤2⋅104
) — the number of test cases. Then t
 test cases follow.

The only line of the test case contains five integers a
, b
, x
, y
 and n
 (1≤a,b,x,y,n≤109
). Additional constraint on the input: a≥x
 and b≥y
 always holds.

### Output
For each test case, print one integer: the minimum possible product of a
 and b
 (a⋅b
) you can achieve by applying the given operation no more than n
 times.
