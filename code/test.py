import itertools
# from functools import reduce
# from sympy import symbols, Dummy
from sympy.polys.domains import ZZ
from sympy.polys.galoistools import (gf_irreducible_p, gf_add, \
                                     gf_sub, gf_mul, gf_rem, gf_gcdex, gf_div, gf_gcdex, gf_quo, gf_exquo)
from sympy.ntheory.primetest import isprime


# from sympy.polys.domains.domain import
def isNull(vec):
    for i, it__ in enumerate(vec):
        if it__ != 0:
            return False
    return True


def deNull(vec):
    i = 0
    le = len(vec)
    while i < le - 1:
        if vec[0] == 0:
            vec.pop(0)
        else:
            return vec
        i += 1
    return vec


alphas = {
    2: 1,
    3: 1,
    4: 2,
    5: 3,
    7: 4,
    8: 3,
    9: 4,
    11: 3,
    13: 3,
    16: 9,
    17: 7,
    19: 5
}


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
        # if isNull(x) or isNull(y):
        #     return [0]

        return gf_rem(gf_mul(x, y, self.p, ZZ), self.reducing, self.p, ZZ)

    def div(self, x, y):
        # return gf_rem(
        d_ = gf_div(x, y, self.p, ZZ)
        # print('ddiv', d_)
        return d_
        # print('quo', gf_quo(d_, self.reducing, self.p, ZZ))
        # print('exquo', gf_exquo(d_, self.reducing, self.p, ZZ))
        # return gf_quo(d_, self.reducing, self.p, ZZ)
        # , self.reducing, self.p, ZZ)

    def inv(self, x):
        s, t, h = gf_gcdex(x, self.reducing, self.p, ZZ)
        return s


def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                '19', '20']
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


def fib(fib1, fib2, n):
    while n > 0:
        fib1, fib2 = fib2, F.add(F.mul(alpha, fib1), fib2)  # alpha * fib1 + fib2
        n -= 1
    # print('fib', fib1)
    return fib1


def ex(t, x):
    r = 0
    # print('len', len(t))
    for i in range(len(t)):
        r += t[i] * x ** (len(t) - i - 1)
        # print(r)

    return r


def gen(start, end):
    res = []

    i = 0
    while i < end - 1:
        # print('p+i', p + i)
        x = convert_base(int(start + i), int(q)).zfill(n + 1)  # '0001'
        y = [int(i) for i in str(x)]  # [int(i) for i in str(convert_base(, int(q)).zfill(n + 1))]
        res.append(y)
        # res.append(list()
        i += 1
    return res


def deArray(x):
    t = []
    for i_ in x:
        if len(i_):
            t.append(i_[0])
    return t


print('Исходная PG(n,p^r)\nn:')
n = int(input())
print('p:')
p = int(input())
print('r:')
r = int(input())
q = p ** r

# Исходная проект. геом.
print(f'PG(n={n}, F_q=F_{q})')

# По теореме Зингера
v = (q ** (n + 1) - 1) // (q - 1)
k = (q ** n - 1) // (q - 1)
la = (q ** (n - 1) - 1) // (q - 1)

# Исходный дизайн
print(f'D(v={int(v)}, k={int(k)}, la={int(la)})')

# Строим проективные векторы
projs = []
x = '1'.zfill(n + 1)
projs.append([int(i) for i in str(x)])

projs += gen(q, v)
print('proj_vects', projs)

F = GF(p, r)
alpha = alphas[q]
print('alpha is ', alpha)
t = gen(0, q * q + 1)

all = t
for i, t in enumerate(all):
    t.insert(0, 1)
# print('all', all)

# Cтроим первый блок вложением
B_1 = projs
for i, t in enumerate(B_1):
    t.insert(0, 0)

print('B1', B_1)
vect = []
vv = []
alpha = [int(i_) for i_ in str(convert_base(alpha, int(p)).zfill(n + 1))]

count_ = 0
print('all', all)
# exit(0)
aa = []
blocks = a = [[] for i in range(100)]
for l_, item in enumerate(B_1):
    available = list(all)

    # if item in available:
    #     available.remove(item)
    # Блоки
    i = 0
    while len(available):
        a = available.pop(0)  # вектор из доступных
        k = 0
        print('B', count_ + 2)  # ,'\n1 and 2', item, a)
        print(item)  # 1st
        print(a)  # second
        count_ += 1
        flag = False
        pre_flag = 0
        while k < v - 2:  # k+2 - номер столбца, который строим
            if flag:
                k -= 1
            else:
                pre_flag = 0
            vect = []
            vec = []
            vect0 = []
            j = 0
            for j in range(n + 2):  # j - номер строки
                x = [int(i_) for i_ in str(convert_base(item[j], int(p)).zfill(n + 2))]
                y = [int(i_) for i_ in str(convert_base(a[j], int(p)).zfill(n + 2))]
                vect.append(fib(x, y, k + 2))
            # vect - построенный вектор

            # Делим vect на vect[0]
            vect0 = []
            for i, it in enumerate(vect):
                if ex(vect[0], p) != 1 and ex(vect[0], p) != 0:
                    d = ex(deArray(F.div(deNull(it), deNull(vect[0]))), p)
                    vect0.append(d)

            for i, it in enumerate(vect):
                vec.append(ex(it, p))

            # if found in blocks -» avaiable.pop new
            flag = False
            # for i, itt in enumerate(blocks):

            if vect0 in blocks[l_] or vec in blocks[l_]:  # len ?
                # print('bl_c', blocks[l_])
                # print(vect0, 'found in', i, blocks[l_])
                flag = True
                # break

            # print('avail', available)
            if flag:
                # k -= 1
                pre_flag += 1
                if len(available):
                    # available.insert(len(available), a)
                    # aa.append(a)
                    a = available.pop(0)
                    # k+=1
                    continue
                else:
                    break
            else:
                if pre_flag:
                    # pass
                    k += 1

                    # k += pre_flag  # -1
                    # for i in range(len(aa)):
                    #     if not (aa[i] in available):
                    #         available.append(aa[i])
                k += 1
                if len(vect0):
                    # print('vector is', vect0)
                    blocks[l_].append(vect0)
                    print(vect0)
                else:
                    # print('vector is', vec)
                    blocks[l_].append(vec)
                    print(vec)
                if vec in available:
                    available.remove(vec)
                if vect0 in available:
                    available.remove(vect0)

        i += 1

print('blocks', count_ + 1)

n += 1
v = (q ** (n + 1) - 1) // (q - 1)
k = (q ** n - 1) // (q - 1)
la = (q ** (n - 1) - 1) // (q - 1)

# Исходный дизайн
print(f'D(v={int(v)}, k={int(k)}, la={int(la)})')
# # Делим vect на vect[0]
#             for i, it in enumerate(vect):
#                 if ex(vect[0], p) != 1:
#                     d = ex(deArray(F.div(deNull(it), deNull(vect[0]))), p)
#                     vect0.append(d)
#                 vec.append(ex(it, p))
