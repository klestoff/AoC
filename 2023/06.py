def find_ways_to_win(time: int, distance: int) -> int:
    left, right = 1, time - 1
    while left < right:
        m = (right + left) // 2
        if (time - m) * m > distance:
            right = m - 1
        else:
            left = m + 1

    if left * (time - left) < distance:
        left += 1

    print(time, left * (time - left), distance)
    return time - 2 * left + 1


file = open('solved/06.txt', 'r')
_, t = file.readline().rstrip().split(': ')
_, d = file.readline().rstrip().split(': ')
file.close()

# Part 1
times = list(map(int, t.split()))
distances = list(map(int, d.split()))

ways_to_win = 1
for i in range(len(times)):
    ways_to_win *= find_ways_to_win(times[i], distances[i])

print(ways_to_win)

# Part 2
times = int(''.join(t.split()))
distances = int(''.join(d.split()))
print(find_ways_to_win(times, distances))
