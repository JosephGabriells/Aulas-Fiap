# Input do usuário sobre o valor da cédula e das moedas
cedula = int(input("Digite o valor da cédula: "))
# Validação da cédula
while cedula <= 0:
    cedula = int(input("Por favor, digite um valor válido para a cédula: "))
    
moeda1 = int(input("Digite o valor de uma moeda: "))
# Validação da moeda 1
while moeda1 <= 0:
    moeda1 = int(input("Por favor, digite um valor válido para a moeda: "))
    
moeda2 = int(input("Digite o valor de outra moeda: "))
# Validação da moeda 2
while moeda2 <= 0:
    moeda2 = int(input("Por favor, digite um valor válido para a moeda: "))

# Atribuição das variáveis iniciais
valor_total = cedula
contador_moeda1 = 0
contador_moeda2 = 0
troco = 0

# Algoritmo para o cálculo do troco
while troco < cedula:
    if moeda1 > moeda2:
        if (valor_total - moeda1 > 0 and valor_total - moeda1 > moeda2) or (valor_total - moeda1 == 0):
            valor_total = valor_total - moeda1
            contador_moeda1 = contador_moeda1 + 1
        elif valor_total - moeda2 > 0 or valor_total - moeda2 == 0:
            valor_total = valor_total - moeda2
            contador_moeda2 = contador_moeda2 + 1    
        else:
            break   
        
    else:
        if (valor_total - moeda2 > 0 and valor_total - moeda2 > moeda1) or (valor_total - moeda2 == 0):
            valor_total = valor_total - moeda2
            contador_moeda2 = contador_moeda2 + 1
        elif (valor_total - moeda1 > 0) or (valor_total - moeda1 == 0):
            valor_total = valor_total - moeda1
            contador_moeda1 = contador_moeda1 + 1    
        else:
            break   
        
    # Incremento do troco   
    troco = contador_moeda1 * moeda1 + contador_moeda2 * moeda2
    
    
# Algoritmo para verificação se é possível realizar a troca
if troco == cedula:
    print("Possível:", contador_moeda1,"moeda(s) de", moeda1,"e",contador_moeda2,"moeda(s) de", moeda2)
else:
    print("Não é possível realizar a troca.")
   

        
    




