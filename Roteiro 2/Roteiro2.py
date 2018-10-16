from grafo_adj_nao_dir import *
from grafo import Grafo as G

def convertToMatrizAdj(g: G):

    N = g.N
    m = []
    coeficiente = 0
    for i in range(len(N)):
        lenVertices = len(N)
        linha = (coeficiente*['-']) + (lenVertices-coeficiente)*[0]
        coeficiente+=1
        m.append(linha)
    arestas = list(g.A.values())

    for i in range(len(arestas)):
        ligacao = arestas[i].split("-")
        indice1 = N.index(ligacao[0])
        indice2 = N.index(ligacao[1])

        if (indice1 <= indice2):
            m[indice1][indice2] += 1
        else:
            m[indice2][indice1] += 1

    grafo = Grafo(N,m)

    return grafo

def vertices_nao_adjacentes(g: Grafo):
    vna = []
    vna_f = []
    linha_vert = -1
    for i in g.M:
        linha_vert += 1
        coluna_vert = -1
        for j in i:
            coluna_vert += 1
            are = g.N[linha_vert]+'-'+g.N[coluna_vert]
            are2 = g.N[coluna_vert]+'-'+g.N[linha_vert]
            if j==0 and (are not in vna):
                vna.append(are)
                if are2 not in vna:
                    vna.append(are2)
    for i in g.N:
        for j in vna:
            if i == j[0]:
                vna_f.append(j)

    return vna_f

def ha_laco(g: Grafo):
    cont = 0
    for i in range(len(g.M)):
        if g.M[i][i] >= 1:
            return True

    return False

def ha_paralelas(g: Grafo):
    for i in g.M:
        for j in i:
            if j != '-' and j > 1:
                return True

    return False

def grau(g: Grafo, vert):
    cont = 0
    ind = 0
    for i in range(len(g.N)):
        if g.N[i]==vert:
            ind = i

    for i in g.M[ind]:
        if i != '-':
            cont += i

    for i in range(len(g.M)):
        if i != ind:
            if g.M[i][ind]!= '-':
                cont+=g.M[i][ind]
    return cont

def arestas_sobre_vertice(g: Grafo, vert):
    asv = []
    ind_vert = 0
    for i in range(len(g.N)):
        if g.N[i] == vert:
            ind_vert = i

    for i in range(len(g.M)):
        for j in range(len(g.M)):
            if (g.M[i][j] != '-' and g.M[i][j] > 0) and (i == ind_vert or j == ind_vert):
                for k in range(g.M[i][j]):
                    asv.append(g.N[i]+'-'+g.N[j])
    return asv

def eh_completo(g: Grafo):
    cont = 0
    cont2 = 0
    for i in range(len(g.M)):
        for j in range(len(g.M)):
            if j > i:
                cont += 1
                if g.M[i][j] > 0:
                    cont2 += 1

    if cont == cont2:
        return True

    return False
