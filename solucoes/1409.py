from collections import deque, defaultdict

def knapsack_min_mana(magias, vida_monstro):

    if vida_monstro <= 0:
        return 0
    
    dp = [float('inf')] * (vida_monstro + 1)
    dp[0] = 0
    
    for dano_necessario in range(1, vida_monstro + 1):
        for mana_custo, dano in magias:
            if dano >= dano_necessario:
                dp[dano_necessario] = min(dp[dano_necessario], mana_custo)
            else:
                if dp[dano_necessario - dano] != float('inf'):
                    dp[dano_necessario] = min(dp[dano_necessario], dp[dano_necessario - dano] + mana_custo)
    
    return dp[vida_monstro] if dp[vida_monstro] != float('inf') else -1

def bfs_min_mana(grafo, monstros_por_salao, magias, n):

    mana_por_salao = {}
    for salao in range(1, n + 1):
        if salao in monstros_por_salao:
            mana_total = 0
            for vida_monstro in monstros_por_salao[salao]:
                mana_necessario = knapsack_min_mana(magias, vida_monstro)
                if mana_necessario == -1:
                    mana_por_salao[salao] = -1
                    break
                mana_total += mana_necessario
            else:
                mana_por_salao[salao] = mana_total
        else:
            mana_por_salao[salao] = 0
    
    from heapq import heappush, heappop
    
    heap = [(mana_por_salao[1], 1)]
    visited = set()
    
    while heap:
        mana_gasto, salao_atual = heappop(heap)
        
        if salao_atual in visited:
            continue
            
        visited.add(salao_atual)
        
        if salao_atual == n:
            return mana_gasto
        
        for vizinho in grafo[salao_atual]:
            if vizinho not in visited:
                mana_necessario = mana_por_salao[vizinho]
                if mana_necessario != -1:  
                    novo_mana = mana_gasto + mana_necessario
                    heappush(heap, (novo_mana, vizinho))
    
    return -1

def resolver():
    while True:
        linha = input().split()
        m, n, g, k = map(int, linha)
        
        if m == 0 and n == 0 and g == 0 and k == 0:
            break
        
        magias = []
        for _ in range(m):
            mana, dano = map(int, input().split())
            magias.append((mana, dano))
        
        grafo = defaultdict(list)
        for _ in range(g):
            a, b = map(int, input().split())
            grafo[a].append(b)
            grafo[b].append(a)
        
        monstros_por_salao = defaultdict(list)
        for _ in range(k):
            salao, vida = map(int, input().split())
            monstros_por_salao[salao].append(vida)
        
        if n == 1:
            if 1 in monstros_por_salao:
                mana_total = 0
                possivel = True
                for vida in monstros_por_salao[1]:
                    mana_necessario = knapsack_min_mana(magias, vida)
                    if mana_necessario == -1:
                        possivel = False
                        break
                    mana_total += mana_necessario
                print(mana_total if possivel else -1)
            else:
                print(0)
            continue
        
        resultado = bfs_min_mana(grafo, monstros_por_salao, magias, n)
        print(resultado)

if __name__ == "__main__":
    resolver()