instructions = [int(line.strip().replace("L", "-").replace("R", "")) for line in open("Day1/input.txt")]
dial_pos = 50
count = 0

for instruction in instructions:
    print(f"{instruction=}")
    if instruction < 0:
        div, mod = divmod(instruction, -100)
        count += div
        if dial_pos != 0 and dial_pos + mod <= 0:
            count += 1
    else:
        div, mod = divmod(instruction, 100)
        count += div
        if dial_pos + mod >= 100:
            count += 1

    dial_pos = (dial_pos + instruction) % 100
    if dial_pos == 0:
        count += 1

print(count)