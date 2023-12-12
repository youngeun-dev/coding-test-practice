from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length) 
    truck_weights = deque(truck_weights) 
    current_weight = 0
    
    while truck_weights:
        time += 1
        current_weight -= bridge.popleft() 
        if current_weight + truck_weights[0] <= weight: # 다리 무게 제한 X
            t = truck_weights.popleft()
            bridge.append(t)
            current_weight += t
        else: # 다리 무게 제한 O
            bridge.append(0)
            
    time += bridge_length
    return time
