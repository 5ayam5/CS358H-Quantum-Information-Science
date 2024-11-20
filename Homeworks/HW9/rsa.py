N = 4668619
e = 3
phi = 4664296
m = 1202997
d = 3109531


def solve_pq():
    temp = N - phi + 1
    sq = int(pow(pow(temp, 2) - 4 * N, 0.5))
    return (temp + sq) // 2, (temp - sq) // 2


def bin_exp(x, n, m):
    res = 1
    while n > 0:
        if n % 2 == 1:
            res = (res * x) % m
        x = (x * x) % m
        n = n // 2
    return res


p, q = solve_pq()
print(p, q)
print(p * q == N)

print(e * d)
print(e * d % phi == 1)

m0 = bin_exp(m, d, N)
print(m0)
print(bin_exp(m0, e, N) == m)

m1 = m0 + 10000
print(bin_exp(m1, e, N))
print(bin_exp(bin_exp(m1, e, N), d, N) == m1)
