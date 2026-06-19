a, s, b = map(str, input().split())

exp = ["+", "-","*", "/"]
a = int(a)
b = int(b)
if s in exp:
    if s == "+":
        print(a + b)
    elif s == "-":
        print(a - b)
    elif s == "*":
        print(a * b)
    elif s == "/":
        print(a // b)

