def is_number(char: str) -> bool:
    return '0' <= char <= '9'


def find_numbers(line: str, _from: int) -> int:
    if line == '' or _from < 0 or _from >= len(line) or not is_number(line[_from]):
        return 0

    _start = _end = _from
    while _start > 0 and is_number(line[_start - 1]):
        _start -= 1
    while _end < len(line) - 1 and is_number(line[_end + 1]):
        _end += 1

    return int(line[_start:_end+1])


with open('solved/03.txt', 'r') as board:
    _sum = 0

    prv = cur = ''
    nxt = board.readline().rstrip()
    while nxt != '':
        prv = cur
        cur = nxt
        nxt = board.readline().rstrip()

        idx, end = 0, len(cur)
        while idx < end:
            if cur[idx] == '*':
                numbers = []
                for line in [prv, cur, nxt]:
                    temp = find_numbers(line, idx)
                    if temp == 0:
                        numbers.append(find_numbers(line, idx-1))
                        numbers.append(find_numbers(line, idx+1))
                    else:
                        numbers.append(temp)

                numbers = list(filter(lambda x: x != 0, numbers))
                if len(numbers) == 2:
                    _sum += numbers[0] * numbers[1]

            idx += 1

    print(_sum)
