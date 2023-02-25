def solution(participant, completion):
    participant.sort()
    completion.sort()

    idx = 0

    result = participant[-1]

    while idx < len(completion):
        if participant[idx] != completion[idx]:
            result = participant[idx]
            break

        idx += 1

    return result