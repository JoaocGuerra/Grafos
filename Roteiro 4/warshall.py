from grafo_adj import Grafo

g_p = Grafo()

vert = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
for i in vert:
    g_p.adiciona_vertice(i)

are = ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']
for i in are:
    g_p.adiciona_aresta(i)

def warshall(g: Grafo):
    E = g.M.copy()
    for i in range(1, len(g.N)):
        for j in range(1, len(g.N)):
            if E[i][j] == 1:
                for k in range(1, len(g.N)):
                    E[j][k] = max(E[j][k], E[i][k])

    return E

E = warshall(g_p)
for i in range(len(E)):
    for j in range(len(E)):
        print(E[i][j], end=" ")
    print()
