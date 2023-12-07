REDS = 12
GREENS = 13
BLUES = 14

with open('../02.txt', 'r') as txt:
    _sum: int = 0
    for line in txt:
        game, shows = line.rstrip().split(': ')
        n_game = int(game[5:])

        is_possible = True
        for show in shows.split('; '):
            for cube in show.split(', '):
                count, color = cube.split()
                if color == 'red':
                    if int(count) > REDS:
                        is_possible = False
                if color == 'green':
                    if int(count) > GREENS:
                        is_possible = False
                if color == 'blue':
                    if int(count) > BLUES:
                        is_possible = False

        if is_possible: _sum += n_game

    print(_sum)