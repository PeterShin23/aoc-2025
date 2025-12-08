"""
1. find the largest number in the input,
2. second pass from that index to end, find the largest number
3. IF the first pass largest number is at index = length -1, then just find the largest number in the entire list again.
"""


data = None

with open('input.txt', 'r') as f:
  data = f.read().strip().split('\n')

# Part 1
total = 0

for bank in data:
  # First pass
  largest = (-1, -1)
  for i in range(len(bank)-1, -1, -1):
    joltage = int(bank[i])
    if joltage >= largest[1]:
      largest = (i, joltage)
  
  # Second pass
  if largest[0] == len(bank) - 1:
    second = (-1, -1)
    for i in range(len(bank)-2, -1, -1):
      joltage = int(bank[i])
      if joltage >= second[1]:
        second = (i, joltage)
    total += int(str(second[1]) + str(largest[1]))
  else:
    second = (-1, -1)
    for i in range(len(bank)-1, largest[0], -1):
      joltage = int(bank[i])
      if joltage >= second[1]:
        second = (i, joltage)
    total += int(str(largest[1]) + str(second[1]))

print("total:", total)