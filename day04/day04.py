print("advent of code 2022 - day 4")

entries = list()

with open("input.txt") as file:
    for line in file:
        entries.append(str(line).strip())

sum_contained_ranges = 0
sum_overlapping_ranges = 0
for entry in entries:
    range1, range2 = entry.split(',')
    [range1_lower, range1_upper] = [int(x) for x in range1.split('-')]
    [range2_lower, range2_upper] = [int(x) for x in range2.split('-')]

    # print(f"range1: {range1} // range2: {range2}")
    # print(f"range1 lower: {range1_lower} upper: {range1_upper}")
    # print(f"range2 lower: {range2_lower} upper: {range2_upper}")

    range1_set = set(range(range1_lower, range1_upper + 1))
    range2_set = set(range(range2_lower, range2_upper + 1))

    # print(f"range1: {range1_set} and range2: {range2_set}")

    if (range1_set.issubset(range2_set)) or (range2_set.issubset(range1_set)):
        sum_contained_ranges += 1
        # print(f"contained range: {range1} and {range2}")

    if not range1_set.isdisjoint(range2_set) or not range2_set.isdisjoint(range1_set):
        sum_overlapping_ranges += 1
        # print(f"overlapping range: {range1} and {range2}")

# result = 413
print(f"part 1: result = {sum_contained_ranges}")

# result = 806
print(f"part 2: result = {sum_overlapping_ranges}")
