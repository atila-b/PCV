# -*- coding: utf-8 -*-
from grafo.grafo import Grafo
import time
from copy import deepcopy

def custo_caminho(self, cam): 
        sum = 0
        for i in range(len(cam) - 1):
            for aresta in self.li[cam[i]]:
                if aresta.x == cam[i+1]:
                    sum += aresta.peso
                    break
        return sum

def constroi_grafo(grafo, file):
    i = 0
    for line in file:
        line = line.split()
        line[-1] = line[-1].strip()
        i+=1
        for j in range(i, len(line)):
            grafo.insere_aresta(i-1, j, int(line[j]))
    return grafo
    
def PCV(grafo, vi):
    #grafo.print_grafo()
    print("- Heurística Bellmore & Nemhauser\n")
    start_time = time.time()
    H = grafo.BN(vi)
    end_time = time.time()
    print("custo = " + str(custo_caminho(grafo, H)))
    print("tempo de execucao = " + str(end_time - start_time) + " segundos\n")
    print("- Heurística Twice-around\n")
    start_time = time.time()
    H = grafo.TA(vi)
    end_time = time.time()
    print("custo = " + str(custo_caminho(grafo, H)))
    print("tempo de execucao = " + str(end_time - start_time) + " segundos\n")
    print("- Heurística de Christofides\n")
    start_time = time.time()
    H = grafo.christofides(vi)
    end_time = time.time()
    print("custo = " + str(custo_caminho(grafo, H)))
    print("tempo de execucao = " + str(end_time - start_time) + " segundos\n")

def main():
    """
    print("Grafo 1:")
    grafo4 = Grafo()
    for i in range(5):
        grafo4.insere_vertice()
    grafo4.insere_aresta(0, 1, 2)
    grafo4.insere_aresta(1, 2, 3)
    grafo4.insere_aresta(2, 3, 3)
    grafo4.insere_aresta(3, 4, 4)
    grafo4.insere_aresta(4, 0, 4)
    grafo4.insere_aresta(0, 2, 1)
    grafo4.insere_aresta(0, 3, 7)
    grafo4.insere_aresta(1, 3, 5)
    grafo4.insere_aresta(1, 4, 3)
    grafo4.insere_aresta(2, 4, 2)
    PCV(grafo4, 0)

    print("Grafo 2:")
    grafo7 = Grafo()
    for i in range(6):
        grafo7.insere_vertice()
    grafo7.insere_aresta(0, 1, 1) 
    grafo7.insere_aresta(1, 2, 5) 
    grafo7.insere_aresta(2, 3, 10) 
    grafo7.insere_aresta(3, 4, 1) 
    grafo7.insere_aresta(4, 0, 8) 
    grafo7.insere_aresta(0, 2, 4) 
    grafo7.insere_aresta(0, 3, 9) 
    grafo7.insere_aresta(1, 3, 5) 
    grafo7.insere_aresta(1, 4, 7) 
    grafo7.insere_aresta(2, 4, 10) 
    grafo7.insere_aresta(5, 0, 2) 
    grafo7.insere_aresta(5, 1, 6) 
    grafo7.insere_aresta(5, 2, 4) 
    grafo7.insere_aresta(5, 3, 7)
    grafo7.insere_aresta(5, 4, 3) 
    PCV(grafo7, 0)
    """
    print("Aplicando as heurísticas nas bases de dados para resolver o PCV:\n")
    print("Grafo da base de dados pd01_d.txt:\n")
    grafo1 = Grafo()
    for i in range(15):
        grafo1.insere_vertice()
    
    f1 = open('./datasets/pd01_d.txt','r')
    grafo1 = constroi_grafo(grafo1, f1)
    PCV(grafo1, 0)
    
    print("Grafo da base de dados gr17_d.txt:\n")
    grafo2 = Grafo()
    for i in range(17):
        grafo2.insere_vertice()
    
    f1 = open('./datasets/gr17_d.txt','r')
    grafo2 = constroi_grafo(grafo2, f1)
    PCV(grafo2, 0)

    print("Grafo da base de dados fri26_d.txt:\n")
    grafo3 = Grafo()
    for i in range(26):
        grafo3.insere_vertice()
    
    f1 = open('./datasets/fri26_d.txt','r')
    grafo3 = constroi_grafo(grafo3, f1)
    PCV(grafo3, 0)

    print("Grafo da base de dados dantzig42_d.txt:\n")
    grafo4 = Grafo()
    for i in range(42):
        grafo4.insere_vertice()
    
    f1 = open('./datasets/dantzig42_d.txt','r')
    grafo4 = constroi_grafo(grafo4, f1)
    PCV(grafo4, 1)

    print("Grafo da base de dados att48_d.txt:\n")
    grafo0 = Grafo()
    for i in range(48):
        grafo0.insere_vertice()
    f1 = open('./datasets/att48_d.txt', 'r')
    grafo0 = constroi_grafo(grafo0, f1)
    PCV(grafo0, 0)

if __name__ == '__main__':
    main()