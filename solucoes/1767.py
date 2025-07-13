def knapsack_saco_noel(pacotes, peso_limite):

    n = len(pacotes)
    
    dp = [[0 for _ in range(peso_limite + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        qt_brinquedos, peso = pacotes[i-1]
        
        for w in range(peso_limite + 1):
            # Não pega o pacote i
            dp[i][w] = dp[i-1][w]
            
            # Pega o pacote i
            if peso <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-peso] + qt_brinquedos)
    
    max_brinquedos = dp[n][peso_limite]
    peso_usado = 0
    pacotes_usados = []
    
    w = peso_limite
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            qt_brinquedos, peso = pacotes[i-1]
            pacotes_usados.append(i-1)
            peso_usado += peso
            w -= peso
    
    pacotes_restantes = n - len(pacotes_usados)
    
    return max_brinquedos, peso_usado, len(pacotes_usados), pacotes_restantes

def resolver():
    n = int(input())  
    
    for caso in range(n):
        pac = int(input()) 
        
        pacotes = []
        for _ in range(pac):
            qt, peso = map(int, input().split())
            pacotes.append((qt, peso))
        
        max_brinquedos, peso_usado, pacotes_usados, pacotes_restantes = knapsack_saco_noel(pacotes, 50)
        
        print(f"{max_brinquedos} brinquedos")
        print(f"Peso: {peso_usado} kg")
        print(f"sobra(m) {pacotes_restantes} pacote(s)")
        print()

if __name__ == "__main__":
    resolver()