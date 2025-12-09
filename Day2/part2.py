def is_invalid_id(id_str):
    length = len(id_str)

    if length < 2:
        return False

    for pattern_length in range(1, (length//2) + 1):
        div, mod = divmod(length, pattern_length)
        if mod != 0:
            continue

        pattern = id_str[:pattern_length]
        if pattern * div == id_str:
            return True
    return False



with open("Day2/input.txt") as file:
    ranges = [id.split("-") for id in file.read().split(",")]
    count = 0
    for start, stop in ranges:
        for num in range(int(start), int(stop)+1):
            #print(num)
            if is_invalid_id(str(num)):
                count += num

    print(f"{count=}")