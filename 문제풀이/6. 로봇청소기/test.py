def recur(n):
    if n == 0:
        return
    recur(n - 1)
    print(n)

recur(3)