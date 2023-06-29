import random
from matplotlib import pyplot as plt

def main(n):

    def progress(i,end,part):
        if part==1:
            print((i*100/end)/2,"%")
        elif part==2:
            print((i*100/end)/2+50,"%")

    def conf(e):

        def porta_certa_escolhida_aberta(): # 1°Porta Certa ; 2°Porta Escolhida ; 3°Porta Aberta
            portas=[]
            while len(portas)<2:
                portas.append(random.randint(1,3))

            i=0
            while i==0:
                x=random.randint(1,3)
                if x!=portas[0] and x!=portas[1]:
                    i=1
            portas.append(x)
            return portas
        portas=porta_certa_escolhida_aberta()

        def decisao(e):
            if e==1:
                for x in range(1,4):
                    if x!=portas[1] and x!=portas[2]:
                        return x
            if e==0:
                return portas[1]

        portas[1]=decisao(e)

        return portas

    def jogo(e): # (0) -> Errou a Porta ; (1) -> Acertou a Porta

        portas=conf(e)
        if portas[1]==portas[0]:
            return 1
        else:
            return 0

    def iterar_tentativas(e,n):
        i=0
        marcos=[]
        while i<n:
            marcos.append(jogo(e))
            if e==0:
                progress(i,n,1)
            elif e==1:
                progress(i,n,2)
            i+=1
        return marcos

    def contar_vitorias(e,n):
        i=0
        for x in iterar_tentativas(e,n):
            if x==1:
                i+=1
        return i*100/n

    def gerar_graficos(valor1, valor2, n):
        valores = [valor1, valor2]
        labels = ['Não Trocou de Porta', 'Trocou de Porta']
        cores = ['blue', 'red']
        
        ylab='Percentual de Vitórias (',str(n),' iterações)'
        plt.bar(labels, valores, color=cores)
        plt.xlabel('Escolha do Jogador')
        plt.ylabel(ylab)
        plt.title('Paradoxo de Monty Hall')
        
        for i, v in enumerate(valores):
            plt.text(i, v + 0.5, str(v), ha='center', va='bottom')
        
        plt.show()

    gerar_graficos(contar_vitorias(0,n),contar_vitorias(1,n),n)

main(100000)