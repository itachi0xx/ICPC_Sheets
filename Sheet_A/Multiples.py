def main():
    a, b = map(int, input("").split())

    if a >= b and  a % b == 0:
        print("Multiples")
    elif a < b and b % a == 0:
        print("Multiples")
    else:
        print("No Multiples")


main()