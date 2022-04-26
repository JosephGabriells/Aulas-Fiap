num = int(input("Digite o seu número decimal: "))
backup_num = num
hex = 0
i = 1

while num != 0:
    resto = num % 16
    num = num // 16
    
    if resto < 9:
        hex = str(resto) + str(hex)
    elif resto == 10:
        hex = "A" + str(hex)
    elif resto == 11:
        hex = "B" + str(hex)
    elif resto == 12:
        hex = "C" + str(hex)
    elif resto == 13:
        hex = "D" + str(hex)
    elif resto == 14:
        hex = "E" + str(hex)
    elif resto == 15:
        hex = "F" + str(hex)
          
print("O número", backup_num,"é representado por",hex[:-1],"em hexadecimal.")

#print("O número", backup_num,"em decimal é representado pelo número", binario,"em binário.")

    

    
    
