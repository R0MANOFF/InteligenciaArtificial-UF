import math
from random import randint

'''
@Descricao: Classe que implementa os agentes
'''
class Agente:

    def __init__(self, loc):
        self.loc = loc
        self.full = 0
        self.org = 0
        self.sentido = "direita"

    def definirLixeiras(self, lix1):
        self.lix1 = lix1
        
                    
                    
    def MovimentaLinha(self):
        if(self.sentido == 'direita'):
            if self.loc[1]<19:
               self.loc = (self.loc[0],self.loc[1] + 1)
            else:
                if self.loc[0]<19:
                    self.loc = (self.loc[0] + 1,self.loc[1])
                self.sentido = "esquerda"
        elif(self.sentido == "esquerda"):
            if self.loc[1]>0:
                self.loc = (self.loc[0],self.loc[1] - 1)
            else:
                if self.loc[0]<19:
                    self.loc = (self.loc[0] + 1,self.loc[1])
                self.sentido = "direita"   
            
             
            

    def andar(self,direção):
        self.last_move= direção
        if direção ==1:
            if self.loc[0]>0:
               self.loc = (self.loc[0] - 1,self.loc[1])
               return True
        if direção == 2: #baixo
            if self.loc[0]<19:
               self.loc = (self.loc[0] + 1,self.loc[1])
               return True
        if direção == 3:
            if self.loc[1]>0:
               self.loc = (self.loc[0],self.loc[1] - 1)
               return True
        if direção == 4: #direita
            if self.loc[1]<19:
               self.loc = (self.loc[0],self.loc[1] + 1)
               return True
        return False
    
    def pegarLixo(self, lixo):
        self.full = 1
        if lixo == 1:
            self.org = 1
        else:
            self.org = 0

    def soltarLixo(self):
        self.full = 0
    
    def distanciaLixeira(self):
        d1 = math.sqrt((self.loc[0] - self.lix1.loc[0])**2 + (self.loc[1] - self.lix1.loc[1])**2)
        return self.lix1
       
    
    def vaiProLocal(self, loc):
        andou = False
        if self.loc[1] > loc[1]:
            andou = self.andar(3)
        elif self.loc[1] < loc[1]:
            andou = self.andar(4)
        elif self.loc[0] < loc[0]:
            andou = self.andar(2)
        elif self.loc[0] > loc[0]:
            andou = self.andar(1)
        
        return andou
    
    def buscarLixo(self, tipo, espaco):
        pegouLixo = False
        if self.loc[0]-1>= 0 and espaco.espaco[self.loc[0]-1][self.loc[1]] == tipo:
            self.andar(1)
            self.pegarLixo(espaco.lixos[self.loc])
            pegouLixo = True
        elif self.loc[0] + 1 <19 and espaco.espaco[self.loc[0] + 1][self.loc[1]] == tipo:
            self.andar(2)
            self.pegarLixo(espaco.lixos[self.loc])
            pegouLixo = True
        elif self.loc[1]-1>=0 and espaco.espaco[self.loc[0]][self.loc[1]-1] == tipo:
            self.andar(3)
            self.pegarLixo(espaco.lixos[self.loc])
            pegouLixo = True
        elif self.loc[1]+1< 19 and espaco.espaco[self.loc[0]][self.loc[1]+1] == tipo:
            self.andar(4)
            self.pegarLixo(espaco.lixos[self.loc])
            pegouLixo = True
        return pegouLixo

    def trocarLixeira(self, lixeira):
        return self.lix1
    
class AgenteModelo(Agente):

    def __init__(self, loc):
        super().__init__(loc)
        self.historico = {0:[], 1:[], 2:[], 3:[]}
        # 0: limpo
        # 1: organico
        # 2: reciclavel
        # 3: local último lixo

    def buscarLixo(self, tipo, espaco):
        pegouLixo = False
        if self.loc[0]-1>= 0 and espaco.espaco[self.loc[0]-1][self.loc[1]] == tipo:
            self.andar(1)
            self.pegarLixo(espaco.lixos)
            pegouLixo = True
        elif self.loc[0] + 1 <19 and espaco.espaco[self.loc[0] + 1][self.loc[1]] == tipo:
            self.andar(2)
            self.pegarLixo(espaco.lixos)
            pegouLixo = True
        elif self.loc[1]-1>=0 and espaco.espaco[self.loc[0]][self.loc[1]-1] == tipo:
            self.andar(3)
            self.pegarLixo(espaco.lixos)
            pegouLixo = True
        elif self.loc[1]+1< 19 and espaco.espaco[self.loc[0]][self.loc[1]+1] == tipo:
            self.andar(4)
            self.pegarLixo(espaco.lixos)
            pegouLixo = True
        return pegouLixo

    def armazenarPercpcao(self, espaco):
        loc_u = self.validPos(self.loc[0]-1, self.loc[1])
        loc_d = self.validPos(self.loc[0]+1, self.loc[1])
        loc_l = self.validPos(self.loc[0], self.loc[1]-1)
        loc_r = self.validPos(self.loc[0], self.loc[1]+1)

        percp_c = espaco[self.loc[0]][self.loc[1]]
        percp_u = espaco[loc_u[0]][loc_u[1]]
        percp_d = espaco[loc_d[0]][loc_d[1]]
        percp_l = espaco[loc_l[0]][loc_l[1]]
        percp_r = espaco[loc_r[0]][loc_r[1]]

        if self.loc not in self.historico[percp_c]:
            self.historico[percp_c].append(self.loc)

        if loc_u not in self.historico[percp_u]:
            self.historico[percp_u].append(loc_u)

        if loc_d not in self.historico[percp_d]:
            self.historico[percp_d].append(loc_d)

        if loc_l not in self.historico[percp_l]:
            self.historico[percp_l].append(loc_l)

        if loc_r not in self.historico[percp_r]:
            self.historico[percp_r].append(loc_r)

    def ultimoLixo(self):
        self.historico[3].append(self.loc)

    def validPos(self, loc_y, loc_x):
        if loc_y < 0:
            loc_y = 0
        elif loc_y > 19:
            loc_y = 19
        if loc_x < 0:
            loc_x = 0
        elif loc_x > 19:
            loc_x = 19
        
        return (loc_y, loc_x)
    
    def buscarLixoMemoria(self, tipo_lixo, id_lixo=0):
        if self.historico[tipo_lixo]:
            return self.historico[tipo_lixo][id_lixo]
        return None
    
    def consultarMemoria(self):
        if self.historico[2]:
            return 2, self.historico[2][0]
        
        if self.historico[1]:
            return 1, self.historico[1][0]

        if self.historico[3]:
            local = self.historico[3][-1]
            return 3, local
        
        return None, None
    
    def pegarLixo(self, lixos):
        lixo = lixos[self.loc]
        self.full = 1
        if lixo == 1:
            self.org = 1
        else:
            self.org = 0
        self.removerMemoria(lixo, self.loc)

    def removerMemoria(self, tipo, mem):
        index = self.historico[tipo].index(mem)
        self.historico[tipo].pop(index)

