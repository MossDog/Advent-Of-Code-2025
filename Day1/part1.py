instructions = [int(line.strip().replace("L", "-").replace("R", "")) for line in open("Day1/input.txt")]

dial_pos = 50
mod = 100
count = 0

for instruction in instructions:
    dial_pos = (dial_pos + instruction) % mod
    if dial_pos == 0:
        count += 1

print(count)