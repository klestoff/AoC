from operator import itemgetter


def apply_mapping(m: list, s: list):
    if len(m) == 0:
        return

    s.sort()
    m.sort(key=itemgetter(1))
    print(m)

    i, j = 0, 0
    while i < len(s) and j < len(m):
        if s[i][0] + s[i][1] < m[j][1]:
            i += 1
        elif s[i][0] < m[j][1]:
            diff = m[j][1] - s[i][0]
            new_record = [s[i][0], diff]
            s[i][0] += diff
            s[i][1] -= diff
            s.insert(i, new_record)
            i += 1
        elif s[i][0] < m[j][1] + m[j][2]:
            diff = m[j][0] - m[j][1]

            # smaller diapason, need to split range
            local_diff = s[i][0] - m[j][1]
            if s[i][1] > m[j][2] - local_diff:
                new_record = [s[i][0] + m[j][2] - local_diff, s[i][1] - m[j][2] + local_diff]
                s.insert(i+1, new_record)
                s[i][1] = m[j][2] - local_diff

            s[i][0] += diff
            i += 1
        else:
            j += 1

    print(seeds)


with open('solved/05.txt', 'r') as text:
    seeds = []
    line = text.readline()
    if line[:6] == 'seeds:':
        # 1: seeds = list(map(lambda x: int(x), line[7:].split()))
        # Part 2:
        raw_seeds = list(map(lambda x: int(x), line[7:].split()))
        i = 0
        while i < len(raw_seeds):
            # [ start_number, len ]
            seeds.append([raw_seeds[i], raw_seeds[i+1]])
            i += 2

    _map = []
    while line != '':
        line = text.readline()
        if line.rstrip() == '':
            apply_mapping(_map, seeds)
            _map = []
        elif line[-5:] == 'map:\n':
            print(line.rstrip())
        else:
            _map.append(list(map(lambda x: int(x), line.rstrip().split())))

    print(min(seeds))
