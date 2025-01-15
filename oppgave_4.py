# Eksisterende data i dictionary
data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873],
}

# Hvis landet brukeren skriver inn finnes i dictionarien, skrives informasjonen til konsollen
land = input("Hvilket land vil du lære mer om? ")
if land in data:
    hovedstad, innbyggere = data[land]
    print(f"{hovedstad} er hovedstaden i {land}, og det er {innbyggere} millioner innbyggere i {hovedstad}.")

# Hvis landet ikke finnes i dictionarien, kan brukeren legge den til
else:
    def legg_til_data(data):
        land = input("Har ingen informasjon om dette landet. Skriv inn navn på landet: ")
        hovedstad = input(f"Skriv inn hovedstaden i {land}: ")
        innbyggere = float(input(f"Skriv inn antall innbyggere i {hovedstad} (bruk tall, og følgende format, f.eks 2.161): "))

        data[land] = [
            hovedstad,
            innbyggere
        ]
        print(f"Informasjon om {land} er lagt til!")

    # Ny data lagres til dictionary
    legg_til_data(data)
    
    # Det skrives til konsoll at data er lagt til dictionarien
    print("Oppdatert informasjon om land: ", data)
