print("Informe o primeiro número")
num1 = float(input())
print("Informe o segundo número")
num2 = float(input())
print("Informe o terceiro número")
num3 = float(input())
if num1 > num2 and num1 > num3:
    num4 = num1
elif num2 > num3 and num2 > num1:
    num4 = num2
elif num3 > num2 and num3 > num1:
    num4 = num3
else:
   num4 = "Todos os números são iguais"
print("O maior numero é:", num4)
