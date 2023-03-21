# 실패
def solution(today, terms, privacies):
    result = []

    term = {}
    for t in terms:
        k, m = t.split()
        term[k] = int(m)

    ty, tm, td = map(int, today.split('.'))

    def check(y, m, d):
        if y < ty:
            return False
        elif m < tm:
            return False
        elif d < td:
            return False

        return True

    for i in range(len(privacies)):
        date, k = privacies[i].split()
        y, m, d = map(int, date.split('.'))

        # -------------------------------------
        nm = m + term[k]

        if nm > 12:
            y += (nm // 12)

        m = nm % 12
        if m == 0:
            m = 12

        d -= 1
        if d == 0:
            m -= 1
            d = 28

            if m == 0:
                m = 12

        if not check(y, m, d):
            result.append(i + 1)

    return result


s = solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])
print(s)