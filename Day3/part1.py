with open("Day3/input.txt") as file:
    banks = [line.strip() for line in file]
    #print(f"{banks=}")
    joltage = 0

    for bank in banks:
        #print(f"{bank=}")
        first = 0
        second = 0

        for i in range(len(bank)):
            curr = int(bank[i])
            if curr > first and i < len(bank) - 1:
                first = curr
                second = 0
            elif curr > second:
                second = curr

        #print(f"{first=}, {second=}")
        joltage += (first * 10) + second

    print(joltage)