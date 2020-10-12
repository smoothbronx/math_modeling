


print(next(map(lambda x: (f'корней нет (D = {x[2]}) < 0' if x[2] < 0 else (f'один корень (D = 0); x = {x[0]}' if x[2] == 0 else f'два корня (D = {x[2]}) > 0; x1 = {x[0]}, x2 = {x[1]}')), map(lambda x: ((-x[1] - x[2]**0.5) / (2 * x[0]), (-x[1] + x[2]**0.5) / (2 * x[0]), x[2]), map(lambda x: (*x[:-1], x[1]**2 - 4 * x[0] * x[2]), [[int(input()) for _ in range(3)]])))))