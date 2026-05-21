# A. Marisa Steals Reimu's Takeout

### Limit
time limit per test: 1 second

memory limit per test: 256 megabytes


### Problem
The Darkness Brought In by Swallowstone Naturalis Historia
— Dateless Bar "Old Adam"
Marisa is a girl of integrity who always helps others safeguard their belongings. Over a period of n
 days, she comes each day to take one of Reimu's takeouts. The i
-th takeout is described by its deliciousness value — an integer wi
 (0≤wi≤2
), forming a sequence w
 of length n
.

Marisa has a special fondness for the number 3
. She can perform the following operation zero or more times:

Select a non-empty subsequence∗
 of w
 whose sum is divisible by 3
, and remove the elements of the subsequence from w
.
Determine the maximum number of operations Marisa can perform.

∗
A sequence a
 is a subsequence of a sequence b
 if a
 can be obtained from b
 by the deletion of several (possibly, zero or all) element from arbitrary positions.

### Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤500
). The description of the test cases follows.

The first line of each test case contains a single integer n
 (1≤n≤100
).

The second line contains n
 integers w1,w2,…,wn
 (0≤wi≤2
), denoting the deliciousness values of the takeouts.

### Output
For each test case, output the maximum number of operations Marisa can perform.
