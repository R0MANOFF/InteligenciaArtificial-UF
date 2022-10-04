from agente import Agente, AgenteModelo, AgenteUtilidade, AgenteObjetivo
from espaco import Espaco
import os, math, time
from random import randint

SLEEP_TIME = 0.005

def reativoSimples():
    Ag1 = Agente((0,0)) #definir agente e sua localizacao
    espaco = Espaco(1) #definindo espaco e o tipo de modelo apresentado
    espaco.gerar(Ag1) #gerar espaco a ser usado 
    l1 = espaco.getLixeiras() #gerar lixeira

    Ag1.definirLixeiras(l1)

    ini = time.time() #contador tempo 
    lixeira = l1
    espaco.desenhar(Ag1)
    pegou = False
    while(espaco.estaSujo()):
        if Ag1.full == 0: #se agente esta vazio
            #preferencia por tipo
            pegou = Ag1.buscarLixo(1, espaco)
            if not pegou:
                pegou = Ag1.buscarLixo(2, espaco)
                if not pegou:
                    Ag1.MovimentaLinha()#randint(1,4))
            espaco.atualizar(Ag1.loc)
            lixeira_prox = Ag1.distanciaLixeira()
        else:
            andou = Ag1.vaiProLocal(lixeira_prox.loc)
            if not andou:
                Ag1.soltarLixo()
                lixeira_prox.receberLixo(Ag1.org)
                espaco.removeLixo()
        
        
        os.system('cls')
        espaco.desenhar(Ag1)
        time.sleep(SLEEP_TIME)
    
    fim = time.time()
    return (fim - ini)*1000

def reativoBaseadoEmModelo():
    Ag1 = AgenteModelo((0,0))
    espaco = Espaco(2)
    espaco.gerar(Ag1)
    l1 = espaco.getLixeiras()

    Ag1.definirLixeiras(l1)

    ini = time.time()
    lixeira = l1
    espaco.desenhar(Ag1)
    pegou = False
    while(espaco.estaSujo()):
        if Ag1.full == 0:
            tipo_prox_lixo, prox_lixo = Ag1.consultarMemoria()
            if prox_lixo is not None:
                andou = Ag1.vaiProLocal(prox_lixo)
                if not andou:
                    if tipo_prox_lixo != 3:
                        Ag1.pegarLixo(espaco.lixos)
                        pegou = True
                        Ag1.ultimoLixo()
                    else:
                        Ag1.removerMemoria(tipo_prox_lixo, prox_lixo)
            else:
                pegou = Ag1.buscarLixo(2, espaco)
                if not pegou:
                    pegou = Ag1.buscarLixo(1, espaco)
                    if not pegou:
                        Ag1.MovimentaLinha()
                    else:
                        Ag1.ultimoLixo()
                else:
                    Ag1.ultimoLixo()
            
            if pegou:
                espaco.atualizar(Ag1.loc)
            lixeira_prox = Ag1.distanciaLixeira()
        else:
            andou = Ag1.vaiProLocal(lixeira_prox.loc)
            if not andou:
                Ag1.soltarLixo()
                lixeira_prox.receberLixo(Ag1.org)
                espaco.removeLixo()

        Ag1.armazenarPercpcao(espaco.espaco)
        
        
        os.system('cls')
        espaco.desenhar(Ag1)
        time.sleep(SLEEP_TIME)
    
    fim = time.time()
    return (fim - ini)*1000

def reativoBaseadoEmObjetivo():
    Ag1 = AgenteObjetivo((0,0))
    espaco = Espaco(3)
    espaco.gerar(Ag1)
    l1= espaco.getLixeiras()

    Ag1.definirLixeiras(l1)

    ini = time.time()
    lixeira = l1
    espaco.desenhar(Ag1)
    pegou = False
    while(espaco.estaSujo()):
        if Ag1.full == 0:            
            pegou = Ag1.buscarLixo(2, espaco)
            if not pegou:
                pegou = Ag1.buscarLixo(1, espaco)
                if not pegou:
                    tipo_prox_lixo, prox_lixo = Ag1.consultarMemoria()
                    if prox_lixo is not None:
                        andou = Ag1.vaiProLocal(prox_lixo)
                        if not andou:
                            if tipo_prox_lixo != 3:
                                Ag1.pegarLixo(espaco.lixos)
                                pegou = True
                                Ag1.ultimoLixo()
                            else:
                                Ag1.removerMemoria(tipo_prox_lixo, prox_lixo)
                    else:
                        Ag1.proximoPasso()
                else:
                    Ag1.ultimoLixo()
            else:
                Ag1.ultimoLixo()
            
            if pegou:
                espaco.atualizar(Ag1.loc)
            lixeira_prox = Ag1.distanciaLixeira()
        else:
            andou = Ag1.vaiProLocal(lixeira_prox.loc)
            if not andou:
                Ag1.soltarLixo()
                lixeira_prox.receberLixo(Ag1.org)
                espaco.removeLixo()

        Ag1.armazenarPercpcao(espaco.espaco)
        
        
        os.system('cls')
        espaco.desenhar(Ag1)
        time.sleep(SLEEP_TIME)
    
    fim = time.time()
    return (fim - ini)*1000

