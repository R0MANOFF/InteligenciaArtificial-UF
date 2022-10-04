from lixeira import Lixeira
from deposito import Deposito
from random import *
import numpy as np

'''
@Descricao: Classe que implementa o espaco de busca do agente
'''
class Espaco:

    def __init__(self,modelo):
        self.modelo = modelo
        self.espaco = None
        self.tamanho = (20,20)
        self.lix1 = Lixeira((0,0))
        self.lixos = None
        self.qtdLixos= 10
        self.iteracoes = 0
    '''
    @Descricao: metodo que gera lixos no espaço de forma aleatoria
    '''

    def getLixeiras(self):
        return self.lix1

    def gerarLixos(self, ag1):
        lixos = {}
        for i in range(0,10):
            loc =tuple((randrange(0,20,2),randrange(0,20,2)))
            while(loc in lixos or loc == self.lix1.loc  or loc == ag1.loc ):
                loc =tuple((randrange(0,20,2),randrange(0,20,2)))
            lixos[loc]=randint(1,2)
        self.lixos = lixos
        
    '''
    @Descricao: metodo que gera o espaço e os lixos nele
    '''
    def gerar(self, ag1):
        self.gerarLixos(ag1)
        espaco = np.zeros(self.tamanho)
        for key in self.lixos.keys():
            espaco[key[0]][key[1]] = self.lixos[key]
        self.espaco = espaco

    '''
    @Descricao: metodo que desenha o espaço em tela
    '''
    def desenhar(self, ag1):
        print(' --------------------')
        for i in range(self.tamanho[0]):
            print('|', end="")
            for j in range(self.tamanho[1]):
                if i == ag1.loc[0] and j == ag1.loc[1]:
                    print("@", end="")
                elif self.espaco[i][j] == 1:
                    print("*", end="")
                elif self.espaco[i][j] == 2:
                    print("#", end="")
                elif self.lix1.loc[0] == i and self.lix1.loc[1] == j:
                    print("L", end="")
                else:
                    print(" ", end="")
            print('|')
        print(' --------------------')
        if self.modelo == 1:
            print("----MODELO REATIVO SIMPLES----")
        elif self.modelo == 2:
            print("----MODELO REATIVO BASEADO EM MODELOS----")
        elif self.modelo == 3:
            print("----MODELO REATIVO BASEADO EM OBJETIVO----")
        else:
            ("----MODELO REATIVO BASEADO EM UTILIDADE----")

        print("LEGENDA E OUTRAS INFORMACOES:")
        print(' -----------------------')
        print('LIXO TIPO 1 -> #')
        print('LIXO TIPO 2 -> *')
        print('QTD DE LIXOS ESPALHADOS: {}'.format(self.qtdLixos))
        print("---------------------")
        print("LIXEIRA:")
        print("          QTD TIPO 1: {}".format(self.lix1.qtdtipo1))
        print("          QTD TIPO 2: {}".format(self.lix1.qtdtipo2))
        print("---------------------")

    def atualizar(self, loc):
        self.espaco[loc[0]][loc[1]] = 0

    def estaSujo(self):
        return self.qtdLixos !=0 or self.lix1.qtdtipo1 + self.lix1.qtdtipo2 != 10

    def removeLixo(self):
        self.qtdLixos-=1
            