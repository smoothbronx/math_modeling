

print(next(map(lambda x: (('Это равносторонний треугольник' if len(set(x[0])) == 1 else (('Это прямоугольный равнобедренный треугольник' if (x[0][0]**2 + x[0][1]**2 == x[0][2]**2) else 'Это равнобедренный треугольник') if len(set(x[0])) == 2 else ('Это прямоугольный треугольник' if (x[0][0]**2 + x[0][1]**2 == x[0][2]**2) else ('Это остроугольный треугольник' if (x[0][0]**2 + x[0][1]**2 > x[0][2]**2) else 'Это тупоугольный треугольник')))) if x[1] else 'Такого треугольника не существует'), map(lambda x: (x, x[-1] < sum(x[:-1])), [sorted([int(input()) for _ in range(3)])]))))