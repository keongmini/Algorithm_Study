from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    result = 0
    field = [[-1] * 102 for _ in range(102)]