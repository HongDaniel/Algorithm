import re

p = re.compile("ca.e")

# . : 하나의 문자
# ^ : 문자열의 시작 ex) ^de = desk
# $ : 문자열의 끝 ex) se$ = case

def print_match(m):
    if m:
        print("m.group() : ", m.group())
        print("m.string : ", m.string)
        print("m.start() : ", m.start())
        print("m.end() : ", m.end())
        print("m.span() : ", m.span())
    else :
        print("매치없음\n")
#m= p.search("good care")
#print_match(m)

t = p.findall("care cafe")
print(t)