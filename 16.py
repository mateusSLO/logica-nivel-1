print("A unidade da maçã custa R$1,30")
print("Se for uma dúzia ou mais a unidade da maçã custa R$1,00")
num = int(input())
if num < 12:
    num2 = num * 1.30
elif num >= 12:
    num2 = num * 1
else:
    print("invalido")
print("Pague", num2)
