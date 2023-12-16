from functools import reduce


def read_sequence(filename: str) -> list[str]:
    with open(filename) as f:
        line = f.readline().rstrip()

        return list(line.split(','))


def seq_sum(seq: str) -> int:
    return reduce(lambda _sum, x: (_sum + x) * 17 % 256, [0] + list(map(ord, seq)))


def fill_the_boxes(seq_list: list[str]) -> list[map]:
    b = [{} for _ in range(256)]
    for seq in seq_list:
        if seq[-1] == '-':
            box_n = seq_sum(seq[:-1])
            if seq[:-1] in b[box_n]:
                del b[box_n][seq[:-1]]
        else:
            symb, count = seq.split('=')
            box_n = seq_sum(symb)
            b[box_n][symb] = int(count)

    return b


start_seq = read_sequence('15.txt')
res = list(map(seq_sum, start_seq))
print(sum(res))

boxes = fill_the_boxes(start_seq)
print(len(boxes), boxes)
_sum = 0
for i in range(len(boxes)):
    kc = 1
    for k in boxes[i].keys():
        _sum += (i + 1) * kc * boxes[i][k]
        kc += 1
print(_sum)