def main():
    # solution # 1:
    a, b, c = map(int, input("").split())
    min = b ; max = b

    if a > max:
        max = a
    if c > max:
        max = c

    if a < min:
        min = a
    if c < min:
        min = c

    print(min, max, sep = " ")


    # solution # 2:

    num = list(map(int, input().split()))
    num.sort()
    print(num[0], num[-1], sep=" ")

main()