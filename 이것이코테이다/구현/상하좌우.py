n = int(input())
move = list(map(str, input().split()))

x = 0
y = 0

for i in range(len(move)):
    if(move[i] == 'R'):
        if(y < n-1):
            y += 1
        else:
            pass

    elif(move[i] == 'L'):
        if(y > 0):
            y -= 1
        else:
            pass
    elif(move[i] == 'U'):
        if(x > 0):
            x -= 1
        else:
            pass
    elif(move[i] == 'D'):
        if(x < n-1):
            x += 1
        else:
            pass


print(f"x:{x+1} y:{y+1}")
