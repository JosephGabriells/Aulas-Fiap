import random
jogadas = ["Pedra", "Papel", "Tesoura"]
rodadas = 1

print("Bem vindo ao Jokenpo x Python!")
while rodadas <= 3:
    print("Esta é a rodada", rodadas,"de 3")
    print("------------------------------------------")
    print("0 - Pedra")
    print("1 - Papel")
    print("2 - Tesoura")
    print("------------------------------------------")
    jogador = int(input("Digite a sua jogada: "))
    while jogador != 0 and jogador != 1 and jogador != 2:
        jogador = int(input("Por favor, digite uma jogada válida. Digite a sua jogada: "))
        
    i = random.randint(0,2)
    cpu = jogadas[i]

    print("------------------------------------------")
    if jogador == i:
        print("Houve um empate! Ambos selecionaram: ", jogadas[i])
    else:
        if jogadas[i] == jogadas[0]:
            if jogador == 1:
                print("Parabéns, você ganhou! Você jogou:", jogadas[jogador],"e a CPU jogou",jogadas[i])     
            else:
                print("Infelizmente, você perdeu! Você jogou:", jogadas[jogador],"e a CPU jogou",jogadas[i])     
                
        if jogadas[i] == jogadas[1]:
            if jogador == 2:
                print("Parabéns, você ganhou! Você jogou:", jogadas[jogador],"e a CPU jogou",jogadas[i])    
            else:
                print("Infelizmente, você perdeu! Você jogou:", jogadas[jogador],"e a CPU jogou",jogadas[i])   
                
        if jogadas[i] == jogadas[2]:
            if jogador == 0:
                print("Parabéns, você ganhou! Você jogou:", jogadas[jogador],"e a CPU jogou",jogadas[i])
            else:
                print("Infelizmente, você perdeu! Você jogou:", jogadas[jogador],"e a CPU jogou",jogadas[i])
    print("------------------------------------------")
    
    rodadas = rodadas + 1
    
    if rodadas <= 3:
        print("Deseja seguir para a próxima rodada?(Y/N)")
        resposta = input("Resposta: ")
        while resposta != "y" and resposta != "n":
            print("Deseja seguir para a próxima rodada?(Y/N)")
            resposta = input("Resposta: ")
            
        if resposta == "y":
            continue
        else:
            break       