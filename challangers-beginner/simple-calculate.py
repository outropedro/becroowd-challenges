code_product_1, quantity_product_1, value_product_1= str(input("")).split(" ")
code_product_1 = int(code_product_1)
quantity_product_1 = int(quantity_product_1)
value_product_1 = float((value_product_1))

code_product_2, quantity_product_2, value_product_2 = str(input("")).split(" ")
code_product_2 = int(code_product_2)
quantity_product_2 = int(quantity_product_2)
value_product_2 = float((value_product_2))

value_product_1 = quantity_product_1 * value_product_1

value_product_2 = quantity_product_2 * value_product_2

total_value = value_product_1 + value_product_2

print(f"VALOR A PAGAR: R$ {total_value:.2f}")