def mapearMundo(Ag1, espaco):
        while(Ag1.andar(2)):
            Ag1.historico[5][0]+=1
            Ag1.armazenarPercpcao(espaco.espaco)
            os.system('cls')
            espaco.desenhar(Ag1)
            time.sleep(SLEEP_TIME)

        while(Ag1.andar(4)):
            Ag1.historico[5][1]+=1
            Ag1.armazenarPercpcao(espaco.espaco)
            os.system('cls')
            espaco.desenhar(Ag1)
            time.sleep(SLEEP_TIME)
            
        while(Ag1.andar(1)):
            Ag1.armazenarPercpcao(espaco.espaco)
            os.system('cls')
            espaco.desenhar(Ag1)
            time.sleep(SLEEP_TIME)
            
        while(Ag1.andar(3)):
            Ag1.armazenarPercpcao(espaco.espaco)
            os.system('cls')
            espaco.desenhar(Ag1)
            time.sleep(SLEEP_TIME)
            
        Ag1.lugaresDesconhecidos()  

def reativoBaseadoEmUtilidade():
    Ag1 = AgenteUtilidade((0,0))
    espaco = Espaco(4)
    espaco.gerar(Ag1)
    l1 = espaco.getLixeiras()

    Ag1.definirLixeiras(l1)

    ini = time.time()
    lixeira = l1
    espaco.desenhar(Ag1)
    
    mapearMundo(Ag1, espaco)
    pegou = False
    while(espaco.estaSujo()):
        if Ag1.full == 0:
            tipo_prox_lixo, prox_lixo = Ag1.consultarMemoria()
            if prox_lixo is not None:
                andou = Ag1.vaiProLocal(prox_lixo)
                if not andou:
                    if tipo_prox_lixo != 3:
                        Ag1.pegarLixo(espaco.lixos)
                        pegou = True
                        Ag1.ultimoLixo()
                    else:
                        Ag1.removerMemoria(tipo_prox_lixo, prox_lixo)
            else:
                pegou = Ag1.buscarLixo(1, espaco)
                if not pegou:
                    pegou = Ag1.buscarLixo(2, espaco)
                    if pegou:
                        Ag1.ultimoLixo()
                else:
                    Ag1.ultimoLixo()
            
            if pegou:
                espaco.atualizar(Ag1.loc)            
            lixeira_prox = Ag1.distanciaLixeira()
        else:
            andou = Ag1.vaiProLocal(lixeira_prox.loc)
            if not andou:
                Ag1.soltarLixo()
                lixeira_prox.receberLixo(Ag1.org)
                espaco.removeLixo()
        Ag1.armazenarPercpcao(espaco.espaco)
        
        
        os.system('cls')
        espaco.desenhar(Ag1)
        time.sleep(SLEEP_TIME)
    
    fim = time.time()
    return (fim - ini)*1000

if __name__ == "__main__":
    
    op = -1
    while(op != 0):
        print("\nDIGITE UM NUMERO:\n")
        print("1 - MODELO REATIVO SIMPLES\n2 - MODELO REATIVO BASEADO EM MODELOS\n3 - MODELO REATIVO BASEADO EM OBJETIVO\n4 - MODELO REATIVO BASEADO EM UTILIDADE")
        print('0 - SAIR')
        
        n = input()
        if(n=='1'):
            simples = reativoSimples()
            print(f'MODELO REATIVO SIMPLES: {simples:.2f} ms')
        elif(n=='2'):
            modelo = reativoBaseadoEmModelo()
            print(f'MODELO REATIVO BASEADO EM MODELOS: {modelo:.2f} ms')
        elif(n=='3'):
            objetivo = reativoBaseadoEmObjetivo()
            print(f'MODELO REATIVO BASEADO EM OBJETIVO: {objetivo:.2f} ms')
        elif(n=='4'):
            utilidade = reativoBaseadoEmUtilidade()
            print(f'MODELO REATIVO BASEADO EM UTILIDADE: {utilidade:.2f} ms')
        elif(n=='0'):
            print('Até logo')
            break
        else: 
            print("opcao invalida")
    
    
    
    '''print(f'MODELO REATIVO SIMPLES: {simples:.2f} ms')
    
    
    
    '''

