# B. Digit String

### Limit
time limit per test: 2 seconds

memory limit per test: 512 megabytes

### Probelm
You are given a string s
 consisting of digits from 1
 to 4
.

Let's say that the string is beautiful if it is impossible to select some of its elements and write them out (in the same order as they appear in the string) to form a number that is a multiple of 4
. For example, the strings 31, 222, 213 are beautiful, while the strings 143, 3123, 1322 are not. The empty string is considered beautiful.

Your task is to calculate the minimum possible number of elements in the string s
 that need to be removed in order to make it beautiful.

### Input
The first line contains a single integer t
 (1≤t≤104
) — the number of test cases.

The only line of each test case contains a string s
 (1≤|s|≤3⋅105
), consisting of digits from 1
 to 4
.

Additional constraint on the input: the sum of the lengths of s
 over all test cases doesn't exceed 3⋅105
.

### Output
For each test case, print a single integer — the minimum possible number of elements in the string s
 that need to be removed in order to make it beautiful.
