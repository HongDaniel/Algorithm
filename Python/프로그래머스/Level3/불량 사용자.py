from itertools import permutations as P
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]


def check(users, banned_id):
    users = list(users)
    for ban_id in banned_id:
        for user in users:  # ['frodo', 'abc123']
            if len(ban_id) != len(user):
                continue
            flag = True
            for idx in range(len(ban_id)):
                if ban_id[idx] != '*' and ban_id[idx] != user[idx]:
                    flag = False
                    break
            if flag:
                # print(f"ban_id:{ban_id} user:{user}")
                users.remove(user)
                break
    if len(users) == 0:
        return True
    else:
        return False


def solution(user_id, banned_id):
    answer = []
    candis = list(P(user_id, len(banned_id)))
    for users in candis:
        if check(users, banned_id):  # 일치할 경우
            if set(users) not in answer:
                answer.append(set(users))
    print(f"answer:{answer}")
    return len(answer)


solution(user_id, banned_id)
