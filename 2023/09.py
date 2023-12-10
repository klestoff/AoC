def find_next(items: list[int]) -> tuple[int, int]:
    all_items = [items]
    j = 0

    while len(set(all_items[j])) != 1 or all_items[j][-1] != 0:
        new_items = []
        for i in range(len(all_items[j]) - 1):
            new_items.append(all_items[j][i + 1] - all_items[j][i])
        all_items.append(new_items)
        j += 1

    while j > 0:
        all_items[j - 1].append(all_items[j - 1][-1] + all_items[j][-1])
        all_items[j - 1].insert(0, all_items[j - 1][0] - all_items[j][0])
        j -= 1

    return all_items[0][0], all_items[0][-1]


with open('../09.txt') as f:
    lefts = []
    rights = []
    for line in f:
        diffs = list(map(int, line.strip().split()))
        left, right = find_next(diffs)
        lefts.append(left)
        rights.append(right)

    print(sum(lefts), sum(rights))
