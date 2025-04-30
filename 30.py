print("Digite um número de 0 a 10:")
n = int(input())
vetor = [1,2,3,4,4,4,5,6,6,6,6,6,7,8,8,8,8,8,8,8,9,10,10,10,10,10,10,10,10,10]
count = 0
for m in vetor:
    if m == n:
        count += 1
print("O número se repete",count)
