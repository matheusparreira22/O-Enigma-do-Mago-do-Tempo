def ordenar_viagem(viagem):
    # Normaliza os valores pegando sempre o menor entre o número e sua inversão
    viagem_normalizada = {min(num, num[::-1]) for num in viagem}
    
    # Retorna a lista ordenada
    return sorted(viagem_normalizada)

# Exemplo de uso
entrada = ["21", "12", "31", "13"]
saida = ordenar_viagem(entrada)
print(saida)  # Saída esperada: ["12", "21", "13", "31"]
