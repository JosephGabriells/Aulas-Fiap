num = int(input("Digite o seu número binário: "))
backup_num = num
multi = 0
binario = 0 
soma = 0
while num != 0:
    binario = num % 10
    num = num // 10
    soma = soma + (binario * (2 ** multi))
    multi = multi + 1
    
print("O número", backup_num,"em binário representa o número", soma,"em decimal.")
