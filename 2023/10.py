OPTIONS = {
    'F': ((1, 0), (0, 1)),
    '-': ((0, -1), (0, 1)),
    '7': ((1, 0), (0, -1)),
    '|': ((-1, 0), (1, 0)),
    'J': ((-1, 0), (0, -1)),
    'L': ((-1, 0), (0, 1)),
}
TOP = 9999


def get_start_symbol(maze: list[str], i: int, j: int) -> str:
    def is_top(sym): return sym == '|' or sym == 'F' or sym == '7'
    def is_bottom(sym): return sym == '|' or sym == 'L' or sym == 'J'
    def is_left(sym): return sym == '-' or sym == 'F' or sym == 'L'
    def is_right(sym): return sym == '-' or sym == '7' or sym == 'J'

    candidates = {
        'F': (is_bottom, is_right),
        '-': (is_left, is_right),
        '7': (is_bottom, is_left),
        '|': (is_top, is_bottom),
        'J': (is_top, is_left),
        'L': (is_top, is_right),
    }

    result = []
    for c in candidates.keys():
        is_suitable = True
        for k in range(len(candidates[c])):
            fun = candidates[c][k]
            n_i = i + OPTIONS[c][k][0]
            n_j = j + OPTIONS[c][k][1]
            is_suitable = is_suitable and 0 <= n_i <= len(maze) and 0 <= n_j <= len(maze[0]) and fun(maze[n_i][n_j])

        if is_suitable:
            result.append(c)

    if len(result) > 1:
        print("More than 1 candidate for start", result)

    return result[0]


def draw_maze(maze: list[str], solution: list[int]):
    graphics = {
        'F': '┌',
        '-': '─',
        '7': '┐',
        '|': '│',
        'J': '┘',
        'L': '└',
        '.': '0',
    }

    n = len(maze[0])
    for i in range(len(maze)):
        for j in range(n):
            print(graphics[maze[i][j] if solution[i * n + j] != TOP else '.'] if solution[i * n + j] >= 0 else '.', end='')
        print("")


def solve(maze: list[str], i: int, j: int) -> list[int]:
    n = len(maze[0])
    solution = [-1] * n * len(maze)

    solution[i * n + j] = 0
    steps = [(1, i + opt[0], j + opt[1]) for opt in OPTIONS[maze[i][j]]]
    while len(steps) > 0:
        step, i, j = steps.pop(0)
        if solution[i * n + j] != -1 and solution[i * n + j] < step:
            continue

        solution[i * n + j] = step
        steps.extend([(step + 1, i + opt[0], j + opt[1]) for opt in OPTIONS[maze[i][j]]])

    return solution


def print_debug_solution(solution: list[int], row_len: int):
    l = 0
    while l < len(solution):
        print('{:3d}'.format(l // row_len), ': ', *['{:6d}'.format(k) for k in solution[l:l + row_len]], sep='')
        l += row_len


def paint_maze_insides(maze: list[str], solution: list[int]):
    n = len(maze[0])

    for i in range(len(maze)):
        walls_count = 0
        j = 0
        while j < n:
            if solution[i * n + j] >= 0:
                walls_count += 1
                match maze[i][j]:
                    case 'F':
                        while j < n-1 and solution[i * n + j + 1] >= 0 and maze[i][j+1] in '-J':
                            j += 1

                    case 'L':
                        while j < n-1 and solution[i * n + j + 1] >= 0 and maze[i][j+1] in '-7':
                            j += 1

            elif walls_count % 2 == 1:
                solution[i * n + j] = TOP

            j += 1


m = []
x, y = 0, 0
with open('10.txt', 'r') as f:
    curr_line = 0
    for line in f:
        line = line.strip()
        pos = line.find('S')
        if pos > -1:
            x = pos
            y = curr_line
        m.append(line)
        curr_line += 1

m[y] = m[y][:x] + get_start_symbol(m, y, x) + m[y][x + 1:]
s = solve(m, y, x)
# draw_maze(m, s)

# Part 1
print('Part 1:', max(s))

# Part 2
paint_maze_insides(m, s)
# print_debug_solution(s, len(m[0]))
# draw_maze(m, s)

print('Part 2:', len(list(filter(lambda c: c == TOP, s))))
