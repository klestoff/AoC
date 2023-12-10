from math import lcm


def find_path(n: list, seq: str, first_count: int, _from: str, stop_condition) -> (int, str):
    count = first_count
    curr = _from
    while not stop_condition(curr):
        curr = n[curr][0] if (seq[count % len(seq)] == 'L') else n[curr][1]
        count += 1

    return count, curr


with open('../08.txt', 'r') as text:
    sequence = text.readline().rstrip()
    nodes = {}
    for line in text:
        if line.rstrip() == '':
            continue
        node, lr = line.split(' = ')
        nodes[node] = lr.lstrip('(').rstrip(')\n').split(', ')


# Part 1
print(find_path(nodes, sequence, 0, 'AAA', lambda x: x == 'ZZZ')[0])

# Part 2
starts = list(filter(lambda c: c[-1] == 'A', nodes))
numbers = []
for start in starts:
    count, stop_at = find_path(nodes, sequence, 0, start, stop_condition=lambda x: x[-1] == 'Z')
    # start_at = nodes[stop_at][0 if sequence[count % len(sequence)] == 'L' else 1]
    # count2, _ = find_path(nodes, sequence, count + 1, start_at, stop_condition=lambda x: x[-1] == 'Z')
    # print(count, count2 - count)
    numbers.append(count)

print(lcm(*numbers))
