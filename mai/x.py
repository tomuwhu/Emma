n = int(input())
while n != 1:
    print(n, end=" ")
    n = n * 3 + 1 if n % 2 else n // 2
print(n)