# B. Ten Words of Wisdom

### LIMIT
time limit per test: 1 second

memory limit per test: 256 megabytes

### PROBLEM
In the game show "Ten Words of Wisdom", there are n
 participants numbered from 1
 to n
, each of whom submits one response. The i
-th response is ai
 words long and has quality bi
. No two responses have the same quality, and at least one response has length at most 10
.

The winner of the show is the response which has the highest quality out of all responses that are not longer than 10
 words. Which response is the winner?

### Input
The first line contains a single integer t
 (1≤t≤100
) — the number of test cases.

The first line of each test case contains a single integer n
 (1≤n≤50
) — the number of responses.

Then n
 lines follow, the i
-th of which contains two integers ai
 and bi
 (1≤ai,bi≤50
) — the number of words and the quality of the i
-th response, respectively.

Additional constraints on the input: in each test case, at least one value of i
 satisfies ai≤10
, and all values of bi
 are distinct.

### Output
For each test case, output a single line containing one integer x
 (1≤x≤n
) — the winner of the show, according to the rules given in the statement.

It can be shown that, according to the constraints in the statement, exactly one winner exists for each test case.
