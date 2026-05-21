# C. Secret message

### Limit
time limit per test: 2 seconds

memory limit per test: 256 megabytes

### Problem
Bob, the genius spy, has intercepted an encrypted message. He assumes that it contains secret information and is actively engaged in deciphering it.

The note, which has fallen into the hands of the spy, consists of k
 strips, each of length n
 and containing strict lowercase Latin letters. With extensive experience in deciphering such documents, Bob guessed that the message he is interested in (the deciphering of the note) is also a string of length n
, and the i
-th letter of this message corresponds to the i
-th letter of one of the strips.

According to Bob, the informativity of a string s
 is defined as the minimum positive integer d
 such that a string t
 of length d
 exists, and s
 can be formed by repeating t
 several times. For example, the informativity of the string "aaaa" is 1, the informativity of the string "abab" is 2, and the informativity of the string "abcd" is 4.

Bob assumes that the note's author, to ensure reliable transmission of information, repeated the data in the message several times. Therefore, he believes that a more plausible decryption of the note would have the smallest possible informativity.

Help the spy: find the message that represents the decryption of the note and has the minimum possible informativity.

### Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤104
). The description of the test cases follows.

In the first line of each test case, there are numbers n
 and k
 (2≤n,k≤50000,4≤n⋅k≤105
) — the length of the strips of paper and the number of strips.

In each of the following k
 lines of each test case, there is a sequence of n
 lowercase Latin letters — the next strip.

It is guaranteed that the sum n⋅k
 across all test cases does not exceed 105

### Output
For each test case, output a string of length n
 — the decryption of the note, which has the minimal possible informativity. If there are multiple suitable answers, any of them may be output.
