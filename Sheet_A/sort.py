def main():
    a, b, c = map(int, input().split())

    oa, ob, oc = a, b, c

    if a > b:
        a, b = b, a

    if a > c:
        a, c = c, a

    if b > c:
        b, c = c, b

    print(a)
    print(b)
    print(c)

    print()

    print(oa)
    print(ob)
    print(oc)

main()