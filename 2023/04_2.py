with open('solved/04.txt', 'r') as lottery_tickets:
    cards = [1]
    curr = 1
    for ticket in lottery_tickets:
        if curr not in cards:
            cards.extend([1])
        card, numbers = ticket.rstrip().split(': ')
        wining_numbers, ticket_numbers = numbers.split(' | ')
        intersection = set(wining_numbers.split()) & set(ticket_numbers.split())
        increment = len(intersection)
        if increment > 0:
            extend_array_for = (curr + increment) - len(cards)
            if extend_array_for > 0:
                cards.extend([1] * extend_array_for)

            for i in range(curr, curr + increment):
                cards[i] += cards[curr-1]

        curr += 1

    print(sum(cards[:curr-1]))
