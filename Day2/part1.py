def is_invalid_id(id_str):
    length = len(id_str)

    if length % 2 == 1:
        return False
            
    mid = length//2

    return id_str[:mid] == id_str[mid:]


with open("Day2/input.txt") as file:
    ranges = [id.split("-") for id in file.read().split(",")]
    count = 0
    for start, stop in ranges:
        for num in range(int(start), int(stop)+1):
            #print(num)
            if is_invalid_id(str(num)):
                count += num

    print(f"{count=}")