def main():

    x = int(input())

    if x < 2:
        print("No")
        return

    for i in range(2, x):
        if x % i == 0:
            print("No")
            return

    print("Yes")


main()