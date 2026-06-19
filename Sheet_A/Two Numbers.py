def main():
    x, y = map(int, input("").split())

    print(f"floor {x} / {y} = {x // y}")
    print(f"ceil {x} / {y} = {(x + y - 1) // y}")
    roundvalue = int((x / y) + 0.5)
    print(f"round {x} / {y} = {(roundvalue)}")

main()