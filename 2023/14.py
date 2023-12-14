from collections import Counter
from hashlib import sha1


def read_puzzle(filename: str):
    with open(filename) as f:
        lines = f.readlines()

    return list(map(lambda s: [*(s.strip())], lines))


def calculate_mass_on_move(dish: list[list[str]]) -> int:
    mass, max_mass = 0, len(dish)
    for j in range(len(dish[0])):
        pos = 0
        for i in range(len(dish)):
            if dish[i][j] == 'O':
                mass += max_mass - pos
                pos += 1
            elif dish[i][j] == '#':
                pos = i + 1

    return mass


def calculate_mass(dish: list[list[str]]) -> int:
    mass, max_mass = 0, len(dish)
    for i in range(max_mass):
        mass += dish[i].count('O') * (max_mass - i)

    return mass


def rotate(dish: list[list[str]], rotation: list[tuple[int, int]] = None):
    if rotation is None:
        rotation = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    for dy, dx in rotation:
        for y in range(len(dish))[::(-1 if dy > 0 else 1)]:
            for x in range(len(dish[0]))[::(-1 if dx > 0 else 1)]:
                if dish[y][x] == 'O':
                    nx, ny = x, y
                    while 0 <= nx + dx < len(dish[0]) and 0 <= ny + dy < len(dish) and dish[ny + dy][nx + dx] == '.':
                        nx, ny = nx + dx, ny + dy

                    if nx != x or ny != y:
                        dish[ny][nx] = 'O'
                        dish[y][x] = '.'


def get_dish_configuration_hash(dish: list[list[str]]) -> str:
    digest = sha1()
    digest.update(''.join([''.join(row) for row in dish]).encode('ascii'))

    return digest.hexdigest()


puzzle = read_puzzle('14.txt')
# Part 1
print(calculate_mass_on_move(puzzle))

# Part 2
# test of rotation
test = puzzle.copy()
rotate(test, [(-1, 0)])
print(calculate_mass(test))

# Looking for a cycle
known_puzzles = {}
sums = []
iteration = 0
period = 0
while period == 0:
    rotate(puzzle)
    sums.append(calculate_mass(puzzle))

    key = get_dish_configuration_hash(puzzle)
    if key in known_puzzles:
        period = iteration - known_puzzles[key]
    else:
        known_puzzles[key] = iteration

    iteration += 1

print(sums[iteration - 1 - period + (1000000000 - iteration) % period])
