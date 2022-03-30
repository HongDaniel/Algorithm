n = 4
m = 4
x_axis = [1]
y_axis = [3]


def areaOf(x_left, x_right, y_bottom, y_top):
    return (x_right-x_left)*(y_top-y_bottom)


def solution(n, m, x_axis, y_axis):
    answer = 0
    x_axis.append(n)
    y_axis.append(m)
    x_left, x_right = 0, 0
    candis = []
    for x in x_axis:
        x_right = x
        y_bottom, y_top = 0, 0
        for y in y_axis:
            y_top = y
            candis.append(areaOf(x_left, x_right, y_bottom, y_top))
            y_bottom = y_top
        x_left = x_right
    return max(candis)


solution(n, m, x_axis, y_axis)
