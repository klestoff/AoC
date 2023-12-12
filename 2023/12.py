from functools import cache


def read_lines(filename: str) -> tuple[str, tuple[int]]:
    with open(filename) as f:
        for condition in f:
            springs, raw_numbers = condition.rstrip().split()
            yield springs, tuple(map(int, raw_numbers.split(',')))


@cache
def count_variants(condition: str, numbers: tuple[int]) -> int:
    if len(numbers) == 0:
        return 1 if all(c != '#' for c in condition) else 0

    if len(condition) < sum(numbers) + len(numbers) - 1:
        return 0

    i = 0
    while i < len(condition) and condition[i] == '.':
        i += 1
    if i > 0:
        return count_variants(condition[i:], numbers)

    count = 0
    if (
        all(c != '.' for c in condition[:numbers[0]])
        and (
            len(condition) == numbers[0]
            or (len(condition) > numbers[0] and condition[numbers[0]] != '#')
        )
    ):
        count += count_variants(condition[numbers[0] + 1:], numbers[1:])

    if condition[0] == '?':
        count += count_variants(condition[1:], numbers)

    return count


# Part 1
total = 0
for broken_condition, calibration_numbers in read_lines('../12.t1'):
    variants = count_variants(broken_condition, calibration_numbers)
    # print(broken_condition, calibration_numbers, variants)
    total += variants

print(total)

# Part 2
total = 0
for broken_condition, calibration_numbers in read_lines('../12.txt'):
    variants = count_variants('?'.join([broken_condition] * 5), calibration_numbers * 5)
    # print(broken_condition, calibration_numbers, variants)
    total += variants

print(total)
