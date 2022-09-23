import collections

def solution(id_list, report, k):
    reports = collections.defaultdict(list)
    for r in report:
        f, t = r.split()
        if f not in reports[t]:
            reports[t].append(f)

    result = [0 for _ in range(len(id_list))]
    for r in reports:
        if len(reports[r]) >= k:
            for name in reports[r]:
                result[id_list.index(name)] += 1

    return result
