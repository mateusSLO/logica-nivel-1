print("Digite a idade em anos:")
ano = int(input())
ano2 = ano * 365
print("Digite a idade em meses:")
meses = int(input())
if meses == 1:
    meses = 31
elif meses == 2:
    meses = 59
elif meses == 3:
    meses = 90
elif meses == 4:
    meses = 120
elif meses == 5:
    meses = 151
elif meses == 6:
    meses = 181
elif meses == 7:
    meses = 212
elif meses == 8:
    meses = 243
elif meses == 9:
    meses = 273
elif meses == 10:
    meses = 304
elif meses == 11:
    meses = 334
elif meses == 12:
    meses = 365
dias = ano2 + meses
print("Sua idade em dias é", dias)
