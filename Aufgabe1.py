import matplotlib.pyplot as plt
import numpy as np


data = np.array([
    [0.0, 7.94876054e-10],
    [5.0, 3.75527088e-05],
    [10.0, 0.000118826436],
    [10.0, 0.000117368945],
    [15.0, 0.000185304583],
    [20.0, 0.000245806004],
    [25.0, 0.00029399863],
    [30.0, 0.000335263321],
    [35.0, 0.000368086767],
    [40.0, 0.000395529321],
    [45.0, 0.000419339776],
    [50.0, 0.00043867738],
])

I = data[:, 0]   # first column
P = data[:, 1]   # second column

P_korr = (P-P[0]) * 1e6
steigung = np.diff(P_korr) / np.diff(I)

fig, ax = plt.subplots(figsize=(6.2, 4.2))
ax.plot(I, P_korr, "o-",ms=5, lw=1, color="C0")

ax.set_xlabel("Strom $I$ in mA")
ax.set_xlabel("Leistung $P$ in µW")
ax.set_xlim(0,52)
ax.set_ylim(0,None)
ax.grid(alpha=0.3)
ax.legend(loc="lower right")
fig.tight_layout()
fig.savefig("results/aufgabe1.png", dpi=200)