
bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]


def solution1(bridge_lenth, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_lenth
    while bridge:
        answer += 1
        bridge.pop(0)
        if(truck_weights):
            if(sum(bridge)+truck_weights[0] <= weight):
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer


def solution2(bridge_len, weight, trucks):
    answer = 0
    trucks.reverse()
    bridge = {}

    a = 10
    while(trucks or bridge):
        # bridge에 있는 합을 체크
        answer += 1
        bsum = 0
        top = 0
        for key in bridge.keys():
            bridge[key] -= 1

        bridge = dict(
            {key: value for key, value in bridge.items() if value != 0})
        for key in bridge.keys():
            bsum += key

        if(trucks):
            top = trucks.pop()
        if(top):
            if(bsum+top <= weight):
                bridge[top] = bridge_len
            else:
                trucks.append(top)
        a -= 1
        #print(f"{answer}차시- trucks:{trucks} bridge:{bridge} bsum: {bsum}")
    # print(answer)
    return answer


solution(bridge_length, weight, truck_weights)
