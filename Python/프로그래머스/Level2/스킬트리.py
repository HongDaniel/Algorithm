import string

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]


def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    skilldic = {}  # 스킬의 순서
    al = list(string.ascii_uppercase)  # 대문자

    for i in range(len(al)):  # 스킬에 인덱스 부여
        if al[i] in skill:
            skilldic[al[i]] = skill.index(al[i])+1
        else:
            skilldic[al[i]] = 0

    for n in range(len(skill_trees)):
        flag = True
        maxn = 0

        for i in range(len(skill_trees[n])):
            if(maxn < skilldic[skill_trees[n][i]]):
                if(skilldic[skill_trees[n][i]] == maxn+1):
                    maxn = skilldic[skill_trees[n][i]]
                else:
                    flag = False

        if(flag):
            answer += 1

    return answer


def solution2(skill, skill_trees):
    answer = 0
    temp = []

    for n in range(len(skill_trees)):
        temp = []
        flag = True

        for i in range(len(skill_trees[n])):
            if skill_trees[n][i] in skill:
                temp.append(skill_trees[n][i])
        print(temp)
        new = "".join(temp)

        for i in range(len(new)):
            if(new[i] != skill[i]):
                flag = False

        if(flag):
            answer += 1
    print(answer)


solution2(skill, skill_trees)
