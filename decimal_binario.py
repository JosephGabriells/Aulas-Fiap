num = int(input("Digite o seu número decimal: "))
backup_num = num
soma = 0
binario = 0
i = 1
while num != 0:
    resto = num % 2
    num = num // 2
    print(resto)
    binario = resto * i + binario
    i = i * 10

print("O número", backup_num,"em decimal é representado pelo número", binario,"em binário.")

    

    
    
