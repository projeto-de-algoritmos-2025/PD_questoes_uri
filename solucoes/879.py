class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for membros_crime, lucro_crime in zip(group, profit):
            for k in range(n, membros_crime - 1, -1):
                for p in range(minProfit, -1, -1):
                    novo_lucro = min(minProfit, p + lucro_crime)
                    dp[k][novo_lucro] = (dp[k][novo_lucro] + dp[k - membros_crime][p]) % MOD

        total_esquemas = 0
        for k in range(n + 1):
            total_esquemas = (total_esquemas + dp[k][minProfit]) % MOD
            
        return total_esquemas

if __name__ == '__main__':
    solver = Solution()

    print("Demonstrando a solução com os exemplos do problema:\n")
    
    #Exemplo 1
    n1, minProfit1 = 5, 3
    group1, profit1 = [2, 2], [2, 3]
    print(f"--- Exemplo 1 ---")
    print(f"Entrada: n={n1}, minProfit={minProfit1}, group={group1}, profit={profit1}")
    resultado1 = solver.profitableSchemes(n1, minProfit1, group1, profit1)
    print(f"Resultado: {resultado1} (Esperado: 2)\n")

    #Exemplo 2
    n2, minProfit2 = 10, 5
    group2, profit2 = [2, 3, 5], [6, 7, 8]
    print(f"--- Exemplo 2 ---")
    print(f"Entrada: n={n2}, minProfit={minProfit2}, group={group2}, profit={profit2}")
    resultado2 = solver.profitableSchemes(n2, minProfit2, group2, profit2)
    print(f"Resultado: {resultado2} (Esperado: 7)\n")