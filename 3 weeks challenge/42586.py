from collections import deque


def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)

    time = 0
    cnt = 0

    result = []
    while progresses:
        progress = progresses[0]
        speed = speeds[0]

        now = progress + (time * speed)

        if now >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        else:
            time += 1
            if cnt > 0:
                result.append(cnt)
                cnt = 0

    result.append(cnt)
    return result

