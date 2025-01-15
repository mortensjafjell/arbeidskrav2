import numpy as np
import matplotlib.pyplot as plt

# Funksjonen for x
def f(x):
    return -x ** 2 - 5

x = np.linspace(-10, 10, 200)
y = f(x)

# Endre bakgrunn til svart
plt.style.use("dark_background")

# Plotte figuren, inkludert størrelse
plt.figure(figsize=(8, 6))

# Grafens utseende
plt.title("Plotting av funksjonen f(x) = -x**2 - 5")
plt.xlabel("X", fontsize=14)
plt.ylabel("Y", fontsize=14, rotation="horizontal")

# Plotte grid og linje
plt.grid()
plt.plot(x, y, "teal", linewidth=2)

plt.show()
