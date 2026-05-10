# A. Gellyfish and Tricolor Pansy

### LIMIT
time limit per test: 1 second

memory limit per test: 256 megabytes

### PROBLEM
Gellyfish and Flower are playing a game called "Duel".

Gellyfish has a
 HP, while Flower has b
 HP.

Each of them has a knight. Gellyfish's knight has c
 HP, while Flower's knight has d
 HP.

They will play a game in rounds until one of the players wins. For k=1,2,…
 in this order, they will perform the following actions:

- If k
 is odd and Gellyfish's knight is alive:
  - Gellyfish's knight can attack Flower and reduce b
 by 1
. If b≤0
, Gellyfish wins. Or,
  - Gellyfish's knight can attack Flower's knight and reduce d
 by 1
. If d≤0
, Flower's knight dies.

- If k
 is even and Flower's knight is alive:
  - Flower's knight can attack Gellyfish and reduce a
 by 1
. If a≤0
, Flower wins. Or,
  - Flower's knight can attack Gellyfish's knight and reduce c
 by 1
. If c≤0
, Gellyfish's knight dies.

As one of the smartest people in the world, you want to tell them who will win before the game. Assume both players play optimally.

It can be proven that the game will never end in a draw. That is, one player has a strategy to end the game in a finite number of moves.

### Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤104
). The description of the test cases follows.

The first and only line of each test case contains four integers a
, b
, c
, d
 (1≤a,b,c,d≤109
) — the HP of Gellyfish, the HP of Flower, the HP of Gellyfish's knight, and the HP of Flower's knight, respectively.

### Output
For each test case, if Flower will win, output "Flower", otherwise output "Gellyfish".
