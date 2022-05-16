# jogo da forca
# versao 0.2
# 15/05/2022
# Autor: Alexandre Frey

# uso da biblioteca random para efetuar o sorteio da palavra e dica a ser jogada
import random


# Inicio da função sorteio_da_palavra
# Essa função serve para a partir de um arquivo denominado "palavras.txt"
# obter a palavra a ser advinhada e a respectiva dica para a palavra.
def sorteio_da_palavra(palavra, dica):
    lista_de_palavras = []  # irá receber a lista com as palavras do arquivo
    try:  # para tratar erro caso o arquivo nao exista
        with open('palavras.txt', 'r') as arquivo:
            for linha in arquivo:  # para cada linha do arquivo
                linha = linha.strip()
                lista_de_palavras.append(linha)  # adiciona a linha na lista de palavras
    except:  # mostra erro e encerra o programa
        print('ERRO AO ABRIR O ARQUIVO PALAVRAS.TXT! VERIFIQUE SE ELE EXISTE!')
        quit()

    # faz o sorteio de um item da lista de palavras:dicas, convertendo para
    # letras MAIUSCULAS e separando em duas strings usando como separador os
    # dois pontos (:), onde a primeira é a palavra e a segunda a dica
    palavra_e_dica = random.choice(lista_de_palavras).upper().split(':')

    # preenche as strings palavra e dica com as respectivas informações
    palavra = palavra_e_dica[0]  # palavra recebe a primeira parte da string (palavra)
    dica = palavra_e_dica[1]  # dica recebe a segunda parte da string (dica)
    return palavra, dica  # retorna as variaveis palavra e dica
# Final da função sorteio_da_palavra


# Início da função marca_letras_corretas
# Essa função marca as letras que o jogador acertou na palavra_oculta
def marca_letras_corretas(palavra, chute, palavra_oculta):
    indice = 0
    for letra in palavra:
        if letra in chute:
            palavra_oculta[indice] = chute
        indice += 1
    return palavra_oculta
# Final da função marca_letras_corretas


# Início da função verifica_letras_faltantes
# Essa função retorna quantas letras faltam para completar a palavra,
# baseado em quantos "_" ainda tem na palavra mascarada (palavra_oculta)
def verifica_letras_faltantes(palavra_oculta):
    letras_faltando = 0
    for underscore in palavra_oculta:
        if underscore == '_':
            letras_faltando += 1
    return letras_faltando
# Final da função verifica_letras_faltantes


# Início da função verifica_letras_chutadas
# Essa função serve para verificar se o chute está na palavra_oculta ou não,
# adicionando conforme o caso a letra chutada na variável chutes_corretos ou
# chutes_incorretos.
# Também muda para True o estado da variável acertou_chute caso seja o caso
def verifica_letras_chutadas(chute, palavra_oculta, chutes_corretos, chutes_incorretos):
    if chute not in palavra_oculta:
        chutes_incorretos += chute
        acertou_chute = False
    elif chute in palavra_oculta:
        chutes_corretos += chute
        acertou_chute = True
    return chutes_corretos, chutes_incorretos, acertou_chute
# Final da função verifica_letras_chutadas


# Início da função pedir_chute
# Essa função pede uma letra (chute) e verifica se a letra já foi chutada,
# com base no conteúdo das variáveis chutes_corretos e chutes_incorretos.
# Se já foi pede novamente a letra. Se não retorna a letra "chutada".
# Essa funão também tem um segundo laço de while, o qual serve para prevenir
# que o jogador informe mais de uma letra por vez. caso o faça o programa mostra
# erro e pede novamente que se digite apenas uma letra.
def pedir_chute(chutes_corretos, chutes_incorretos):
    while True:
        while True:
            chute = input('DIGITE UMA LETRA: ')
            chute = chute.upper()  # garante que a letra chutada fique e MAIUSCULA para evitar erros

            if len(chute) > 1:  # se informar mais de uma letra por vez
                print('INFORME APENAS UMA LETRA!')  # exibe erro
                continue  # retorna o inicio do segundo while
            else:  # senao
                break  # encerra o segundo while

        if chute in chutes_corretos:  # se a letra chutada ja foi chutada (e acertada)
            print('{}: ESSA LETRA JÁ FOI CHUTADA E ACERTADA! TENTE OUTRA LETRA!'.format(chute))
            continue  # retorna ao inicio do primeiro while
        if chute in chutes_incorretos:  # se a letra chutada ja foi chutada (e errada)
            print('{}: ESSA LETRA JÁ FOI CHUTADA E ERRADA! TENTE OUTRA LETRA!'.format(chute))
            continue  # retorna o inicio do primeiro while
        else:  # senao (letra ainda nao foi chutada)
            break  # encerra o primeiro while
    return chute  # retorna a letra chutada
