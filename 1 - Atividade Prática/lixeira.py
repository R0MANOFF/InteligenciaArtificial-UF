class Lixeira:
    def __init__(self, loc):
        self.loc= loc
        self.qtdtipo1=0 #organico
        self.qtdtipo2=0
    
    def receberLixo(self, tipo1):
        if tipo1 == 1:
            self.qtdtipo1+=1
        else:
            self.qtdtipo2+=1