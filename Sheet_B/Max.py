def main():
    x = int(input())
    max = 0

    for i in map(int, input().split()):
        if i > max:
            max = i
    print(max)
main()