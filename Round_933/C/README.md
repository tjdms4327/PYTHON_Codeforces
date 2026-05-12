# C. Rudolf and the Ugly String

### LIMIT
time limit per test: 2 seconds

memory limit per test: 256 megabytes

### PROBLEM
Rudolf has a string s
 of length n
. Rudolf considers the string s
 to be ugly if it contains the substring†
 "pie" or the substring "map", otherwise the string s
 will be considered beautiful.

For example, "ppiee", "mmap", "dfpiefghmap" are ugly strings, while "mathp", "ppiiee" are beautiful strings.

Rudolf wants to shorten the string s
 by removing some characters to make it beautiful.

The main character doesn't like to strain, so he asks you to make the string beautiful by removing the minimum number of characters. He can remove characters from any positions in the string (not just from the beginning or end of the string).

†
 String a
 is a substring of b
 if there exists a consecutive segment of characters in string b
 equal to a
.

### Input
The first line contains a single integer t
 (1≤t≤104
) — the number of test cases. The descriptions of the test cases follow.

The first line of each test case contains a single integer n
 (1≤n≤106
) — the length of the string s
.

The next line of each test case contains the string s
 of length n
. The string s
 consists of lowercase Latin letters.

The sum of n
 over all test cases does not exceed 106
.

### Output
For each test case, output a single integer — the minimum number of characters that need to be deleted to make the string s
 beautiful. If the string is initially beautiful, then output 0
.
