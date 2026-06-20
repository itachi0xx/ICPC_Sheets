def main():
    n = int(input())
    pos, neg, even, odd, zero = 0, 0, 0, 0, 0

    for i in map(int, input().split()):
        if i > 0:
            pos  += 1
        elif i < 0:
            neg += 1


        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    print(f"Even: {even}")
    print(f"odd: {odd}")
    print(f"Positive: {pos}")
    print(f"Negative: {neg}")


main()