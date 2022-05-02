n, k = map(int, input().split())
strength = list(map(int, input().split()))
robots = [0]*(2*n)
flag = True
answer = 0


def move_right(arr):
    tmp = arr[-1]
    nar = arr[:-1]
    nar.insert(0, tmp)
    return nar


def stage1(robots, strength):
    strength = move_right(strength)
    robots = move_right(robots)
    if robots[n-1] >= 1:
        robots[n-1] = 0
    return strength, robots


def stage2(robots, strength):
    for i in range(n-2, -1, -1):
        if robots[i+1] == 0 and robots[i] == 1 and strength[i+1] >= 1:
            strength[i+1] -= 1
            robots[i+1] = 1
            robots[i] = 0
    robots[n-1] = 0
    return strength, robots


def stage3(robots, strength):
    if strength[0] > 0:
        robots[0] += 1
        strength[0] -= 1
    return strength, robots


def stage4(robots, strength):
    if strength.count(0) >= k:
        return False
    else:
        return True


while(flag):
    strength, robots = stage1(robots, strength)
    strength, robots = stage2(robots, strength)
    strength, robots = stage3(robots, strength)
    flag = stage4(robots, strength)
    answer += 1
print(answer)
