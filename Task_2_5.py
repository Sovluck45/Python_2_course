def letters(l_n=None):
    if l_n is None:
        l_n = 32
    if l_n == 128:
        return
    else:
        print(f"{l_n:2d} - {chr(l_n)}", end=" ")
        if (l_n - 31) % 10 == 0:
            print()
    return letters(l_n + 1)


letters()
