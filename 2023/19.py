from functools import reduce


def read_instructions(filename: str):
    algo = {}
    parts = []
    with open(filename, 'r') as f:
        line = f.readline().strip()
        while line != '':
            step, instructions = line.rstrip('}').split('{')
            machine = []
            for instruction in instructions.split(','):
                _split = instruction.split(':')
                if len(_split) < 2:
                    machine.append(('_', _split[0]))
                else:
                    machine.append((_split[0][0], _split[0][1], int(_split[0][2:]), _split[1]))

            algo[step] = machine
            line = f.readline().strip()

        for line in f:
            part = {}
            line = line.strip('{}\n').split(',')
            for characteristics in line:
                key, value = characteristics[0], int(characteristics[2:])
                part[key] = value
            parts.append(part)

    return algo, parts


def run_algorithm(algo, parts):
    _sum = 0
    for part in parts:
        state = 'in'
        while state != 'A' and state != 'R':
            for instructions in algo[state]:
                key = instructions[0]
                if key == '_':
                    state = instructions[1]
                elif ((instructions[1] == '<' and part[key] < instructions[2])
                      or (instructions[1] == '>' and part[key] > instructions[2])):
                    state = instructions[3]
                    break

        if state == 'A':
            _sum += sum(part.values())

    return _sum


RANGE_IDX = dict(zip('xmas', range(4)))


def reduce_ranges(ranges: list[tuple[int, int]], instruction: tuple[str, str] | tuple[str, str, int, str]):
    new_ranges = ranges.copy()
    rest_ranges = ranges.copy()

    if instruction[0] != '_':
        range_idx = RANGE_IDX[instruction[0]]
        match instruction[1]:
            case '<':
                new_ranges[range_idx] = (ranges[range_idx][0], instruction[2])
                rest_ranges[range_idx] = (instruction[2], ranges[range_idx][1])
            case '>':
                new_ranges[range_idx] = (instruction[2] + 1, ranges[range_idx][1])
                rest_ranges[range_idx] = (ranges[range_idx][0], instruction[2] + 1)

    return new_ranges, rest_ranges


def find_acceptable_variants(algo):
    _sum = 0
    queue = [('in', [(1, 4001)] * 4)]
    while len(queue) > 0:
        state, ranges = queue.pop(0)
        for instructions in algo[state]:
            reduced_ranges, ranges = reduce_ranges(ranges, instructions)
            if instructions[-1] == 'A':
                _sum += reduce(lambda a, b: a * b, [b - a for a, b in reduced_ranges])
            elif instructions[-1] != 'R':
                queue.append((instructions[-1], reduced_ranges))
        print(state, queue)

    return _sum


state_machine, details = read_instructions('19.txt')
# Part 1
print(run_algorithm(state_machine, details))
# Part 2
print(find_acceptable_variants(state_machine))
