import math
import cmath
import matplotlib.pyplot as plt


def solve(k, Q=32, q_minus_1=6):
    omega = cmath.exp(2j * cmath.pi / Q)
    s = 0
    for i in range(Q // q_minus_1 + 1):
        s += omega ** (q_minus_1 * i * k)
    s /= cmath.sqrt((Q // q_minus_1 + 1) * Q)
    return abs(s) ** 2


def probs_plot(Q, q):
    print(sum([solve(k, Q, q - 1) for k in range(Q)]))
    plt.plot([solve(k, Q, q - 1) for k in range(Q)])
    plt.show()


def ques_1a():
    probs_plot(32, 7)
    probs_plot(512, 7)


def has_residue_one(x, N):
    for i in range(1, N):
        if x**i % N == 1:
            return True
    return False


def periods(q):
    ret = []
    for i in range(2, 2 * q + 1):
        if math.gcd(i, 2 * q) == 1:
            print(i, 2 * q)
            ret.append(has_residue_one(i, 2 * q))
    return ret
