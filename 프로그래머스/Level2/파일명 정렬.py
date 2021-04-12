import re
files = ["img12.png", "img10.png", "img02.png",
         "img1.png", "IMG01.GIF", "img2.JPG"]


def solution(files):
    answer = []

    new_files = [[]for i in range(len(files))]
    for i in range(len(files)):
        temp = str(files[i])
        head = re.findall(r'^\D+', temp).pop()  # head분리
        temp = temp[len(head):]

        number = re.findall(r'^\d+', temp).pop()
        tail = temp[len(number):]
        new_files[i].append(head)
        new_files[i].append(number)
        new_files[i].append(tail)

    # print(new_files)

    new_files = sorted(new_files, key=lambda x: int(x[1]))  # 번호를 기준으로 정렬
    new_files = sorted(new_files, key=lambda x: x[0].lower())  # head를 기준으로 정렬
    for i in range(len(new_files)):
        new_files[i] = ''.join(new_files[i])
    print(new_files)

    return new_files


solution(files)
