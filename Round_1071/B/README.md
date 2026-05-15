# B. Blackslex and Showering

### LIMIT
time limit per test: 2 seconds

memory limit per test: 256 megabytes

### PROBLEM
After his IMO medalist friend showered for two hours so that "he doesn't have to shower this again this week," Blackslex will be late for class!

In order to get to class, Blackslex must take the crowded elevator to many floors in a certain order. Because he is a hacker, he can skip visiting up to one floor without the other people knowing. His time taken is the sum of the absolute differences between consecutive floor numbers. Find the minimum time taken, given that he can skip up to one floor.

More formally, given an array a=[a1,a2,…,an]
 of n
 integers, you can choose up to one index k∈{1,2,…,n}
 to erase such that the sum
∑i=1n−2|bi−bi+1|
is minimized, where b=[a1,…,ak−1,ak+1,…,an]
 is the array after erasing element ak
. Report the minimum sum.

### Input
The first line contains one integer t
 (1≤t≤104
) — the number of test cases.

The first line of each test case contains one integer n
 (3≤n≤2⋅105
) — the size of the array.

The second line contains n
 integers a1,a2,…,an
 (1≤ai≤100
).

It is guaranteed that the sum of n
 does not exceed 2⋅105
 over all test cases.

### Output
For each test case, output a single real number — the minimum time taken.
