# Input do usuário sobre a quantidade de produtos
quantidade_produtos = int(input("Digite a quantidade de produtos que você deseja aumentar: "))
# Validação da quantidade de produtos
while quantidade_produtos <= 0:
    quantidade_produtos = int(input("Por favor, digite uma quantidade válida de produtos: "))    

# Atribuição das variáveis iniciais    
i = 1
maior_aumento_reais = 0
maior_aumento_percentual = 0

# while com base na quantidade de produtos para colher os preços
while i <= quantidade_produtos:
     preco_atual = float(input("Digite o preço atual do produto: R$"))
     # Validação do preço atual
     while preco_atual <= 0:
         preco_atual = float(input("Por favor, digite um valor válido para o preço atual do produto: R$"))  
         
     preco_reajustado = float(input("Digite o preço reajustado do produto: R$"))
     # Validação do preço reajustado   
     while preco_reajustado <= 0:
         preco_reajustado = float(input("Por favor, digite um valor válido para o preço reajustado do produto: R$"))  
     
     # Calculo das diferenças em reais e percentual
     diferenca_preco_reais = preco_reajustado - preco_atual
     diferenca_preco_percentual = (diferenca_preco_reais / preco_atual) * 100
     
     # Verificação de qual o maior aumento em reais 
     if diferenca_preco_reais > maior_aumento_reais:
         maior_aumento_reais = diferenca_preco_reais

     
     # Verificação de qual o maior aumento percentual 
     if diferenca_preco_percentual > maior_aumento_percentual:
         maior_aumento_percentual = diferenca_preco_percentual

     
     # Incremento da váriavel que rege o while
     i = i + 1
     
# Saída para o usuário mostrando quais os maiores aumentos
print("O maior aumento em reais foi de: R${:.2f}".format(maior_aumento_reais))     
print("O maior aumento percentual foi de: {:.2f}".format(maior_aumento_percentual),"%")
