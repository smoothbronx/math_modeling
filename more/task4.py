

print(next(map(lambda x: x((int(input()), [], x)), [(lambda x: (x[1] + [x[0]] if (x[0] > 1 and all(x[0] % i for i in range(2, x[0]))) else x[2]((lambda m: (x[0] // m, x[1] + [m], x[2]))(next(filter(lambda p: not x[0] % p, range(2, x[0])))))))])))