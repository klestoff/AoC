from operator import itemgetter

def apply_mapping(m: list, s: list):
    if len(m) == 0:
        return

    s.sort()
    m.sort(key=itemgetter(1))
    print(m)

    i, j = 0, 0
    while i < len(s) and j < len(m):
        if s[i] < m[j][1]:
            i += 1
        elif s[i] < m[j][1] + m[j][2]:
            s[i] += m[j][0] - m[j][1]
            i += 1
        else:
            j += 1

    print(seeds)


with open('solved/05.txt', 'r') as text:
    seeds = []
    line = text.readline()
    if line[:6] == 'seeds:':
        seeds = list(map(lambda x: int(x), line[7:].split()))

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
