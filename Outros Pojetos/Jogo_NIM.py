print("Bem-Vindo ao jogo do NIM!!")

def computador_escolhe_jogada(n, m):
    resto = n % (m + 1)
    if resto == 0:
        print(f"O computador tirou", (m), ("peças"))
        return m
    else:
        print(f"O computador tirou", (resto), ("peças"))
        return resto

def usuario_escolhe_jogada(n, m):
    while True:
        try:
            jogada = int(input("Quantas peças você vai tirar?"))
            if 1 <= jogada <= m and jogada <= n:
                return jogada
            else:
                print("Oops! Jogada inválida! Tente de novo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
def partida():
    print("Bem-Vindo ao jogo do NIM!!")

    while True:
        try:
            n = int(input("Quantas peças?"))
            m = int(input("Limite de peças por jogada?"))
            
            if n <= 0 or m <= 0 or m > n:
                print("Entradas inválidas. N e M devem ser números positivos e M não pode ser maior que N. Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digíte os números inteiros para N e M.")
    if n % (m + 1) == 0:
        print("Você começa!")
        jogador_atual = "usuario"
    else:
        print("Computador começa!")
        jogador_atual = "computador"
    while n > 0:
        if jogador_atual == "computador":
            jogada = computador_escolhe_jogada(n, m)
            n -= jogada
            print(f"Agora restam {n} peças no tabuleiro.")
            jogador_atual = "usuario"
        else:
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            print(f"Você tirou {jogada} peças.")
            print(f"Agora restam {n} peças no tabuleiro.")
            jogador_atual = "computador"
    if jogador_atual == "computador":
        print("Fim do jogo! Você ganhou!")
        return "usuario"
    else:
        print("Fim do jogo! O computador ganhou!")
        return "computador"
def campeonato():
    print("Você escolheu um campeonato!")
    placar_usuario = 0
    placar_computador = 0
    for i in  range(1,4):
        print(f"**** Rodada {i} ****")
        vencedor_rodada = partida()

        if vencedor_rodada == "usuario":
            placar_usuario += 1
        else: 
            vencedor_rodada == "computador"
            placar_computador += 1
    print("**** Final do campeonato! ****")
    print(f"Placar: Você {placar_usuario} X {placar_computador} Computador")

while True:
    print("Escolha:")   
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    try:
        escolha = int(input())

        if escolha == 1:
            partida()
            break 
        elif escolha == 2:
            campeonato()
            break 
        else:
            print("Escolha inválida. Por favor, digite 1 ou 2.")
    except ValueError:
        print("Entrada inválida. Por favor, digite 1 ou 2.")
