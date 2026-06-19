def main():
    name1 = input("").lower().split()
    name2 = input("").lower().split()

    if name1[1] == name2[1]:
        print("brothers")
    else:
        print("not brothers")
main()