def read_pattern(file_name: str) -> list[str]:
    _pattern = []
    with open(file_name) as file:
        for line in file:
            line = line.rstrip()
            if line != '':
                _pattern.append(line)
            else:
                yield _pattern
                _pattern = []

    if len(_pattern) > 0:
        yield _pattern


def get_candidate_error_count(checked_value: str | list[str], candidate: int, max_errors_count: int) -> int:
    errors = 0

    step = 1
    while candidate - step + 1 >= 0 and candidate + step < len(checked_value) and errors <= max_errors_count:
        if checked_value[candidate - step + 1] != checked_value[candidate + step]:
            for a, b in zip(checked_value[candidate - step + 1], checked_value[candidate + step]):
                errors += 1 if a != b else 0
        step += 1

    return errors


def get_pattern_summary(pattern: list[str], desirable_error_count: int = 0) -> int:
    v_candidates = []
    for candidate in range(len(pattern[0]) - 1):
        errors = 0
        for line in pattern:
            errors += get_candidate_error_count(line, candidate, desirable_error_count)

        if errors == desirable_error_count:
            v_candidates.append(candidate)

    h_candidates = []
    for candidate in range(len(pattern) - 1):
        if get_candidate_error_count(pattern, candidate, desirable_error_count) == desirable_error_count:
            h_candidates.append(candidate)

    return (v_candidates[0] + 1 if len(v_candidates) > 0 else 0) + (
        h_candidates[0] + 1 if len(h_candidates) > 0 else 0) * 100


total1 = 0
total2 = 0
for pattern in read_pattern('../13.txt'):
    total1 += get_pattern_summary(pattern, 0)
    total2 += get_pattern_summary(pattern, 1)

print(total1, total2)
