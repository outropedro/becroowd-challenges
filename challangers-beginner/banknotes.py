value = int(input(""))

aux_value = value

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

notes_1 = int(aux_value / 1)
aux_value -= (notes_1 * 1)


print(f"{value}")
print(f"{notes_100} nota(s) de R$ 100,00")
print(f"{notes_50} nota(s) de R$ 50,00")
print(f"{notes_20} nota(s) de R$ 20,00")
print(f"{notes_10} nota(s) de R$ 10,00")
print(f"{notes_5} nota(s) de R$ 5,00")
print(f"{notes_2} nota(s) de R$ 2,00")
print(f"{notes_1} nota(s) de R$ 1,00")