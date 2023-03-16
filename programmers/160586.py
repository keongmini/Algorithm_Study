def solution(keymap, targets):
    index = {}

    for key in keymap:
        for i in range(len(key)):
            if key[i] not in index:
                index[key[i]] = i + 1
            else:
                index[key[i]] = min(index[key[i]], i + 1)

    result = []
    for target in targets:
        now = 0
        for t in target:
            if t not in index:
                now = -1
                break

            now += index[t]

        result.append(now)

    return result
