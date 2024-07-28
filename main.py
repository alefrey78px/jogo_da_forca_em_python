import random


class Palavra:
    def __init__(self):
        self.palavra_selecionada = ""
        self.dica = ""

    def sortear_palavra(self):
        lista_de_palavras = []
        try:
            with open('palavras.txt', 'r') as arquivo:
                for linha in arquivo:
                    linha = linha.strip()
                    lista_de_palavras.append(linha)
        except FileNotFoundError:
            print('ERRO AO ABRIR O ARQUIVO PALAVRAS.TXT! VERIFIQUE SE ELE EXISTE!')
            quit()

        palavra_com_dica = random.choice(lista_de_palavras).upper().split(':')
        self.palavra_selecionada = palavra_com_dica[0]
        self.dica = palavra_com_dica[1]


class Jogador:
    def __init__(self, nome):
        self.nome = nome.upper()
        self.letras_corretas = ""
        self.letras_incorretas = ""
        self.rodadas = 0

    def pedir_chute(self):
        while True:
            chute = input('DIGITE UMA LETRA: ').upper()
            if len(chute) != 1:
                print('INFORME APENAS UMA LETRA!')
                continue
            if chute in self.letras_corretas or chute in self.letras_incorretas:
                print(f'{chute}: ESSA LETRA JA FOI CHUTADA! TENTE OUTRA LETRA!')
                continue
            return chute


class Forca:
    def __init__(self, jogador_atual, palavra_atual):
        self.jogador = jogador_atual
        self.palavra = palavra_atual
        self.palavra_oculta = ["_" if letra != "-" else "-" for letra in palavra_atual.palavra_selecionada]
        self.chances = 7

    def marca_letras_corretas(self, chute):
        for indice, letra in enumerate(self.palavra.palavra_selecionada):
            if letra == chute:
                self.palavra_oculta[indice] = chute

    def conta_letras_faltantes(self):
        return self.palavra_oculta.count("_")

    def verifica_letras_chutadas(self, chute):
        if chute in self.palavra.palavra_selecionada:
            self.jogador.letras_corretas += chute
            return True
        else:
            self.jogador.letras_incorretas += chute
            return False

    @staticmethod
    def mostrar_animacao_enforcamento(numero_erros):
        estagios = [
            r'''
            |==========|
            |          +
            |
            |
            |
            |
            |
            |________________________
            ''',
            r'''
            |==========|
            |          +
            |        (```)
            |
            |
            |
            |
            |________________________
            ''',
            r'''
            |==========|
            |          +
            |        (```)
            |          |
            |
            |
            |
            |________________________
            ''',
            r'''
            |==========|
            |          +
            |        (```)
            |          |
            |         /
            |
            |
            |________________________
            ''',
            r'''
            |==========|
            |          +
            |        (```)
            |          |
            |         / \
            |
            |
            |________________________
            ''',
            r'''
            |==========|
            |          +
            |        (```)
            |          |
            |         / \
            |          |
            |
            |________________________
            ''',
            r'''
            |==========|
            |          +
            |        (```)
            |          |
            |         / \
            |          |
            |         /
            |________________________
            ''',
            r'''
            |==========|
            |          +
            |        (```)
            |          |
            |         / \
            |          |
            |         / \
            |________________________
            '''
        ]
        print(estagios[numero_erros])

    def mostrar_encerramento(self, venceu):
        if venceu:
            print(r'''
             _________________
           /|                 |\
          / |                 | \
         |  |    VENCEDOR!    |  | 
          \ |                 | /
           \|                 |/
            \                 /
             \               /
              \             /
               \           /
               /           \
              /             \
             |_______________|
                  ''')

            print(f'PARABENS {self.jogador.nome}! VOCE ACERTOU! A PALAVRA ERA: {self.palavra.palavra_selecionada}\n')
        else:
            print(r'''
                          _____
                        /       \
                       /         \
                      /  _     _  \
                     |  | |   | |  |
                     |  |_|   |_|  |
                     |     / \     |
                     |    /_ _\    |
                      \           /
                       \         /
                        \       /
                         \_____/
                          |||||
                          |||||
                          |||||
                          |||||
            ''')

            print(
                f'SINTO MUITO {self.jogador.nome},'
                f' VOCE FOI ENFORCADO! A PALAVRA ERA {self.palavra.palavra_selecionada}.\n')

    def mostrar_apresentacao(self):
        print(f'A PALAVRA TEM {len(self.palavra_oculta)} LETRAS. DICA: {self.palavra.dica}')
        self.mostrar_palavra()

    def mostrar_palavra(self):
        print('\n')
        for letra in self.palavra_oculta:
            print('\t', letra, end='')
        print('\n')

    def estatisticas(self):
        print('ESTATISTICAS:')
        print(f'CHUTES CORRETOS..: {self.jogador.letras_corretas}')
        print(f'CHUTES INCORRETOS: {self.jogador.letras_incorretas}')
        print(f'NUMERO DE RODADAS: {self.jogador.rodadas}')

    def jogar(self):
        self.mostrar_apresentacao()

        while self.chances > 0 and self.conta_letras_faltantes() > 0:
            self.jogador.rodadas += 1
            chute = self.jogador.pedir_chute()
            self.marca_letras_corretas(chute)
            self.mostrar_palavra()

            if self.verifica_letras_chutadas(chute):
                if self.conta_letras_faltantes() == 0:
                    self.mostrar_encerramento(True)
                    break
            else:
                self.chances -= 1
                self.mostrar_animacao_enforcamento(len(self.jogador.letras_incorretas))
                print(f'NAO TEM A LETRA {chute}! VOCE TEM MAIS {self.chances} CHANCES!')

            if self.chances == 0:
                self.mostrar_encerramento(False)

        self.estatisticas()


# Início do programa principal
print('\n***** BEM VINDO(A) AO JOGO DA FORCA! *****')

while True:
    print('\n***** MENU PRINCIPAL *****\n'
          'ESCOLHA UMA OPCAO:\n'
          'J. JOGAR\n'
          'S. SAIR')

    opcao = input('>> ')

    if opcao.lower() == 's':
        print('SAINDO DO JOGO...')
        break
    elif opcao.lower() == 'j':
        # pede o nome do jogador
        nome_jogador = input('DIGITE SEU NOME: ')

        # instancia a classe Jogador passando o nome digitado
        jogador = Jogador(nome_jogador)

        # instancia a classe Palavra e aciona o metodo que sorteia a palavra
        palavra = Palavra()
        palavra.sortear_palavra()

        # instancia a classe Forca passando nome do jogador, palavra sorteada
        # e aciona o metodo jogar da mesma classe que contem a mecanica do jogo
        jogo = Forca(jogador, palavra)
        jogo.jogar()
    else:
        print('SELECIONE UMA OPCAO VALIDA, J PARA JOGAR OU S PARA SAIR!')
