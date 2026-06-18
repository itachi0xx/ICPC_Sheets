def main():
    x, y=  input("Enter X, and Y: ").split()
    x = int(x)
    y = int(y)

    print(f"{x} + {y} = {x + y}")
    print(f"{x} * {y} = {x * y}")
    print(f"{x} - {y} = {x - y}")

main()