import numpy as np

def beregn_form(a, b):

    #Beregning av areal
    areal_trekant = (a*b / 2)

    areal_halvsirkel = (np.pi * a ** 2) / 2

    totalt_areal = areal_trekant + areal_halvsirkel

    #Beregning av omkrets
    hypotenus = np.sqrt(a**2 + b**2)

    omkrets_halvsirkel = (2 * np.pi * a) / 2
    
    total_omkrets = hypotenus + b + omkrets_halvsirkel

    return totalt_areal, total_omkrets

#Input fra bruker som oppgir lengde for side a og b
a = float(input("Oppgi lengde for side a: "))
b = float(input("Oppgi lengde for side b: "))

areal, omkrets = beregn_form(a, b)

# Svar skrives til konsoll, hvor svaret er begrenset til 2 desimaler
print(F"Arealet av figuren er {areal:.2f}, og omkretsen er {omkrets:.2f}.")
