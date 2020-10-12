

print(list(filter(lambda x: x == sum(filter(lambda p: x % p == 0, range(1, x))), range(2, int(input())))))