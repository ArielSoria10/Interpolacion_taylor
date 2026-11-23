import math


def taylor_exp(x, n=100):
    termino = 1.0
    suma = 1.0
    max_term = 1.0
    for k in range(1, n + 1):
        termino = termino * x / k
        suma += termino
        if abs(termino) > max_term:
            max_term = abs(termino)
    return suma, max_term


p100_neg, mayor_termino = taylor_exp(-20.0, 100)
p100_pos, _ = taylor_exp(20.0, 100)
inv_pos = 1.0 / p100_pos

print(f"math.exp(-20)       = {math.exp(-20):.16e}")
print(f"P_100(-20)          = {p100_neg:.16e}")
print(f"Mayor |término|     = {mayor_termino:.6f}")
print(f"1 / P_100(20)       = {inv_pos:.16e}")