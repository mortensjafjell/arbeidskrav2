import numpy as np

# Input hvor bruker kan oppgi gradtallet som skal omregnes
v_grad = float(input("Skriv inn gradtallet: "))

# Funksjonen med beregningen
def grad_til_rad(v_grad):
    return v_grad*np.pi / 180

# Utførelsen av beregningen
v_rad = grad_til_rad(v_grad)

print(f"Gradtallet {v_grad} er det samme som {v_rad:.4f} radianer.")
