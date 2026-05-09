# C. Mr. Perfectly Fine

### LIMIT
time limit per test: 2 seconds

memory limit per test: 256 megabytes

### PROBLEM
Victor wants to become "Mr. Perfectly Fine". For that, he needs to acquire a certain set of skills. More precisely, he has 2
 skills he needs to acquire.

Victor has n
 books. Reading book i
 takes him mi
 minutes and will give him some (possibly none) of the required two skills, represented by a binary string of length 2
.

What is the minimum amount of time required so that Victor acquires all of the two skills?

### Input
The input consists of multiple test cases. The first line contains an integer t
 (1≤t≤1000
) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer n
 (1≤n≤2⋅105
) — the number of books available.

Then n
 lines follow. Line i
 contains a positive integer mi
 (1≤mi≤2⋅105
) and a binary string of length 2
, where si1=1
 if reading book i
 acquires Victor skill 1
, and si1=0
 otherwise, and si2=1
 if reading book i
 acquires Victor skill 2
, and si2=0
 otherwise.

It is guaranteed that the sum of n
 over all test cases doesn't exceed 2⋅105
.

### Output
For each test case, output a single integer denoting the minimum amount of minutes required for Victor to obtain both needed skills and −1
 in case it's impossible to obtain the two skills after reading any amount of books.