class AgenteObjetivo(AgenteModelo):
    
    def __init__(self, loc):
        super().__init__(loc)
    
    def proximoPasso(self):
        if (self.loc[0]-1,self.loc[1]) not in self.historico[0] and self.loc[0]>0:
                self.andar(1)
        elif (self.loc[0]+1,self.loc[1]) not in self.historico[0] and self.loc[0]<19:
                self.andar(2)
        elif (self.loc[0],self.loc[1]-1) not in self.historico[0] and self.loc[1]>0:
                self.andar(3)
        elif (self.loc[0],self.loc[1]+1) not in self.historico[0] and self.loc[1]<19:
                self.andar(4)
        else:
            movimento = randint(1,4)
            while movimento == 1 and self.last_move ==2 or movimento==2 and self.last_move ==1 or movimento == 3 and self.last_move ==4 or movimento==4 and self.last_move ==3:
                movimento = randint(1,4)
            self.andar(movimento)

class AgenteUtilidade(AgenteModelo):

    def __init__(self, loc):
        super().__init__(loc)
        self.historico = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[0, 0]}
        # 0: limpo
        # 1: organico
        # 2: reciclavel
        # 3: local último lixo
        # 4: locais n mapeados
        # 5: bordas do mundo

    def armazenarPercpcao(self, espaco):
        loc_u = self.validPos(self.loc[0]-1, self.loc[1])
        loc_d = self.validPos(self.loc[0]+1, self.loc[1])
        loc_l = self.validPos(self.loc[0], self.loc[1]-1)
        loc_r = self.validPos(self.loc[0], self.loc[1]+1)

        percp_c = espaco[self.loc[0]][self.loc[1]]
        percp_u = espaco[loc_u[0]][loc_u[1]]
        percp_d = espaco[loc_d[0]][loc_d[1]]
        percp_l = espaco[loc_l[0]][loc_l[1]]
        percp_r = espaco[loc_r[0]][loc_r[1]]

        if self.loc not in self.historico[percp_c]:
            self.historico[percp_c].append(self.loc)

        if loc_u not in self.historico[percp_u]:
            self.historico[percp_u].append(loc_u)

        if loc_d not in self.historico[percp_d]:
            self.historico[percp_d].append(loc_d)

        if loc_l not in self.historico[percp_l]:
            self.historico[percp_l].append(loc_l)

        if loc_r not in self.historico[percp_r]:
            self.historico[percp_r].append(loc_r)
        
        self.atualizaDesconhecido(self.loc)
        self.atualizaDesconhecido(loc_u)
        self.atualizaDesconhecido(loc_d)
        self.atualizaDesconhecido(loc_l)
        self.atualizaDesconhecido(loc_r)
    
    def lugaresDesconhecidos(self):
        max_x = self.historico[5][1]+1
        max_y = self.historico[5][0]+1

        for i in range(max_y):
            for j in range(max_x):
                loc = (i, j)
                if not (loc in self.historico[0] or loc in self.historico[1] or loc in self.historico[2]):
                    self.historico[4].append(loc)
    
    def atualizaDesconhecido(self, loc):
        if len(self.historico[4]) > 0:
            if loc in self.historico[4]:
                self.historico[4].remove(loc)
    
    def consultarMemoria(self):
        l_id, tipo = self.lixoMaisProximo()
        if l_id is not None:
            return tipo, self.historico[tipo][l_id]

        if self.historico[3]:
            return 3, self.historico[3][-1]
        
        if self.historico[4]:
            return 4, self.historico[4][0]

        return None, None

    def lixoMaisProximo(self):
        dists_r = []
        dists_o = []

        i = None
        tipo = None
        min_r = None
        min_o = None

        if len(self.historico[2]) != 0:
            for l_r in self.historico[2]:
                dists_r.append(math.sqrt((self.loc[0] - l_r[0])**2 + (self.loc[1] - l_r[1])**2))
        
        if len(self.historico[1]) != 0:
            for l_o in self.historico[1]:
                dists_o.append(math.sqrt((self.loc[0] - l_o[0])**2 + (self.loc[1] - l_o[1])**2))
        
        if len(dists_r) != 0: 
            min_r = min(dists_r)
        
        if len(dists_o) != 0:
            min_o = min(dists_o)

        if min_r is not None:
            i = dists_r.index(min_r)
            tipo = 2
        elif min_o is not None:
            i = dists_o.index(min_o)
            tipo = 1
                
        return i, tipo


