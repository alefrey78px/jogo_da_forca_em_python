import random


class Palavra:
    def __init__(self):
        self.palavra = ""
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
        self.palavra = palavra_com_dica[0]
        self.dica = palavra_com_dica[1]


class Jogador:
    def __init__(self, nome):
        self.nome = nome.upper()
        self.chutes_corretos = ""
        self.chutes_incorretos = ""
        self.rodadas = 0

    def pedir_chute(self):
        while True:
            chute = input('DIGITE UMA LETRA: ').upper()
            if len(chute) != 1:
                print('INFORME APENAS UMA LETRA!')
                continue
            if chute in self.chutes_corretos or chute in self.chutes_incorretos:
                print(f'{chute}: ESSA LETRA JA FOI CHUTADA! TENTE OUTRA LETRA!')
                continue
            return chute


def animacao_enforcamento(numero_erros):
    estagios = [
        '''
        |==========|
        |          +
        |
        |
        |
        |
        |
        |________________________
        ''',
        '''
        |==========|
        |          +
        |        (```)
        |
        |
        |
        |
        |________________________
        ''',
        '''
        |==========|
        |          +
        |        (```)
        |          |
        |
        |
        |
        |________________________
        ''',
        '''
        |==========|
        |          +
        |        (```)
        |          |
        |         /
        |
        |
        |________________________
        ''',
        '''
        |==========|
        |          +
        |        (```)
        |          |
        |         / \\
        |
        |
        |________________________
        ''',
        '''
        |==========|
        |          +
        |        (```)
        |          |
        |         / \\
        |          |
        |
        |________________________
        ''',
        '''
        |==========|
        |          +
        |        (```)
        |          |
        |         / \\
        |          |
        |         /
        |________________________
        ''',
        '''
        |==========|
        |          +
        |        (```)
        |          |
        |         / \\
        |          |
        |         / \\
        |________________________
        '''
    ]
    print(estagios[numero_erros])


class Forca:
    def __init__(self, jogador, palavra_sorteada):
        self.jogador = jogador
        self.palavra_sorteada = palavra_sorteada
        self.palavra_oculta = ["_" if letra != "-" else "-" for letra in palavra_sorteada.palavra]
        self.chances = 7

    def marca_letras_corretas(self, chute):
        for indice, letra in enumerate(self.palavra_sorteada.palavra):
            if letra == chute:
                self.palavra_oculta[indice] = chute

    def verifica_letras_faltantes(self):
        return self.palavra_oculta.count("_")

    def verifica_letras_chutadas(self, chute):
        if chute in self.palavra_sorteada.palavra:
            self.jogador.chutes_corretos += chute
            return True
        else:
            self.jogador.chutes_incorretos += chute
            return False

    def encerramento(self, venceu):
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

            print(f'PARABENS {self.jogador.nome}! VOCE ACERTOU! A PALAVRA ERA: {self.palavra_sorteada.palavra}\n')
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
                f'SINTO MUITO {self.jogador.nome}, VOCE FOI ENFORCADO! A PALAVRA ERA {self.palavra_sorteada.palavra}.\n')

    def apresentacao(self):
        print(f'A PALAVRA TEM {len(self.palavra_oculta)} LETRAS. DICA: {self.palavra_sorteada.dica}')
        self.formata_palavra_oculta_para_exibicao()

    def formata_palavra_oculta_para_exibicao(self):
        print('\n')
        for letra in self.palavra_oculta:
            print('\t', letra, end='')
        print('\n')

    def estatisticas(self):
        print('ESTATISTICAS:')
        print(f'CHUTES CORRETOS..: {self.jogador.chutes_corretos}')
        print(f'CHUTES INCORRETOS: {self.jogador.chutes_incorretos}')
        print(f'NUMERO DE RODADAS: {self.jogador.rodadas}')

    def jogar(self):
        self.apresentacao()

        while self.chances > 0 and self.verifica_letras_faltantes() > 0:
            self.jogador.rodadas += 1
            chute = self.jogador.pedir_chute()
            self.marca_letras_corretas(chute)
            self.formata_palavra_oculta_para_exibicao()

            if self.verifica_letras_chutadas(chute):
                if self.verifica_letras_faltantes() == 0:
                    self.encerramento(True)
                    break
            else:
                self.chances -= 1
                animacao_enforcamento(len(self.jogador.chutes_incorretos))
                print(f'NAO TEM A LETRA {chute}! VOCE TEM MAIS {self.chances} CHANCES!')

            if self.chances == 0:
                self.encerramento(False)

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
        nome_jogador = input('DIGITE SEU NOME: ')
        jogador = Jogador(nome_jogador)
        palavra_sorteada = Palavra()
        palavra_sorteada.sortear_palavra()
        jogo = Forca(jogador, palavra_sorteada)
        jogo.jogar()
    else:
        print('SELECIONE UMA OPCAO VALIDA, J PARA JOGAR OU S PARA SAIR!')
