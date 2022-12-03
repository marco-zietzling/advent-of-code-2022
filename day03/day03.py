print("advent of code 2022 - day 3")

entries = list()

with open("input.txt") as file:
    for line in file:
        entries.append(str(line).strip())


def calculate_item_priority(item: chr):
    if item.isupper():
        return ord(item) - ord('A') + 27
    elif item.islower():
        return ord(item) - ord('a') + 1
    else:
        raise Exception(f"Unknown item {item}")


sum = 0
for entry in entries:
    split_position = len(entry) // 2
    compartment1 = entry[:split_position]
    compartment2 = entry[split_position:]
    common_item = next(iter(set(compartment1).intersection(compartment2)))
    sum += calculate_item_priority(common_item)

    # print(f"{entry} to be split at position {split_position}")
    # print(f"{compartment1} -- {compartment2}")
    # print(f"item in both compartments: {common_item}")
    # print(f"priority of common item: {calculate_item_priority(common_item)}")

# result = 7766
print(f"part 1: result = {sum}")

sum = 0
i = 0
while i < len(entries) - 2:
    rucksack1 = entries[i]
    rucksack2 = entries[i + 1]
    rucksack3 = entries[i + 2]
    common_item = next(iter(set(rucksack1).intersection(rucksack2).intersection(rucksack3)))
    sum += calculate_item_priority(common_item)
    i += 3

# result = 2415
print(f"part 2: result = {sum}")
