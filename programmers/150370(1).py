def solution(today, terms, privacies):
    today_y, today_m, today_d = map(int, today.split('.'))

    expiration = {}

    for term in terms:
        a, b = term.split()
        expiration[a] = int(b)

    result = []

    for i in range(len(privacies)):
        privacy = privacies[i]
        date, term = privacy.split()
        y, m, d = map(int, date.split('.'))

        new = m + expiration[term]

        if new > 12:
            if new % 12 == 0:
                y += (new // 12) - 1            # 주의! 12로 나눠서 0일 때 - 1
                m = 12
            else:
                y += new // 12
                m = new % 12
        else:
            m = new

        if today_y > y:
            result.append(i + 1)
        elif today_y == y:
            if today_m > m:
                result.append(i + 1)
            elif today_m == m:
                if today_d >= d:        # 같은 일자 처리
                    result.append(i + 1)

    return result

