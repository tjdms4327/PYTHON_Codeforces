# B. Swap and Delete

### LIMIT
time limit per test: 1 second

memory limit per test: 256 megabytes

### PROBLEM
You are given a binary string s
 (a string consisting only of 0-s and 1-s).

You can perform two types of operations on s
:

1. delete one character from s
. This operation costs 1
 coin;
2. swap any pair of characters in s
. This operation is free (costs 0
 coins).

You can perform these operations any number of times and in any order.

Let's name a string you've got after performing operations above as t
. The string t
 is good if for each i
 from 1
 to |t|
 ti≠si
 (|t|
 is the length of the string t
). The empty string is always good. Note that you are comparing the resulting string t
 with the initial string s
.

What is the minimum total cost to make the string t
 good?

### Input
The first line contains a single integer t
 (1≤t≤104
) — the number of test cases. Then t
 test cases follow.

The only line of each test case contains a binary string s
 (1≤|s|≤2⋅105
; si∈{
0, 1}
) — the initial string, consisting of characters 0 and/or 1.

Additional constraint on the input: the total length of all strings s
 doesn't exceed 2⋅105
.

### Output
For each test case, print one integer — the minimum total cost to make string t
 good.
