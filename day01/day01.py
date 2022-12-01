print("advent of code 2022 - day 1")

entries = list()

with open("input.txt") as file:
    for line in file:
        entries.append(str(line).strip())

# part 1 & 2
calories = 0
calories_per_elves = [int()]

for entry in entries:
    if entry == "":
        calories_per_elves.append(calories)
        calories = 0
    else:
        calories += int(entry)

calories_per_elves.sort(reverse=True)

# result = 74394
print(f"part 1: result = {calories_per_elves[0]}")

# result = 212836
print(f"part 2: result = {calories_per_elves[0] + calories_per_elves[1] + calories_per_elves[2]}")
