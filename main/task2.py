

print(*next(map(lambda x: [x[0] * (x[1] ** i)for i in range(x[2])], [[int(input()) for _ in range(3)]])))