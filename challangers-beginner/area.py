value_1, value_2, value_3 = str(input("")).split(" ")
value_1 = float(value_1)
value_2 = float(value_2)
value_3 = float(value_3)

#area triangle rectangle 
area_triangle = (value_1 * value_3) / 2

#area of a circle 
area_circle = 3.14159 * value_3 ** 2

#area of a trapeze
area_trapeze = ((value_1 + value_2) *value_3) / 2

#area of a square
area_square = (value_2**2)

#area of a rectangle
area_rectangle = value_1 * value_2

print(f"TRIANGULO: {area_triangle:.3f}")
print(f"CIRCULO: {area_circle:.3f}")
print(f"TRAPEZIO: {area_trapeze:.3f}")
print(f"QUADRADO: {area_square:.3f}")
print(f"RETANGULO: {area_rectangle:.3f}")
