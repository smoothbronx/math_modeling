

print("Да" if next(map(lambda x: x % 4 == 0 and (not x % 100 == 0 or x % 400 == 0), [int(input())])) else "Нет")