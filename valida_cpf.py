cpf = int(input("Digite o seu cpf: "))
soma = 0
mult = 2
dv = cpf % 100
cpf = cpf // 100
backup_cpf = cpf


#Verificação se o CPF é válido

while cpf != 0:
    resto = cpf % 10
    cpf = cpf // 10

    soma = soma + resto * mult
    mult = mult + 1

resto = soma % 11

if resto < 2:
    dc1 = 0
else:
    dc1 = 11 - resto

cpf = backup_cpf * 10 + dc1 #*10 pro número ganhar mais uma casa decimal
backup_cpf = cpf
# backup_cpf = str(backup_cpf) + str(dc)
mult = 2
soma = 0

while cpf != 0:
    resto = cpf % 10
    cpf = cpf // 10
    soma = soma + resto * mult
    mult = mult + 1

resto = soma % 11
if resto < 2:
    dc2 = 0
else:
    dc2 = 11 - resto

dvteste = dc1 * 10 + dc2 


# print("O segundo digito verificador é:",dc)
# backup_cpf = backup_cpf * 10 + dc

if dv != dvteste:
    print("Os digitos verificadores deveriam ser:", dvteste,"porém você informou:", dv)
    print("Portanto, CPF inválido")

else:
    print("Os digitos verificadores deveriam ser:", dvteste,"e você informou:", dv)
    print("Portanto, CPF válido")

    