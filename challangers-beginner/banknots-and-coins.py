value = float(input(""))
aux_value = value

#notes

notes_100 = int(value / 100)
aux_value = value - (notes_100 * 100)

notes_50 = int(aux_value / 50)
aux_value -= (notes_50 * 50)

notes_20 = int(aux_value / 20)
aux_value -= (notes_20 * 20)

notes_10 = int(aux_value / 10)
aux_value -= (notes_10 * 10)

notes_5 = int(aux_value / 5)
aux_value -= (notes_5 * 5)

notes_2 = int(aux_value / 2)
aux_value -= (notes_2 * 2)

#coins
coin_1 = int(aux_value / 1)
aux_value -= coin_1 * 1

coin_50 = int(aux_value / 0.50)
aux_value -= coin_50 * 0.50

coint_25 = int(aux_value / 0.25)
aux_value -= coint_25 * 0.25

coin_10 = int(aux_value / 0.10)
aux_value -= coin_10 * 0.10

coin_05 = int(aux_value / 0.050)
aux_value -= (coin_05 * 0.05)

coin_01 = int(aux_value / 0.01)


print(f"NOTAS:")
print(f"{notes_100} nota(s) de R$ 100.00")
print(f"{notes_50} nota(s) de R$ 50.00")
print(f"{notes_20} nota(s) de R$ 20.00")
print(f"{notes_10} nota(s) de R$ 10.00")
print(f"{notes_5} nota(s) de R$ 5.00")
print(f"{notes_2} nota(s) de R$ 2.00")

print(f"MOEDAS:")
print(f"{coin_1} moeda(s) de R$ 1.00")
print(f"{coin_50} moeda(s) de R$ 0.50")
print(f"{coint_25} moeda(s) de R$ 0.25")
print(f"{coin_10} moeda(s) de R$ 0.10")
print(f"{coin_05} moeda(s) de R$ 0.05")
print(f"{coin_01} moeda(s) de R$ 0.01")