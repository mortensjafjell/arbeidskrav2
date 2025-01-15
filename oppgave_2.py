import math

antall_elever = int(input("Skriv inn antall elever: "))

antall_pizza = antall_elever * 0.25
antall_pizza_avrundet = math.ceil(antall_pizza)

print(f"Det må handles inn {int(antall_pizza_avrundet)} pizzaer til klassefesten.")
