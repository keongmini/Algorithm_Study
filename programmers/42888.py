def solution(record):
    records = [order.split() for order in record]
    members = {}
    for order in records:
        if order[0] == 'Enter' or order[0] == 'Change':
            members[order[1]] = order[2]

    result = []
    for order in records:
        if order[0] == 'Enter':
            result.append(members[order[1]] + "님이 들어왔습니다.")
        if order[0] == 'Leave':
            result.append(members[order[1]] + "님이 나갔습니다.")

    return result