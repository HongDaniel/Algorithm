modes = []
        maxium = most[0][1]
        if maxium > 1:  # 최소 2명
            for num in most:
                if num[1] == maxium:
                    modes.append(''.join(num[0]))
        for el in modes:
            answer.append(el)