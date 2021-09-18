from jogo_da_velha import branco, token, verificaGanhador

def movimentoIA(board, jogador):
    
    possibilidades = getPosicoes(board)
    # print(possibilidades)
    melhorMovimento = None
    melhorValor = None

    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = busca(board)
        board[possibilidade[0]][possibilidade[1]] = branco

        if(melhorValor is None):
            melhorValor = valor
            melhorMovimento = possibilidade
        else:
            if(melhorValor <= valor):
                melhorValor = valor
                melhorMovimento = possibilidade
        
    return melhorMovimento[0], melhorMovimento[1]

def getPosicoes(board):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] == branco):
                posicoes.append([i, j])
    return posicoes

def busca(board):
    contagemPossibilidadesX = 0
    contagemPossibilidadesO = 0
    resultado = 0

    # linhas 
    for i in range(3):
      resultado = fazerContagemDePossibilidades(board[i])
      contagemPossibilidadesX += resultado[0]
      contagemPossibilidadesO += resultado[1]


    # coluna
    for i in range(3):
        resultado = fazerContagemDePossibilidades([board[0][i], board[1][i], board[2][i]])
        contagemPossibilidadesX += resultado[0]
        contagemPossibilidadesO += resultado[1]

    # diagonal principal
    resultadoPrincipal = fazerContagemDePossibilidades([board[0][0], board[1][1], board[2][2]])
    contagemPossibilidadesX += resultadoPrincipal[0]
    contagemPossibilidadesO += resultadoPrincipal[1]

    # diagonal secundaria
    resultadoSecundaria = fazerContagemDePossibilidades([board[0][2], board[1][1], board[2][0]])
    contagemPossibilidadesX += resultadoSecundaria[0]
    contagemPossibilidadesO += resultadoSecundaria[1]
    
    return contagemPossibilidadesX - contagemPossibilidadesO


def fazerContagemDePossibilidades(lista):
  contagemPossibilidadesX = 0
  contagemPossibilidadesO = 0
  containsX = "X" in lista
  containsO = "O" in lista
  containsEspaco = "*" in lista

  if(containsX and not containsO):
    contagemPossibilidadesX += 1
    if(lista.count("X") == 3):
      contagemPossibilidadesX += 1
  elif(containsO and not containsX):
    contagemPossibilidadesO += 1
  elif(not containsX and not containsO and containsEspaco):
    contagemPossibilidadesX += 1
    contagemPossibilidadesO += 1
  elif(containsX and containsO and lista.count("O") == 2):
    contagemPossibilidadesX += 1
  
  return [contagemPossibilidadesX, contagemPossibilidadesO]