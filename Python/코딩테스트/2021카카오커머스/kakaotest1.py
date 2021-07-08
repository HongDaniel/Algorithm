gift_cards = [5, 4, 5, 4, 5]
wants = [1, 2, 3, 5, 4]


def remove_same(gift_cards, wants):
    temp = []
    for i in range(len(gift_cards)):
        if gift_cards[i] == wants[i]:
            same = gift_cards[i]
            temp.append(same)
    for i in range(len(temp)):
        gift_cards.remove(temp[i])
        wants.remove(temp[i])


def solution(gift_cards, wants):
    remove_same(gift_cards, wants)  # 중복되는 카드 없애기
    if len(gift_cards) == 0:
        return 0
    # print(gift_cards)
    # print(wants)
    for i in range(len(wants)):
        if wants[i] in gift_cards:
            loc = gift_cards.index(wants[i])
            gift_cards[i], gift_cards[loc] = gift_cards[loc], gift_cards[i]

    remove_same(gift_cards, wants)

    return len(gift_cards)


print(solution(gift_cards, wants))
