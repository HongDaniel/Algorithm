import math

num = int(input())
flag = True
for i in range(2, num):
    if(num % i == 0):
        print("not a prime number")
        flag = False

if(flag):
    print("prime number")
