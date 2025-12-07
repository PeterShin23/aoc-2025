"""
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124

if odd not possible
split in middle
if first half == second half
add to total
"""

data = []

with open('input.txt', 'r') as f:
    content = f.read().strip()
    for item in content.split(','):
        start, end = item.split('-')
        data.append((int(start), int(end)))

total = 0
for start, end in data:
    for i in range(start, end + 1):
        s = str(i)
        length = len(s)

        if length % 2 != 0:
            continue

        half = length // 2
        first_half = s[:half]
        second_half = s[half:]

        if first_half == second_half:
            total += int(s)

print(total)