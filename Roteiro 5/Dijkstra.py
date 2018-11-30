from grafo_adj import Grafo


def dijkstra(g: Grafo, ini, fin, c, pontos):
    if ini == fin:
        return [ini]
    u = -1
    v = -1
    lista_de_pontos = []
    for i in range(len(g.N)):
        if g.N[i] == ini:
            u = i
        if g.N[i] == fin:
            v = i
        if g.N[i] in pontos:
            lista_de_pontos.append(i)
    beta = []
    phi = []
    pi = []
    cargas = []
    for i in range(len(g.N)):
        beta.append(1000)
        phi.append(0)
        pi.append(-1)
        cargas.append(0)
    beta[u] = 0
    phi[u] = 1
    for i in range(len(g.N)):
        if 1 not in g.M[i] and i != v:
            phi[i] = 1
    cargas[u] = c
    for i in lista_de_pontos:
        cargas[i] = 5
    w = u
    r_ast = 100

    while True:
        list = g.M[w]
        for r in range(len(list)):
            if (list[r] > 0 and beta[r] > beta[w] + list[r] and cargas[w] - 1 >= 0) or (list[r] > 0 and cargas[r] == 0 and cargas[w] -1 >= 0):
                beta[r] = beta[w] + list[r]
                if cargas[r] != 5:
                    cargas[r] = cargas[w] - 1
                pi[r] = w
        menor = 100
        for i in range(len(beta)):
            if beta[i] < menor and phi[i] == 0 and cargas[i] > 0 and ((1 in g.M[i] and i != v) or (i == v)):
                menor = beta[i]
                r_ast = i
        phi[r_ast] = 1
        w = r_ast
        if r_ast == v or menor == 100:
            break

    caminho = [g.N[v]]
    caminho_1 = [pi[v]]
    for i in caminho_1:
        caminho.append(g.N[i])
        if i == u:
            break
        caminho_1.append(pi[i])
    return caminho[::-1]


vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG']

arestas = ["T-S", 'A-B', 'A-C', 'A-D', 'D-C', 'B-E', 'B-I', 'C-G', 'D-H', 'E-F', 'F-B', 'F-J', 'G-F', 'G-J',
           'G-K', 'H-G', 'H-L', 'I-M', 'J-N', 'J-I', 'K-O', 'L-P', 'P-T', 'O-S', 'M-Q', 'M-S', 'N-S', 'N-R',
           'N-T', 'Q-U', 'R-V', 'R-Q', 'S-R', 'S-X', 'U-AA', 'U-Y', 'V-Y', 'V-W', 'V-Z', 'W-S', 'X-AD', 'X-AE',
           'AA-AB', 'AB-AC', 'AD-AC', 'AD-W', 'AC-AF', 'AC-AG']
g_r = Grafo([], [])
for i in vertices:
    g_r.adiciona_vertice(i)
for i in arestas:
    g_r.adiciona_aresta(i)

c_g_r = ['E', 'M']
print(dijkstra(g_r, 'B', 'X', 1, c_g_r))
