a, b, c = str(input("")).split(" ")
a = int(a)
b = int(b)
c = int(c)

maiorAB = (a + b + abs(a - b)) / 2

if c > maiorAB:
    print(f"{int(c)} eh o maior")
else: 
    print(f"{int(maiorAB)} eh o maior")