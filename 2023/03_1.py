def is_symbol(char: str) -> bool:
    return char != '.' and (char < '0' or char > '9')


def is_connected(line: str, _from: int, _to: int) -> bool:
    if line is None or line == '':
        return False

    end = min(_to + 1, len(line))
    idx = max(_from - 1, 0)
    while idx < end:
        if is_symbol(line[idx]):
            return True
        idx += 1

    return False


with open('solved/03.txt', 'r') as board:
    _sum = 0

    prv = cur = None
    nxt = board.readline().rstrip()
    while nxt != '':
        prv = cur
        cur = nxt
        nxt = board.readline().rstrip()

        start = None
        idx, end = 0, len(cur)
        while idx <= end:
            if idx != end and '0' <= cur[idx] <= '9':
                if start is None:
                    start = idx
            elif start is not None:
                if (
                    is_connected(prv, start, idx)
                    or is_connected(nxt, start, idx)
                    or (start > 0 and is_symbol(cur[start-1]))
                    or (idx < end and is_symbol(cur[idx]))
                ):
                    _sum += int(cur[start:idx])
                start = None
            idx += 1

    print(_sum)
