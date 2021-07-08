play_list = [2, 3, 1, 4]
listen_time = 3


def solution(play_list, listen_time):
    answer = 0
    song = ''
    title = []
    if sum(play_list)-play_list[0]-play_list[-1]+2 <= listen_time:
        print(len(play_list))
        return len(play_list)

    else:
        i = 65
        for el in play_list:
            song += chr(i)*el
            title.append(chr(i))
            i += 1
        song = song*2
        print(song)
        MAX = 0
        for i in range(0, len(song)-listen_time+1):
            cnt = 0
            played = len(set(song[i:i+listen_time]))
            if MAX < played:
                MAX = played
        print(MAX)
        return MAX


solution(play_list, listen_time)
