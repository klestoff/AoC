with open('../02.txt', 'r') as txt:
    _sum: int = 0
    for line in txt:
        game, shows = line.rstrip().split(': ')

        max_red = max_green = max_blue = 0
        for show in shows.split('; '):
            for cube in show.split(', '):
                count, color = cube.split()
                if color == 'red':
                    if int(count) > max_red:
                        max_red = int(count)
                if color == 'green':
                    if int(count) > max_green:
                        max_green = int(count)
                if color == 'blue':
                    if int(count) > max_blue:
                        max_blue = int(count)

        _sum += max_red * max_green * max_blue

    print(_sum)