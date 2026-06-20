def main():
    password = 1999

    while True:
        x = int(input())
        if x != password:
            print("worng")
        else:
            print("correct")
            break

main()