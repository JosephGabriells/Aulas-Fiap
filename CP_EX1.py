# Input do usuário
n = int(input("Digite a quantidade de números que deseja inserir: "))
# Validação do input do usuário
while n <= 0:
    n = int(input("Digite uma quantidade válida de números que deseja inserir: "))

# Atribuição das variáveis iniciais
i = 0
seguimento = 0
num_comparacao = 0

# Verificação para condição de apenas um número
if n !=1:
    # While para a verificação das sequências
    while i < n:
        num = int(input("Digite o número: "))
        if num != num_comparacao:
            num_comparacao = num
            seguimento = seguimento + 1
        i = i + 1
else:
    num = int(input("Digite o número: "))
    seguimento = seguimento + 1

# Saída para o usuário
print("O número total de segmentos de números é:",seguimento)


