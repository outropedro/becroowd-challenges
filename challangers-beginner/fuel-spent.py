time = int(input(""))
kmh = int(input(""))

km_total = time * kmh

fuel_spent = km_total / 12

print(f"{fuel_spent:.3f}")