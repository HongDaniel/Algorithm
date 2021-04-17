    print(edge)
        el1 = edge[0]
        el2 = edge[1]

        if level[el1] <= level[el2]:
            a[el2] += a[el1]
            a[el1] = 0
        else:
            a[el1] += a[el2]
            a[el2] = 0