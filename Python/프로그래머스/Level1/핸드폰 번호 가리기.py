phone_number = "01033334444"


def solution(phone_number):
    return '*' * (len(phone_number)-4) + phone_number[-4:]


solution(phone_number)
