with open('solved/04.txt', 'r') as lottery_tickets:
    _sum = 0
    for ticket in lottery_tickets:
        card, numbers = ticket.rstrip().split(': ')
        wining_numbers, ticket_numbers = numbers.split(' | ')
        intersection = set(wining_numbers.split()) & set(ticket_numbers.split())
        if len(intersection) > 0:
            _sum += 1 << (len(intersection) - 1)

    print(_sum)