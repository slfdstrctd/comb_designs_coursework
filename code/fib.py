import itertools
from sympy.polys.domains import ZZ
from sympy.polys.galoistools import (gf_irreducible_p, gf_add, \
                                     gf_sub, gf_mul, gf_rem)
from sympy.ntheory.primetest import isprime


def convert_base(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                '19', '20']
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


class GF:
    def __init__(self, p, n=1):
        p, n = int(p), int(n)
        if not isprime(p):
            raise ValueError("p must be a prime number, not %s" % p)
        if n <= 0:
            raise ValueError("n must be a positive integer, not %s" % n)
        self.p = p
        self.n = n
        if n == 1:
            self.reducing = [1, 0]
        else:
            for c in itertools.product(range(p), repeat=n):
                poly = (1, *c)
                if gf_irreducible_p(poly, p, ZZ):
                    self.reducing = poly
                    break

    def add(self, x, y):
        return gf_add(x, y, self.p, ZZ)

    def sub(self, x, y):
        return gf_sub(x, y, self.p, ZZ)

    def mul(self, x, y):
        return gf_rem(gf_mul(x, y, self.p, ZZ), self.reducing, self.p, ZZ)


def ex(t, x):
    r = 0
    for i in range(len(t)):
        r += t[i] * x ** (len(t) - i - 1)
    return r


def fib(fib1, fib2, n):
    while n > 0:
        fib1, fib2 = fib2, F.add(F.mul(alpha, fib1), fib2)  # alpha * fib1 + fib2
        n -= 1
    return fib1


print('n:')
n = int(input())
print('p:')
p = int(input())
print('r:')
r = int(input())
q = p ** r

F = GF(p, r)

k = 0
t = 1
alpha = 0
x0 = 0
x1 = 1

max_ind = -1
max_alp = -1

while t < q:
    alpha = x = [int(i_) for i_ in str(convert_base(t, int(p)).zfill(n + 1))]
    x = [int(i_) for i_ in str(convert_base(x0, int(p)).zfill(n + 1))]
    y = [int(i_) for i_ in str(convert_base(x1, int(p)).zfill(n + 1))]

    k = 0
    vect = []
    vect.append(x0)
    vect.append(x1)
    while k < q ** 2 + 3:
        vect.append(ex(fib(x, y, k + 2), p))
        k += 1

    vect.pop(0)
    vect.pop(0)
    str_ = ','.join(str(x) for x in vect)

    ve = [x0, x1, vect[0], vect[1]]
    se = ','.join(str(x) for x in ve)

    ind = str_.find(se)

    if ind > max_ind:
        max_ind = ind
        max_alp = t
    t += 1

print('alpha is', max_alp)