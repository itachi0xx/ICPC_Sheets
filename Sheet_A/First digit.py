num = int(input())
fd = num

while num > 999 and num <= 9999:
    num = num // 1000


if num % 2 == 0:
    print("EVEN")
else:
    print("ODD")