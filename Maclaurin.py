import matplotlib.pyplot as plt
import numpy as np


def taylor_sin(x, n):
    x_arr = np.asarray(x, dtype=float)
    termino = x_arr.copy()
    suma = termino.copy()

    num_pasos = (n - 1) // 2
    for k in range(num_pasos):
        termino = termino * (-(x_arr**2)) / ((2 * k + 2) * (2 * k + 3))
        suma = suma + termino

    return float(suma) if np.isscalar(x) else suma


p9_pi = taylor_sin(np.pi, 9)
print(f"P_9(pi) = {p9_pi:.6f}")

grados = list(range(1, 22, 2))
x_pi = np.linspace(-np.pi, np.pi, 2001)
x_pi4 = np.linspace(-np.pi / 4, np.pi / 4, 2001)

err_max_pi = [np.max(np.abs(np.sin(x_pi) - taylor_sin(x_pi, g))) for g in grados]
err_max_pi4 = [
    np.max(np.abs(np.sin(x_pi4) - taylor_sin(x_pi4, g))) for g in grados
]

grado_menor_pi = next(g for g, e in zip(grados, err_max_pi) if e < 1e-6)
grado_menor_pi4 = next(g for g, e in zip(grados, err_max_pi4) if e < 1e-6)

print(f"Menor grado impar con error < 10^-6 en [-pi, pi]:     {grado_menor_pi}")
print(
    f"Menor grado impar con error < 10^-6 en [-pi/4, pi/4]: {grado_menor_pi4}"
)

x_g1 = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
plt.figure(figsize=(10, 5))
plt.plot(x_g1, np.sin(x_g1), label=r"$\sin(x)$", color="black", linewidth=2.5)

estilos = [
    ("--", "royalblue"),
    ("-.", "crimson"),
    (":", "forestgreen"),
    ("--", "darkorange"),
    ("-.", "purple"),
]

for g, (ls, col) in zip([1, 3, 5, 7, 9], estilos):
    plt.plot(
        x_g1,
        taylor_sin(x_g1, g),
        linestyle=ls,
        color=col,
        linewidth=1.8,
        label=f"$P_{g}(x)$",
    )

plt.xlim(-2 * np.pi, 2 * np.pi)
plt.ylim(-2, 2)
plt.axhline(0, color="gray", linewidth=0.8)
plt.axvline(0, color="gray", linewidth=0.8)
plt.title(r"Aproximación de $\sin(x)$ mediante polinomios de Maclaurin")
plt.xlabel("Eje $x$ (radianes)")
plt.ylabel("Eje $y$")
plt.grid(True, alpha=0.3)
plt.legend(loc="upper right")
plt.savefig("grafica_1_taylor_sin.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure(figsize=(10, 5))
plt.semilogy(
    grados,
    err_max_pi,
    "o-",
    label=r"Error máximo en $[-\pi, \pi]$",
    color="crimson",
    linewidth=1.8,
)
plt.semilogy(
    grados,
    err_max_pi4,
    "s--",
    label=r"Error máximo en $[-\pi/4, \pi/4]$",
    color="royalblue",
    linewidth=1.8,
)
plt.axhline(
    1e-6, color="black", linestyle=":", linewidth=1.2, label="Tolerancia $10^{-6}$"
)

plt.xticks(grados)
plt.title("Error máximo de Maclaurin según el grado impar $n$")
plt.xlabel("Grado impar $n$")
plt.ylabel(r"$\max |\sin(x) - P_n(x)|$ (escala logarítmica)")
plt.grid(True, which="both", linestyle="--", alpha=0.3)
plt.legend()
plt.savefig("grafica_2_error_maclaurin.png", dpi=300, bbox_inches="tight")
plt.show()