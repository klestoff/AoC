from collections import Counter

ELEMS = dict((k, v) for v, k in enumerate('23456789TJQKA'))
ELEMS_POWER = len(ELEMS)


def get_hand_power(hand: str) -> int:
    count = dict(Counter(hand))
    hand_type = 0
    if len(count.values()) == 1:
        hand_type = 6  # Five of a kind
    elif len(count.values()) == 2:
        if max(count.values()) == 4:  # Four of a kind
            hand_type = 5
        else:  # Full house
            hand_type = 4
    elif len(count.values()) == 3:
        if max(count.values()) == 3:   # Three of a kind
            hand_type = 3
        else:  # Two pair
            hand_type = 2
    elif len(count.values()) == 4:
        hand_type = 1

    power = 0
    curr_mul = 1
    for i in range(len(hand)):
        power += ELEMS[hand[len(hand) - i - 1]] * curr_mul
        curr_mul *= ELEMS_POWER

    return power + hand_type * curr_mul


with open('07.txt', 'r') as text:
    hands = []
    for line in text:
        _hand, _power = line.rstrip().split()
        hands.append([get_hand_power(_hand), _power, _hand])

    hands.sort()
    print(hands)
    result = sum([int(v[1]) * k for k, v in enumerate(hands, start=1)])

    print(result)