a = 2
temp = bin(a)[2:]
answer = '0'*(5-len(temp))+temp
print(answer)
