from sys import setrecursionlimit

setrecursionlimit(10**6)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def ncr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


def npr(n, r):
    return factorial(n) // factorial(n - r)


def bb_og(n):
    return 1 - (npr(365, n)) / (365**n)


def bb_modified(n):
    return 1 - (364 / 365) ** (n - 1)


d = dict()


def bb_verif(n):
    if n <= 1:
        return 0
    if n in d:
        return d[n]
    d[n] = (364 / 365) ** (n - 2) / 365 + bb_verif(n - 1)
    return d[n]


def binsearch(f, target, low, high):
    while low < high:
        mid = (low + high) // 2
        if f(mid) < target:
            low = mid + 1
        else:
            high = mid
    return int(low)


print(binsearch(bb_og, 0.5, 0, 365))
print(binsearch(bb_og, 0.99, 0, 365))

print(binsearch(bb_modified, 0.5, 0, 1e9))
print(binsearch(bb_modified, 0.99, 0, 1e9))
