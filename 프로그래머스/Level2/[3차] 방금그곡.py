m = "CCB"
musicinfos = ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]


def solution(m, musicinfos):
    candidates = {}
    for info in musicinfos:
        infos = info.split(',')
        play_hour = int(infos[1][:2])-int(infos[0][:2])
        play_min = int(infos[1][3:5])-int(infos[0][3:5])
        playtime = play_hour*60+play_min

        melody = ''
        if len(infos[3]) >= playtime+infos[3].count('#'):  # 재생시간이 더 짧을 때
            melody = infos[3][:playtime+infos[3].count('#')]

        else:  # 재생시간이 더 길 때
            order = 0
            for i in range(playtime):
                if order+1 == len(infos[3]):
                    next_order = 0
                else:
                    next_order = order+1
                if infos[3][next_order] == '#':
                    melody += infos[3][order]+infos[3][next_order]
                    order += 2
                else:
                    melody += infos[3][order]
                    order += 1
                order = order % len(infos[3])

        melody = melody.replace(m+'#', "")
        if m in melody:
            candidates[infos[2]] = playtime

    if len(candidates) == 0:
        return "(None)"

    else:  # 일치하는 항목이 2개 이상일 경우
        candidates = sorted(candidates.items(),
                            key=lambda x: x[1], reverse=True)
        print candidates[0][0]
        return candidates[0][0]


solution(m, musicinfos)
