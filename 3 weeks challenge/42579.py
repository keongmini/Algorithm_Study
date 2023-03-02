from collections import defaultdict

def solution(genres, plays):
    songs = defaultdict(list)

    for i in range(len(genres)):
        songs[genres[i]].append((plays[i], i))

    nums = []
    for song in songs:
        songs[song].sort(key=lambda x: (x[0], -x[1]))

        sumPlay = 0
        for s in songs[song]:
            sumPlay += s[0]
        nums.append((sumPlay, song))

    nums.sort(reverse=True)

    result = []

    for num, genre in nums:
        if len(songs[genre]) > 1:
            for _ in range(2):
                now = songs[genre].pop()
                result.append(now[1])
        else:
            now = songs[genre].pop()
            result.append(now[1])

    return result