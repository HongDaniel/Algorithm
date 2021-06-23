remove = [[0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0]]
a = [1, 2, 3]
print(sum(a))
print(sum(list(sum(el) for el in remove)))
