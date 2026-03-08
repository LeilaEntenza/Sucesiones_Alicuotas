# ¡Hola!, este repositorio está destinado a la divulgación científica y la eficiencia en la resolución de sucesiones alícuotas.
num = -1
while (num <= 0):
    num = int(input("Ingrese un número"))

divisores = []
if num != 0:
    for i in range (num, 1):
        if num%i==0:
            divisores[len(divisores)] = i
            print(i + " es divisor")