# Final da função pedir_chute


# Início da função animacao_enforcamento
# Essa função vai desenhando o enforcamento do personagem.
# Ela recebe um parâmetro (numero_erros) que atrávez dos "ifs"
# desenha os diferentes níveis (7) de "enforcamento"
def animacao_enforcamento(numero_erros):
    print('\n|==========|\n'
          '|          +  ')
    if numero_erros == 1:
        print('|        (```)')
    if numero_erros == 2:
        print('|        (```)\n'
              '|          |    ')
    if numero_erros == 3:
        print('|        (```)\n'
              '|          |  \n'
              '|         /     ')
    if numero_erros == 4:
        print('|        (```)\n'
              '|          |  \n'
              '|         / \\  ')
    if numero_erros == 5:
        print('|        (```)\n'
              '|          |  \n'
              '|         / \\\n'
              '|          |    ')
    if numero_erros == 6:
        print('|        (```)\n'
              '|          |  \n'
              '|         / \\\n'
              '|          |  \n'
              '|         /     ')
    if numero_erros == 7:
        print('|        (```)\n'
              '|          |  \n'
              '|         / \\\n'
              '|          |  \n'
              '|         / \\  ')
    print('|\n'
          '|________________________\n')
# Fim da função animacao_enforcamento


# Início da funçao encerramento serve para exibir um trofeu em caso de vitoria
# ou uma caveira em caso de derrota
def encerramento(nome_jogador, palavra, venceu):
    # Se venceu é True então venceu...
    if venceu:
        print('''
             _________________
           /|                 |\\
          / |                 | \\
         |  |    VENCEDOR!    |  | 
          \ |                 | /
            |                 |
            \                 /
             \               /
              \             /
               \           /
               /           \\
              /             \\
             |_______________|\n''')
        print('PARABÉNS {}! VOCÊ ACERTOU! A PALAVRA ERA: {}\n'.format(nome_jogador, palavra))

    # Se venceu é False então perdeu...
    if not venceu:
        print('''
          _____
         /     \\
        | () () |
         \  ^  /
          |||||
          |||||\n''')
        print('SINTO MUITO {}, VOCÊ FOI ENFORCADO! A PALAVRA ERA {}.\n'.format(nome_jogador, palavra))
# Final da função encerramento


# Inicio da função apresentacao
# Essa função imprime o cabeçalho do jogo
def apresentacao(nome, dica, palavra_oculta):
    print('A PALAVRA TEM {} LETRAS. DICA: {}'.format(len(palavra_oculta), dica))
    formata_palavra_oculta_para_exibicao(palavra_oculta)
# Final da função apresentacao


# Início da função formata_palavra_oculta_para_exibicao
# Essa função imprime na tela a palavra_oculta de uma forma mais
# agradável de visualizar, se apenas fizer print de palavra_oculta
# irá ficar algo assim (ex. palavra SOL):
# ['S','O','L']
# Com essa função o mesmo exemplo ficaria mais ou menos assim:
#   S   O   L
def formata_palavra_oculta_para_exibicao(palavra_oculta):
    print('\n')
    for i in range(len(palavra_oculta)):
        print('\t', palavra_oculta[i], end='')
    print('\n')
# Final da função formata_palavra_oculta_para_exibicao


# Inicio da função estatisticas
# Mostra algumas estatisticas da rodada
def estatisticas(chutes_corretos, chutes_incorretos, rodadas):
    print('ESTATÍSTICAS:')
    print('CHUTES CORRETOS..: {}'.format(chutes_corretos))
    print('CHUTES INCORRETOS: {}'.format(chutes_incorretos))
    print('NUMERO DE RODADAS: {}'.format(rodadas))
# Final da função estatisticas


