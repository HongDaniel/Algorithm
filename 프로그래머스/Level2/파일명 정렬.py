import re
files = ["img12.png", "img10.png", "img02.png",
         "img1.png", "IMG01.GIF", "img2.JPG"]


def solution(files):
    answer = []
    tmp = []
    for idx, file in enumerate(files):  # head, number, tail 나누기
        head = re.split('\d', file).pop(0).lower()
        number = re.findall('\d+', file).pop(0)
        tail = file[len(head)+len(number):]
        number = int(number)
        tmp.append((head, number, tail, idx))

    # 정렬
    tmp.sort(key=lambda x: x[1])
    tmp.sort(key=lambda x: x[0])

    for el in tmp:
        answer.append(files[el[-1]])
    print(answer)
    return answer


solution(files)
