# A. AI Project Development

### Limit
time limit per test: 2 seconds

memory limit per test: 512 megabytes

### Problem
Maxim and Nikita are working together on a project consisting of n
 lines of code.

Maxim starts working immediately and writes at a speed of x
 lines per hour until the very end.

Nikita has two options:

- not use AI and write from the very beginning at a speed of y
 lines per hour;
- spend z
 hours first setting up an AI agent, writing nothing during that time, and then write at a speed of 10⋅y
 lines per hour.
Nikita makes this choice before work begins and does not change it later.

While Nikita is setting up the AI, he does not write any code at all, but Maxim continues working at the speed of x
 lines per hour.

The project is considered completed as soon as Maxim and Nikita together have written at least n
 lines of code. If the project can be completed before the AI setup ends, then the work ends at that moment.

Time is measured using full hours: if a project is completed in the middle of an hour, this hour is counted fully.

Nikita chooses whether to use AI or not.

Determine the minimum number of full hours after which the project will be completed.

### Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤100
). The description of the test cases follows.

The only line of each test case contains four integers n
, x
, y
, and z
 (1≤n,x,y,z≤10000
) — the number of lines in the project, Maxim's speed, Nikita's speed without AI, and the AI setup time, respectively.

### Output
For each test case, output one integer — the minimum number of full hours after which the project will be completed if Nikita acts optimally.
