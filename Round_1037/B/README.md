# B. No Casino in the Mountains

### LIMIT
time limit per test: 1 second

memory limit per test: 256 megabytes

### PROBLEM
You are given an array a
 of n
 numbers and a number k
. The value ai
 describes the weather on the i
-th day: if it rains on the i
-th day, then ai=1
; otherwise, if the weather is good on the i
-th day, then ai=0
.

Jean wants to visit as many peaks as possible. One hike to a peak takes exactly k
 days, and during each of these days, the weather must be good (ai=0
). That is, formally, he can start a hike on day i
 only if all aj=0
 for all j
 (i≤j≤i+k−1)
.

After each hike, before starting the next one, Jean must take a break of at least one day, meaning that on the day following a hike, he cannot go on another hike.

Find the maximum number of peaks that Jean can visit.

### Input
Each test consists of several test cases. The first line contains a single integer t
 (1≤t≤104
) — the number of test cases. The description of the test cases follows.

The first line of each test case contains two integers n
 and k
 (1≤n≤105
, 1≤k≤n
).

The second line contains n
 numbers ai
 (ai∈{0,1}
), where ai
 denotes the weather on the i
-th day.

It is guaranteed that the total value of n
 across all test cases does not exceed 105
.

### Output
For each test case, output a single integer: the maximum number of hikes that Jean can make.
