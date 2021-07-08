tickets = [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]


def solution(tickets):
    tickets.sort(reverse=True)
    routes = {}
    stack = ['ICN']
    answer = []
    for ticket in tickets:
        if ticket[0] not in routes:
            routes[ticket[0]] = []
            routes[ticket[0]].append(ticket[1])
        else:
            routes[ticket[0]].append(ticket[1])

    while stack:
        top = stack[-1]
        if top in routes and routes[top]:
            stack.append(routes[top].pop())
        else:
            answer.append(stack.pop())
    print(answer)
    return answer[::-1]


solution(tickets)
