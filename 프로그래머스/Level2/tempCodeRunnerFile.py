    ar1, ar2, ar3, ar4 = divide(arr)
        tmp = [ar1, ar2, ar3, ar4]
        for i in range(4):
            if check(tmp[i]):
                nums.append(tmp[i][0][0])
            else:
                recursive(tmp[i])