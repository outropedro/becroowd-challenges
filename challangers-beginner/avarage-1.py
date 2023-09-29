PESO_NOTA_1 = 2
PESO_NOTA_2 = 3
PESO_NOTA_3 = 5
nota1 = float(input(""))
nota2 = float(input(""))
nota3 = float(input(""))

media =  (nota1 * PESO_NOTA_1 + nota2 * PESO_NOTA_2 + nota3 * PESO_NOTA_3) / (PESO_NOTA_1 + PESO_NOTA_2 + PESO_NOTA_3)

print(f"MEDIA = {media:.1f}")