# Iníco da função jogando. Contém a mecânica de jogo, chama várias funções
def jogando(nome_jogador):
    # Variaveis locais necessarias para funcionamento do jogo
    palavra = ''  # armazena a palavra sorteada
    dica = ''  # dica armazena respectiva dica da palavra sorteada
    palavra_oculta = []  # para representação da variavel palavra escondendo as letras
    chutes_corretos = ''  # armazena os chutes corretos (letras que tem na palavra)
    chutes_incorretos = ''  # armazena os chutes incorretos (letras que *não tem* na palavra)
    chances = 7  # são 7 erros até enforcar o boneco:
    # (cabeça, pescoço, braço, outro braço, tronco, perna e outra perna)
    acertou_chute = False  # a cada rodada precisamos ver se acertou ou não o chute
    rodadas = 0  # apenas para estatísticas de quantas rodadas no final da jogada

    # Chama função para sorteio da palavra e respectiva dica
    # recebendo a seguir o retorno com a palavra e dica
    palavra, dica = sorteio_da_palavra(palavra, dica)

    # Preenche palavra_oculta com um "underscore" (_) para cada letra da palavra
    # A lista palavra_oculta serve para exibir na tela a palavra de forma "camuflada"
    for i in palavra:
        palavra_oculta.append('_')

    # chama função que imprime a tela inicial da rodada
    apresentacao(nome_jogador, dica, palavra_oculta)

    # Até aqui *nessa função* (jogando) as instruções são executadas apenas 1 (uma)
    # vez *por partida*. A seguir precisamos de um laço de repetição porque se faz
    # necessária a repetição das instruções para que o jogo funcione.
    # Para tal vamos utilizar while True com break quando for necessário encerrar.
    while True:  # pode ser while True porque vamos usar break para parar quando necessário

        rodadas += 1  # incrementa váriavel conforme vai jogando

        # Chama a função que pede o chute da letra
        chute = pedir_chute(chutes_corretos, chutes_incorretos)

        # Chama a função que marca o(s) chute(s) correto(s)
        palavra_oculta = marca_letras_corretas(palavra, chute, palavra_oculta)

        # Chama função que exibe a palavra_oculta na tela
        formata_palavra_oculta_para_exibicao(palavra_oculta)

        # Chama função que verifica se o chute está na palavra oculta
        chutes_corretos, chutes_incorretos, acertou_chute = \
            verifica_letras_chutadas(chute, palavra_oculta, chutes_corretos, chutes_incorretos)

        # Chama a função que verifica se ainda faltam acertar letras na palavra
        if not verifica_letras_faltantes(palavra_oculta):  # se não faltam letras venceu...
            encerramento(nome_jogador, palavra, True)  # encerramento com True mostra o troféu
            break

        # se não acertou o chute
        if not acertou_chute:
            chances = 7 - (len(chutes_incorretos))  # diminui as chances
            animacao_enforcamento(len(chutes_incorretos))  # vai enforcando
            print('NÃO TEM A LETRA {}! VOCÊ TEM MAIS {} CHANCES!'.format(chute, chances))
            if chances:  # se ainda tem chances exibe novamente a palavra_oculta
                formata_palavra_oculta_para_exibicao(palavra_oculta)
            if not chances:  # se não tem chances.
                encerramento(nome_jogador, palavra, False)  # encerramento() com False mostra caveira :((((
                break  # fim de jogo

    # Mostra algumas estatísticas
    estatisticas(chutes_corretos, chutes_incorretos, rodadas)
# Final da função jogando


# Início do programa principal
print('\n***** BEM VINDO(A) AO JOGO DA FORCA! *****')

while True:
    print('\n***** MENU PRINCIPAL *****\n'
          'ESCOLHA UMA OPÇÃO:\n'
          'J. JOGAR\n'
          'S. SAIR')

    opcao = input('>> ')

    if opcao in ['s', 'S']:
        print('SAINDO DO JOGO...')
        break
    elif opcao in ['j', 'J']:
        nome_jogador = input('DIGITE SEU NOME: ')  # pede o nome do jogador(a)
        nome_jogador = nome_jogador.upper()  # coloca o nome em letra MAIUSCULA
        print('BOA SORTE {}!'.format(nome_jogador))
        jogando(nome_jogador)  # chama a função jogando para iniciar o jogo
    else:
        print('SELECIONE UMA OPÇÃO VÁLIDA, J PARA JOGAR OU S PARA SAIR!')
        continue
# Fim do programa
