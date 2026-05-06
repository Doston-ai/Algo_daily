import numpy as np
import matplotlib.pyplot as plt

def eka_simulyatsiya(qoida, kataklar):
    bits = format(qoida, '08b')
    jadval = {}
    for i, k in enumerate(['111','110','101','100','011','010','001','000']):
        jadval[k] = int(bits[i])

    holat = np.zeros(kataklar, dtype=int)
    holat[kataklar // 2] = 1

    tarix = [holat.copy()]
    for _ in range(kataklar - 1):
        yangi = np.zeros(kataklar, dtype=int)
        for i in range(kataklar):
            chap   = holat[(i-1) % kataklar]
            markaz = holat[i]
            ong    = holat[(i+1) % kataklar]
            yangi[i] = jadval[f"{chap}{markaz}{ong}"]
        holat = yangi
        tarix.append(holat.copy())

    return np.array(tarix)  

def hayot_simulyatsiya(boshlangich_holat, qadamlar):
    holat = boshlangich_holat.copy()
    n = holat.shape[0]

    tarix = [holat.copy()]
    for _ in range(qadamlar - 1):
        yangi = np.zeros((n, n), dtype=int)
        for i in range(n):
            for j in range(n):
                qoshnilar = (
                    holat[(i-1)%n][(j-1)%n] + holat[(i-1)%n][j] + holat[(i-1)%n][(j+1)%n] +
                    holat[i][(j-1)%n]                            + holat[i][(j+1)%n] +
                    holat[(i+1)%n][(j-1)%n] + holat[(i+1)%n][j] + holat[(i+1)%n][(j+1)%n]
                )
                if holat[i][j] == 1:        # katak tirik bo'lsa
                    if qoshnilar == 2 or qoshnilar == 3:
                        yangi[i][j] = 1     # yashaydi
                    else:
                        yangi[i][j] = 0     # o'ladi

                else:                        # katak o'lik bo'lsa
                    if qoshnilar == 3:
                        yangi[i][j] = 1     # tiriladi
                    else:
                        yangi[i][j] = 0     # o'lik qoladi
        holat = yangi
        tarix.append(holat.copy())

    return np.array(tarix)


eka_qoida    = int(input("Qoida raqami (0-255, masalan 110): "))
eka_kataklar = int(input("Kataklar soni NxN (masalan 60): "))

hayot_qadamlar = int(input("Vaqt qadamlari (masalan 30): "))


eka_tarix   = eka_simulyatsiya(eka_qoida, eka_kataklar)
hayot_tarix = hayot_simulyatsiya(eka_tarix, hayot_qadamlar)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Katakli Avtomatlar", fontsize=15, fontweight='bold')

axes[0].imshow(eka_tarix, cmap='binary', interpolation='nearest')
axes[0].set_title(f"EKA — Qoida {eka_qoida}", fontsize=12)
axes[0].set_xlabel("Katak")
axes[0].set_ylabel("Vaqt (avlod)")


axes[1].imshow(hayot_tarix[-1], cmap='binary', interpolation='nearest')
axes[1].set_title(f"Hayot o'yini — {hayot_qadamlar}-avlod", fontsize=12)
axes[1].set_xlabel("Katak (x)")
axes[1].set_ylabel("Katak (y)")

plt.tight_layout()
plt.show()