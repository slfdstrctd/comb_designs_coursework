import itertools
from sympy.polys.domains import ZZ
from sympy.polys.galoistools import (gf_irreducible_p, gf_add, \
                                     gf_sub, gf_mul, gf_rem, gf_div, gf_gcdex)
from sympy.ntheory.primetest import isprime


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
    3: 2,
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
        y = deNull(y)
        return gf_rem(gf_mul(x, y, self.p, ZZ), self.reducing, self.p, ZZ)

    def div(self, x, y):
        d_ = gf_div(x, y, self.p, ZZ)
        d_ = d_[::-1]

        for i in range(len(d_)):
            if not len(d_[i]):
                d_[i].append(0)
        return d_

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


def fib(x, y, n):
    if n < 0:
        print("Incorrect input")
        return []
    elif n == 0:
        return x
    else:
        for i in range(1, n):
            mul = F.mul(alpha, x)
            c = F.add(mul, y)
            x = y
            y = c
        return y


def ex(t, x):
    r = 0
    for i in range(len(t)):
        r += t[i] * x ** (len(t) - i - 1)
    return r


def gen(start, end):
    res = []

    i = 0
    while i < end - 1:
        x = convert_base(int(start + i), int(q)).zfill(n + 1)  # '0001'
        y = [int(i) for i in str(x)]  # [int(i) for i in str(convert_base(, int(q)).zfill(n + 1))]
        res.append(y)
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
aa = []

blocks = [[[] for j in range(1000)] for k in range(1000)]
err = 0
# Новый раздел
for l_, item in enumerate(B_1):
    available = list(all)
    # Блоки
    icc = 0
    err = 0

    # Построение нового блока в разделе
    while len(available):
        if not err:
            print('B', count_ + 2)
            count_ += 1  # номер блока

        a = available.pop(0)  # вектор из доступных

        print(item)
        print(a)
        blocks[l_][icc].append(item)
        blocks[l_][icc].append(a)
        k = 0
        # Построение вектора в блоке
        while k < v - 2:  # k+2 - номер столбца, который строим
            vect = []
            vec = []
            vect0 = []
            j = 0
            for j in range(n + 2):  # j - номер строки
                x = [int(i_) for i_ in str(convert_base(item[j], int(p))).zfill(n + 2)]
                y = [int(i_) for i_ in str(convert_base(a[j], int(p))).zfill(n + 2)]
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

            err = 0
            # Проверяем, нет ли построенного вектора в предыдущих
            for j_, jjt in enumerate(blocks[l_]):
                if (len(vect0) and vect0 in jjt) or vec in jjt:
                    # print(vect0, vec, jjt)
                    err = 1
                    blocks[l_][icc] = []

            if err:
                break

            if not err:
                if len(vect0):
                    blocks[l_][icc].append(vect0)
                    print(vect0)
                else:
                    blocks[l_][icc].append(vec)
                    print(vec)
                if vec in available:
                    available.remove(vec)
                if vect0 in available:
                    available.remove(vect0)
            k += 1
        icc += 1

print('blocks', count_ + 1, )
blocks[0].insert(0, B_1)

b = []
b_ = []
for i_, iit in enumerate(blocks):
    for j_, jjt in enumerate(iit):
        if len(jjt):
            for h_ in range(len(jjt[0])):
                b = []
                for k_ in range(len(jjt)):
                    b.append(jjt[k_][h_])
                b_.append(b)

f = open(f"blocks{p}{r}.txt", "w")
for i in range(len(b_)):
    f.write(str(b_[i])[1:-1] + '\n')
f.close()

# Полученный дизайн
n += 1
v = (q ** (n + 1) - 1) // (q - 1)
k = (q ** n - 1) // (q - 1)
la = (q ** (n - 1) - 1) // (q - 1)
print(f'D(v={int(v)}, k={int(k)}, la={int(la)})')
