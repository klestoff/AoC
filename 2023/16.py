def read_contraption(filename: str) -> list[str]:
    with open(filename) as f:
        lines = f.readlines()
        return [line.strip() for line in lines]


contraption = read_contraption('../16.txt')
COLS = len(contraption[0])
ROWS = len(contraption)

UP: tuple[int, int] = (0, -1)
RIGHT: tuple[int, int] = (1, 0)
DOWN: tuple[int, int] = (0, 1)
LEFT: tuple[int, int] = (-1, 0)
POLARITY = {
    UP: 1,
    RIGHT: 2,
    DOWN: 4,
    LEFT: 8
}

SYMBOLS = {
    0: '.',
    POLARITY[UP]: '^',
    POLARITY[RIGHT]: '>',
    POLARITY[DOWN]: 'v',
    POLARITY[LEFT]: '<',
    POLARITY[UP] & POLARITY[DOWN]: '|',
    POLARITY[LEFT] & POLARITY[RIGHT]: '-',
}


REFLECTIONS = {
    '.': {
        UP: UP,
        RIGHT: RIGHT,
        DOWN: DOWN,
        LEFT: LEFT,
    },
    '/': {
        UP: RIGHT,
        RIGHT: UP,
        DOWN: LEFT,
        LEFT: DOWN,
    },
    '\\': {
        UP: LEFT,
        RIGHT: DOWN,
        DOWN: RIGHT,
        LEFT: UP,
    }
}

def find_energy_paths(start_x: int, start_y: int, start_direction: tuple[int, int]) -> list[int]:
    s = [0] * COLS * ROWS
    queue = [(start_x, start_y, start_direction)]
    while len(queue) > 0:
        x, y, direction = queue.pop(0)

        # Out of bounds
        if x < 0 or x >= COLS or y < 0 or y >= ROWS:
            continue

        # we have already been here
        if s[y * COLS + x] & POLARITY[direction] == POLARITY[direction]:
            continue

        s[y * COLS + x] |= POLARITY[direction]
        match contraption[y][x]:
            case '-':
                if direction == LEFT or direction == RIGHT:
                    queue.append((x + direction[0], y + direction[1], direction))
                else:
                    queue.append((x + LEFT[0], y + LEFT[1], LEFT))
                    queue.append((x + RIGHT[0], y + RIGHT[1], RIGHT))

            case '|':
                if direction == UP or direction == DOWN:
                    queue.append((x + direction[0], y + direction[1], direction))
                else:
                    queue.append((x + UP[0], y + UP[1], UP))
                    queue.append((x + DOWN[0], y + DOWN[1], DOWN))

            case _:
                new_dir = REFLECTIONS[contraption[y][x]][direction]
                queue.append((x + new_dir[0], y + new_dir[1], new_dir))

    return s


def energy_sum(s: list[int]) -> int:
    return sum([1 if s[i] > 0 else 0 for i in range(len(s))])


# Part 1
print(energy_sum(find_energy_paths(0, 0, RIGHT)))

# Part 2
sums = []
for i in range(ROWS):
    sums.append(energy_sum(find_energy_paths(0, i, RIGHT)))
    sums.append(energy_sum(find_energy_paths(COLS - 1, i, LEFT)))

for i in range(COLS):
    sums.append(energy_sum(find_energy_paths(i, 0, DOWN)))
    sums.append(energy_sum(find_energy_paths(i, ROWS - 1, UP)))

print(max(sums))

