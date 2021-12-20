character = "10 5 2"
monsters = ["Knight 3 10 10 3", "Wizard 5 10 15 1",
            "Beginner 1 1 15 1", "Beginner2 3 10 0 1", "tmp 3 1 15 1"]


def fightReward(character, monster):
    tmp1, tmp2 = character.split(' '), monster.split(' ')
    charHP, charAtt, charSh = int(tmp1[0]), int(tmp1[1]), int(tmp1[2])
    monName, monReward, monHP, monAtt, monSh = tmp2[0], int(
        tmp2[1]), int(tmp2[2]), int(tmp2[3]), int(tmp2[4])
    cnt = 0
    while(1):
        playerDam = charAtt-monSh  # 플레이어 공격
        if playerDam > 0:
            monHP -= playerDam
            cnt += 1
        else:
            return '', 0
        if monHP < 1:
            return monName, monReward/cnt, monReward

        monDam = monAtt-charSh
        if monDam:
            charHP -= monDam  # 몬스터 공격

        if charHP < 1:  # 플레이어 죽음
            return '', 0, 0
        else:
            if monDam:
                charHP += monDam


def solution(character, monsters):
    candi = []
    for i in range(len(monsters)):
        monName, monReward, origin = fightReward(character, monsters[i])
        if monReward:
            candi.append([monName, monReward, origin])

    print(candi)
    candi.sort(key=lambda x: x[1], reverse=True)
    print(candi)
    answer = candi[0][0]
    print(answer)
    return answer


solution(character, monsters)
