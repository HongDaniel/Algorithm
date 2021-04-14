        if word[0] != pre_word[-1]:
            print("error1")
            answer.append(turn)
            answer.append(rnd)
            break
        elif word in words[:words.index(word)]:
            print("error2")
            answer.append(turn)
            answer.append(rnd)
            break
        elif len(word) == 1:
            print("error3")
            answer.append(turn)
            answer.append(rnd)
            break