def main():
    num = int(input())
    rev = 0
    og = num

    while num > 0:
        digit = num % 10 # getting the last digit
        rev = rev * 10 + digit
        num = num // 10 # remove the last digit after getting it (prevent repeats)

    if og == rev:
        print("Yes", og)
    else:
        print("No")
main()