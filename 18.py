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
if num1 > num2 and num1 < num3:
    num5 = num1
elif num1 < num2 and num1 > num3:
    num5 = num1
else:
    if num2 > num1 and num2 < num3:
        num5 = num2
    elif num2 < num1 and num2 > num3:
        num5 = num2
    else:
        if num3 > num1 and num3 < num2:
            num5 = num3
        elif num3 < num1 and num3 > num2:
            num5 = num3
num6 = num4 + num5
print("A soma do primeiro e do segundo número é:", num6)
