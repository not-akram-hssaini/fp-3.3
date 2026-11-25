import numpy as np
import math as m


# Unsicherheit beim Ablesen der Skala: 0.01/sqrt(12) Typ A


# Nimmt die 3 Minima, und berechnet den Kalibrierungskoeffizienten und seine Unsicherheit.
def kalibieren(a, b, c):
    # Abstände berechnen
    diff = np.diff([a, b, c])
    x = np.mean(diff)

    # Unsicherheit nach Merkblatt
    typ_A = np.std(diff, ddof=1) / np.sqrt(len(diff))
    typ_B = 0.01 / np.sqrt(12)
    u_ges = np.sqrt(typ_B**2 + typ_A**2)

    # Kalibrierungsfaktor
    gamma = 2 * np.pi / x
    u_gamma = 2 * np.pi * u_ges / x**2

    return gamma, u_gamma



# Kalibrierungskoeffizienten
gamma = [
    kalibieren(4.62, 21.02, 37.83),         #Filter 4
    kalibieren(6.00, 21.23, 36.18),         #Filter 3
]
print("Kalibrrierungskoeffizienten: ")
print(f"\tFilter 4: {gamma[0][0]} +- {gamma[0][1]}")
print(f"\tFilter 3: {gamma[1][0]} +- {gamma[1][1]}")




#Nimmt die 3 neuen Minima nach einführen der Platte, berechnet die differenz in Phaseneinheiten zwischen den Minima.
def Phasendiff(kal, old, new):
    gamma, u_gamma = kal

    # Differenzen der Trommelskala
    dx = old - new

    # Phasendifferenzen
    phi = gamma * dx

    # Mittelwert
    x = np.mean(phi)

    # Typ-A-Unsicherheit
    u_A = np.std(phi, ddof=1) / np.sqrt(len(phi))

    # Typ-B-Unsicherheit der Ablesung
    u_B_ablesung = gamma * 0.01 / np.sqrt(12) * np.sqrt(2 / len(phi))

    # Unsicherheit des Kalibrierungsfaktors
    u_B_gamma = np.abs(np.mean(dx)) * u_gamma

    # Gesamte Unsicherheit
    u_ges = np.sqrt(
        u_A**2 +
        u_B_ablesung**2 +
        u_B_gamma**2
    )

    return x, u_ges

delta = [
    Phasendiff(gamma[0], np.array([4.62, 21.02, 37.83]), np.array([0.62, 17.24, 33.78])),    #Filter 4
    Phasendiff(gamma[1], np.array([6.00, 21.23, 36.18]), np.array([2.32, 17.30, 32.52]))     #Filter 3
]

print("\nVerzögerungen der Platte: ")
print(f"\tFilter 4: {delta[0][0]} +- {delta[0][1]}")
print(f"\tFilter 3: {delta[1][0]} +- {delta[1][1]}")