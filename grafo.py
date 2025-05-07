import networkx as nx

def criar_grafo():
    """
    Cria e retorna um grafo ponderado usando NetworkX com base no dicionário fornecido.
    """
    # Criar um grafo vazio
    G = nx.Graph()
    
    # Seu grafo como dicionário
    grafo_final = {
        'A': [('B', 3), ('C', 5), ('D', 2), ('H', 10)],
        'B': [('A', 3), ('C', 5), ('D', 8), ('E', 4), ('G', 6), ('H', 6)],
        'C': [('A', 5), ('B', 5), ('E', 1), ('F', 7), ('G', 9)],
        'D': [('A', 2), ('B', 8), ('E', 12), ('H', 14)],
        'E': [('B', 4), ('C', 1), ('D', 12), ('G', 15)],
        'F': [('C', 7), ('H', 9)],
        'G': [('B', 6), ('C', 9), ('E', 15)],
        'H': [('A', 10), ('B', 6), ('D', 14), ('F', 9)]  # H-F
    }

    # Converter o dicionário em uma lista de triplas (nó1, nó2, peso)
    edges = []
    for node, neighbors in grafo_final.items():
        for neighbor, weight in neighbors:
            edges.append((node, neighbor, weight))

    # Adicionar as arestas com peso ao grafo
    G.add_weighted_edges_from(edges)

    return G


def calcular_custo_total(grafo, caminho):

    if len(caminho) < 2:
        print("Caminho inválido: precisa ter ao menos 2 nós")

    custo_total = 0

    for i in range(len(caminho) - 1):
        u, v = caminho[i], caminho [i + 1]
        custo_total += grafo.get_edge_data(u, v)['weight']

    return custo_total
