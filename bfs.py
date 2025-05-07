from grafo import criar_grafo, calcular_custo_total
from collections import deque
import networkx as nx

def bfs(grafo, inicio, destino):
    visitados = set()
    fila = deque([(inicio, [inicio])])
    todos_visitados = []

    while fila:
        vertice, caminho = fila.popleft()

        if vertice not in visitados:
            visitados.add(vertice)
            todos_visitados.append(vertice)
        
        if vertice == destino:
            return{
                "encontrado": True,
                "caminho": caminho,
                "visitados": todos_visitados
            }

        for vizinho in grafo.neighbors(vertice):
            if vizinho not in visitados:
                fila.append((vizinho, caminho + [vizinho]))
    
    return {
        "encontrado": False,
        "caminho": [],
        "visitados": todos_visitados
    }

if __name__ == "__main__":
    G = criar_grafo()
    inicio = 'A'
    destino = 'G'

    resultado = bfs(G, inicio, destino)

    print("\nCaminho explorado:", ' -> '.join(resultado["visitados"]))
    print("\n----------------------------------------------|\n")
    print("Melhor caminho encontrado:", ' -> '.join(resultado["caminho"]))
    print("\n----------------------------------------------|\n")
    if resultado["encontrado"]:
        custo_total = calcular_custo_total(G, resultado["caminho"])
        print(f"Custo total do caminho: {custo_total}")
        print("\n----------------------------------------------|\n")
        print("Chegou ao destino? ✅ Sim\n")
    else:
        print("Chegou ao destino? ❌ Não")