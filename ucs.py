from grafo import criar_grafo, calcular_custo_total
import heapq
import networkx as nx

def ucs(grafo, inicio, destino):
    if inicio == destino:
        return {
            "encontrado": True,
            "caminho": [inicio],
            "visitados": [inicio],
            "expansoes": 1
        }

    heap = []
    heapq.heappush(heap, (0, inicio, [inicio]))  # (custo, nó, caminho)

    custo_minimo = {inicio: 0}
    visitados = set()
    todos_visitados = []
    expansoes = 0

    while heap:
        custo_atual, no_atual, caminho_atual = heapq.heappop(heap)

        if no_atual in visitados:
            continue  # Já processamos um caminho melhor para esse nó

        visitados.add(no_atual)
        todos_visitados.append(no_atual)
        expansoes += 1  # Conta cada nó que é realmente expandido

        if no_atual == destino:
            return {
                "encontrado": True,
                "caminho": caminho_atual,
                "visitados": todos_visitados,
                "expansoes": expansoes,
                "custo_total": custo_atual
            }

        for vizinho in grafo.neighbors(no_atual):
            peso = grafo.get_edge_data(no_atual, vizinho)['weight']
            novo_custo = custo_atual + peso
            if vizinho not in custo_minimo or novo_custo < custo_minimo[vizinho]:
                custo_minimo[vizinho] = novo_custo
                heapq.heappush(heap, (novo_custo, vizinho, caminho_atual + [vizinho]))

    return {
        "encontrado": False,
        "caminho": [],
        "visitados": todos_visitados,
        "expansoes": expansoes,
        "custo_total": float('inf')
    }

if __name__ == "__main__":
    G = criar_grafo()
    inicio = 'A'
    destino = 'B'

    resultado = ucs(G, inicio, destino)

    print("\nCaminho explorado:", ' -> '.join(resultado["visitados"]))
    print("\n----------------------------------------------|\n")
    print("Melhor caminho encontrado:", ' -> '.join(resultado["caminho"]))
    print("\n----------------------------------------------|\n")

    if resultado["encontrado"]:
        print(f"Custo total do caminho: {resultado['custo_total']}")
        print("\n----------------------------------------------|\n")
        print("Chegou ao destino? ✅ Sim\n")
    else:
        print("Chegou ao destino? ❌ Não")

    print(f"Número de expansões realizadas: {resultado['expansoes']}")