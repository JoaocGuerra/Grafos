from grafo_adj_nao_dir import *

def grau(g: Grafo, vert):
    cont = 0
    ind = 0
    for i in range(len(g.N)):
        if g.N[i] == vert:
            ind = i

    for i in g.M[ind]:
        if i != '-':
            cont += i

    for i in range(len(g.M)):
        if i != ind:
            if g.M[i][ind] != '-':
                cont += g.M[i][ind]
    return cont

def caminho_euleriano(g: Grafo):
    lista = []
    imp=0
    for i in g.N:
        gr = grau(g, i)
        lista.append(gr)

    for i in lista:
        if i % 2 != 0:
            imp += 1

    if imp == 2 or imp == 0:
        return True

    return False

