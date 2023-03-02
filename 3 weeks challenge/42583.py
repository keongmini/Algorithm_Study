from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)

    now = sum(bridge)  # 현재 다리에 올라간 트럭들의 무게
    result = 0
    while bridge:
        result += 1
        left = bridge.popleft()
        now -= left

        if truck_weights:
            if now + truck_weights[0] <= weight:
                bridge.append(truck_weights[0])
                now += truck_weights[0]
                truck_weights.popleft()
            else:
                bridge.append(0)
                now += 0

    return result