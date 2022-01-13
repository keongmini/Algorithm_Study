# bridge_length : 한칸이라고 생각하면 됨
def solution(bridge_length, weight, truck_weights):
    bridge = [0 for i in range(bridge_length)]
    cnt = 0

    while bridge:
        cnt += 1
        bridge.pop(0)

        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights[0])
                truck_weights.pop(0)
            else:
                bridge.append(0)

    return cnt

