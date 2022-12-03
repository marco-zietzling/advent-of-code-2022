print("advent of code 2022 - day 2")

entries = list()

with open("input.txt") as file:
    for line in file:
        entries.append(str(line).strip())

# part 1
shape_score = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

round_score = {
    'A X': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 6,
    'C Y': 0,
    'C Z': 3,
}


def calculate_shape_score(round: str):
    return shape_score.get(round.split(' ')[1])


def calculate_round_outcome_score(round: str):
    return round_score.get(round)


score = 0
for entry in entries:
    if entry == '':
        break
    score += calculate_round_outcome_score(entry) + calculate_shape_score(entry)

# result = 13809
print(f"part 1: result = {score}")

# part 2
target_round_score = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

# A for Rock, B for Paper, and C for Scissors
# X loose, Y draw, Z win
target_round_shape = {
    'A X': 'C',
    'A Y': 'A',
    'A Z': 'B',
    'B X': 'A',
    'B Y': 'B',
    'B Z': 'C',
    'C X': 'B',
    'C Y': 'C',
    'C Z': 'A',
}

shape_score = {
    'A': 1,
    'B': 2,
    'C': 3
}


def calculate_target_round_outcome_score(round: str):
    return target_round_score.get(round.split(' ')[1])


def calculate_target_round_shape_score(round: str):
    return shape_score.get(target_round_shape.get(round))


score = 0
for entry in entries:
    if entry == '':
        break
    score += calculate_target_round_outcome_score(entry) + calculate_target_round_shape_score(entry)

# result = 12316
print(f"part 2: result = {score}")
