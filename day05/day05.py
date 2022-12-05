print("advent of code 2022 - day 5")


def read_input():
    lines = list()
    with open("input.txt") as file:
        for line in file:
            lines.append(str(line).strip('\n'))
    return lines


def setup_stacks(stacks: list, line: str):
    for i in range(1, 36, 4):
        crate = line[i]
        stack_index = (i - 1) // 4
        if crate != ' ':
            stacks[stack_index][:0] = crate


def move_single_crate(stacks: list, current_stack: int, target_stack: int):
    # note: think about list zero-index vs. 1-index in the instruction
    crate = stacks[current_stack - 1].pop()
    stacks[target_stack - 1].append(crate)


def move_multiple_crates(stacks: list, num_crates: int, current_stack: int, target_stack: int):
    # note: think about list zero-index vs. 1-index in the instruction
    crates = stacks[current_stack - 1][-num_crates:]
    del stacks[current_stack - 1][-num_crates:]
    stacks[target_stack - 1].extend(crates)


def parse_rearrangement(line: str):
    # e.g. "move 2 from 4 to 6"
    line_items = line.split(" ")
    return int(line_items[1]), int(line_items[3]), int(line_items[5])


def get_topmost_crates(stacks: list):
    result = ""
    for stack in stacks:
        result += stack[-1]
    return result


def run_simulation(input: list):
    stacks1 = [[] for _ in range(9)]
    stacks2 = [[] for _ in range(9)]

    in_setup_mode = True
    for line in input:
        if line == "" or line == " 1   2   3   4   5   6   7   8   9 ":
            # on empty line, switch from setup mode to processing mode
            in_setup_mode = False
            # print(f"Stacks 1: {stacks1}")
            # print(f"Stacks 2: {stacks2}")
            continue

        if in_setup_mode:
            # print(f"working on {line}")
            setup_stacks(stacks1, line)
            setup_stacks(stacks2, line)
        else:
            num_crates, current_stack, target_stack = parse_rearrangement(line)
            # print(f"moving {num_crates} crates from stack {current_stack} to stack {target_stack}")

            # individually move crates
            for i in range(num_crates):
                move_single_crate(stacks1, current_stack, target_stack)

            # move crates in batches
            move_multiple_crates(stacks2, num_crates, current_stack, target_stack)

    # result = VPCDMSLWJ
    print(f"part 1: result = {get_topmost_crates(stacks1)}")

    # result = TPWCGNCCG
    print(f"part 2: result = {get_topmost_crates(stacks2)}")


input = read_input()
run_simulation(input)
