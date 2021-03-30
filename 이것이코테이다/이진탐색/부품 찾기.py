n = input()
item = list(map(int, input().split()))
m = input()
target = list(map(int, input().split()))

for i in range(len(target)):
    if(target[i] in item):
        print("yes", end=' ')
    else:
        print("no", end=' ')
