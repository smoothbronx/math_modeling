

print(next(map(lambda x: 'частное: ' + str(x[0] // x[1]) + ' (остат' + ('ок: ' + str(x[0] % x[1]) if x[0] % x[1] else 'ка нет') + ')', [(int(input()), int(input()))])))