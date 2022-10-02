from grafo.aresta import Aresta
from copy import deepcopy
import time
class Grafo(object):
    def __init__(self):
        self.li = []

    def insere_vertice(self):
        self.li.append([])

    def insere_aresta(self, x, y, peso):
        arestax = Aresta(y, peso)
        arestay = Aresta(x, peso)
        self.li[x].append(arestax)
        self.li[y].append(arestay)

    def remove_aresta(self, x, y):
        for val in self.li[x]:
            if val.x == y:
                self.li[x].remove(val)
                break
        for val in self.li[y]:
            if val.x == x:
                self.li[y].remove(val)
                break

    def remove_vertice(self, vertice):
        for i in range(len(self.li)):
            if self.li[i] != None:
                for v in self.li[i]:
                    if v.x == vertice:
                        self.li[i].remove(v)
        self.li[vertice] = None

    def print_grafo(self):
        for i in range(len(self.li)):
            if(self.li[i] != None):
                print(str(i) + " -> "),
                for j in range(len(self.li[i])):
                    print(str(self.li[i][j].x) + " -> "),
                print("NULL")

    def BN(self, vi):
        H = []
        H.append(vi)
        ini = vi
        while len(H) < len(self.li): #enquanto o ciclo hamiltoniano nao atingir o limite superior
            min = float('inf')
            ar = None
            for aresta in self.li[vi]: #ache a aresta de menor custo
                if aresta.peso < min and aresta.x not in H:
                    min = aresta.peso
                    ar = aresta
            vi = ar.x #atualize o vertice atual pelo vertice dessa aresta
            H.append(vi) #insira no ciclo hamiltoniano

        H.append(ini)
        print("ciclo hamiltoniano: " + str(H))
        return H

    def TA(self, vi):
        aux = deepcopy(self)
        H = []
        T = aux.prim(vi) #gerando a MST
        T.dobra_arestas() #dobrando as arestas da MST
        L = T.hierholzer(T, vi)  #achando ciclo euleriano na MST
        self.TW(H, L) #enviando os resultados para o operador TW(.)
        return H

    def christofides(self, vi):
        aux = deepcopy(self)
        H = []
        T = aux.prim(vi)  #gerando a MST
        E = aux.matching_perfeito(T)  #matching perfeito na MST
        L = T.hierholzer(T, vi)  #achando ciclo euleriano na MST
        self.TW(H, L) #enviando os resultados para o operador TW(.)
        return H

    def TW(self, H, L):
        k=0
        while k < len(L): #criando o cilo hamiltoniano a partir do ciclo euleriano sequencialmente
            if L[k] not in H:
                H.append(L[k])
            k+=1
        H.append(H[0])
        print("ciclo hamiltoniano: "+ str(H))

    def hierholzer(self, grafo, vi):
        curr_path = [Aresta(vi, 0)]  # caminho atual
        circuit = []  #ciclo euleriano
        while curr_path:  #enquanto ainda existir um caminho, ou seja, o grafo nao esteja vazio
            curr_v = curr_path[-1]   #atualize o vertice atual
            if grafo.li[curr_v.x]:
                next_v = grafo.li[curr_v.x].pop() #escolha o proximo vertice e remova o caminho entre ele e o vertice atual
                grafo.remove_aresta(curr_v.x, next_v.x)
                curr_path.append(next_v)
            else:
                circuit.append(curr_path.pop())
        #ciclo euleriano pronto
        L = []
        for i in range(len(circuit) - 1, -1, -1):  #transferindo o ciclo para o vetor L
            L.append(circuit[i].x)
        #print("ciclo euleriano = " + str(L))
        return L

    def prim(self, i):
        T = [] #conjunto dos vertices selecionados
        T.append(i)
        N = [] #conjunto dos vertices ainda nao selecionados
        for j in range(len(self.li)):
            N.append(j)
        N.remove(i)
        Tmin = [] #conjunto de arestas da arvore minima
        n = len(N)
        while len(T) != n + 1: #enquanto T nao atingir o limite superior, ache a aresta de menor custo, insira o novo vertice em T e remova de N
            min = float("inf")
            aresta = {}
            for j in T: #achando a aresta esta de menor custo
                for k in N:
                    try:
                        for ar in self.li[j]:
                            if ar.x == k and ar.peso < min:
                                min = ar.peso
                                aresta = {'x': j, 'y': k, 'peso': ar.peso}
                    except:
                        pass
            T.append(aresta['y'])
            N.remove(aresta['y'])
            Tmin.append(aresta)

        saida = Grafo()  #construindo a saida com o vetor Tmin
        for i in range(len(self.li)):
            saida.insere_vertice()
        for aresta in Tmin:
            saida.insere_aresta(aresta['x'], aresta['y'], aresta['peso'])
        return saida

    def dobra_arestas(self):
        arestas_dobradas = [] #vetor que armazena as arestas que ja foram dobradas
        i = 0
        for v in self.li: #para cada vertice, dobre suas arestas que ainda nao foram dobradas
            for aresta in v:
                if i <= aresta.x:
                    a1 = str(i) + str(aresta.x)
                else:
                    a1 = str(aresta.x) + str(i)
                if a1 not in arestas_dobradas:
                    self.insere_aresta(i, aresta.x, 0)
                    arestas_dobradas.append(a1)
            i+=1

    def matching_perfeito(self, MST):
        vert = []
        for i in range(len(self.li)):   # Buscando todos os vertices de grau impar do grafo
            if len(MST.li[i])%2 != 0:
                vert.append(i)
        self.matching(MST, vert)

    def matching(G, MST, odd_vert):
        import random
        random.shuffle(odd_vert)

        while odd_vert:   # Enquanto ainda existir um vertice de grau impar
            v = odd_vert.pop()   #Remove o vertice do vetor odd_vert
            length = float("inf")
            u = 1
            closest = 0
            for u in odd_vert: #Busca um matching de menor custo com os outros vertices do vetor
                i = 0
                for ar in G.li[v]:
                    if ar.x == u:
                        break
                    i+=1
                if v != u and G.li[v][i].peso < length:
                    length = G.li[v][i].peso
                    closest = u

            MST.insere_aresta(v, closest, length)
            odd_vert.remove(closest)
