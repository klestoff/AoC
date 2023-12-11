def read_universe(file_name: str):
    universe = []
    with open(file_name) as f:
        for line in f:
            universe.append(line.rstrip())

    return universe


def expand_universe(u: list[str]) -> tuple[list[int], list[int]]:
    rows, cols = [], []
    i = 0
    while i < len(u):
        if not any(filter(lambda x: x != '.', u[i])):
            rows.append(i)
        i += 1

    i = 0
    while i < len(u[0]):
        if not any(filter(lambda x: x != '.', [u[j][i] for j in range(len(u))])):
            cols.append(i)
        i += 1

    return rows, cols


def print_universe(u: list[str]):
    for line in u:
        print(line)


def get_one_axis_distance(x1: int, x2: int, expansion: list[int], expansion_rate=1) -> int:
    expansion_count = len(list(filter(lambda x: min(x1, x2) < x < max(x1, x2), expansion)))
    return abs(x1 - x2) + expansion_count * expansion_rate - expansion_count


def find_distances(u: list[str], rows: list[int], cols: list[int], expansion_rate: int = 2) -> list:
    planets = []
    for i in range(len(u)):
        start = 0
        while True:
            n = u[i].find('#', start)
            if n >= 0:
                planets.append((n, i))
                start = n + 1
            else:
                break

    return [
        (
                get_one_axis_distance(planets[i][0], planets[j][0], cols, expansion_rate)
                + get_one_axis_distance(planets[i][1], planets[j][1], rows, expansion_rate)
        )
        for i in range(len(planets) - 1) for j in range(i + 1, len(planets))
    ]


universe = read_universe('../11.txt')
print_universe(universe)

rows, cols = expand_universe(universe)

print(sum(find_distances(universe, rows, cols)))
print(sum(find_distances(universe, rows, cols, 1000000)))
