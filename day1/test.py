"""
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
Following these rotations would cause the dial to move as follows:

The dial starts by pointing at 50.
The dial is rotated L68 to point at 82.
The dial is rotated L30 to point at 52.
The dial is rotated R48 to point at 0.
The dial is rotated L5 to point at 95.
The dial is rotated R60 to point at 55.
The dial is rotated L55 to point at 0.
The dial is rotated L1 to point at 99.
The dial is rotated L99 to point at 0.
The dial is rotated R14 to point at 14.
The dial is rotated L82 to point at 32.
Because the dial points at 0 a total of three times during this process, the password in this example is 3.
"""

"""
50
-68 -> -18
-> 82

1. need to % 100 each input
2. if output negative, subtract from 100
3. if output positive, and over 100, subtract 100
4. if output positive and under 100, keep as is

"""

data = None

with open('input.txt', 'r') as f:
  data = [(line[0], int(line[1:])) for line in f.read().strip().split('\n')]

hits = 0
curr = 50

for direction, amount in data:
  amount = amount % 100
  if direction == 'L':
    amount = -amount
  
  curr += amount

  if curr == 0:
    hits += 1
  elif curr < 0:
    # curr is negative so I'm subtracting from 100
    curr = 100 + curr
  elif curr == 100:
    curr = 0
    hits += 1
  elif curr > 100:
    curr -= 100
  
print("Hits:", hits)