from grafo import Grafo

def vertices_nao_adjacentes(g: Grafo):
    vna = []
    for i in g.N:
        for j in g.N:
            are = i+'-'+j
            are2 = j+'-'+i
            if (are not in list(g.A.values()) and are2 not in list(g.A.values()) ):
                vna.append(are)
    return vna

def ha_laco(g: Grafo):
    cont = 0
    for i in g.N:
        for j in g.N:
            if i == j:
                are = i+'-'+j
                if (are  in list(g.A.values())):
                    cont+=1
    if (cont>=1):
        return True
    else:
        return False

def ha_paralelas(g: Grafo):
    cont=0
    for i in g.N:
        for j in g.N:
            are = i+'-'+j
            for k in list(g.A.values()):
                if k == are:
                    cont +=1
            
            if cont >= 2:
                return True
            cont = 0

    return False

def grau(g: Grafo,vert):
    cont = 0
    for i in list(g.A.values()):
        if vert in list(i): 
            cont +=1
    return cont

def arestas_sobre_vertice(g: Grafo,vert):
    asv = []
    for i, j in g.A.items():
        if vert in j:
            asv.append(i)
    return asv

def eh_completo(g: Grafo):
    comb = []
    comb2 = []
    for i in range(len(g.N)):
        for j in range(i+1,len(g.N)):
            comb.append(g.N[i]+'-'+g.N[j])
            comb2.append(g.N[j]+'-'+g.N[i])

    for i in range(len(comb)):
        if comb[i] not in list(g.A.values()) and comb2[i] not in list(g.A.values()):
            return False
    return True

def eh_conexo(g: Grafo):
    dic = {}
    if len(g.A.values()) == 0:
        return False

    for vertice in g.N:
        lista = []
        for are in g.A.values():
            if are[0] == vertice and are[2] not in lista:
                lista.append(are[2])
            if are[2] == vertice and are[0] not in lista:
                lista.append(are[0])
        dic[vertice] = lista

    maior = 0
    chave = ""
    for vert in dic:
        if len(dic[vert]) > maior:
            maior = len(dic[vert])
            chave = vert

    lista_maior = []
    for i in range(len(dic[chave])):
        lista_maior.append(dic[chave][i])

    for vert in g.N:
        if vert in lista_maior or chave == vert:
            continue
        else:
            cont = 0
            for busca in lista_maior:
                if vert in dic[busca]:
                    cont += 1

            if cont == 0:
                return False
            lista_maior.append(vert)

    return True
