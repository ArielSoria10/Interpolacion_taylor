import matplotlib.pyplot as plt
import numpy as np


def serie_geometrica(x, N):
    x_arr = np.asarray(x, dtype=float)
    termino = np.ones_like(x_arr)
    suma = termino.copy()

    for _ in range(N):
        termino = termino * (-(x_arr**2))
        suma = suma + termino

    return float(suma) if np.isscalar(x) else suma


s40_09 = serie_geometrica(0.9, 40)
s40_11 = serie_geometrica(1.1, 40)

print(f"S_40(0.9) = {s40_09:.6f}")
print(f"S_40(1.1) = {s40_11:.6f}")

x = np.linspace(-1.5, 1.5, 1000)
f_exacta = 1.0 / (1.0 + x**2)

plt.figure(figsize=(10, 5.5))
plt.plot(
    x, f_exacta, label=r"$f(x) = \frac{1}{1+x^2}$", color="black", linewidth=2.5
)

estilos = [
    ("--", "royalblue"),
    ("-.", "crimson"),
    (":", "forestgreen"),
    ("--", "darkorange"),
]

for N, (ls, col) in zip([2, 5, 10, 20], estilos):
    plt.plot(
        x,
        serie_geometrica(x, N),
        linestyle=ls,
        color=col,
        linewidth=1.8,
        label=f"$S_{{{N}}}(x)$",
    )

plt.xlim(-1.5, 1.5)
plt.ylim(-0.5, 1.5)
plt.axvline(-1, color="gray", linestyle=":", linewidth=1)
plt.axvline(1, color="gray", linestyle=":", linewidth=1)
plt.axhline(0, color="gray", linewidth=0.8)
plt.title(r"Aproximación de $\frac{1}{1+x^2}$ mediante sumas parciales $S_N(x)$")
plt.xlabel("Eje $x$")
plt.ylabel("Eje $y$")
plt.grid(True, alpha=0.3)
plt.legend(loc="upper right")
plt.savefig("grafica_3_serie_geometrica.png", dpi=300, bbox_inches="tight")
plt.show()