def solution(s):
    nums = list(map(int, s.split(" ")))

    result = ""
    result += str(min(nums))
    result += " "
    result += str(max(nums))

    return result