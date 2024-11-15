from collections import deque

def simulador_atendimento(dados):
    fila = deque()  # Fila de atendimento
    tempo_atual = 0  # Tempo atual do simulador
    tempo_total = 0  # Acumulador do tempo total de atendimento
    atendimentos = []  # Lista para armazenar os resultados dos atendimentos

    for chegada, servico in dados:
        # Verifica se alguém precisa ser atendido antes de uma nova chegada
        if fila:
            while fila and fila[0][0] <= chegada:
                atendimento = fila.popleft()
                tempo_atual = max(tempo_atual, atendimento[0]) + atendimento[1]
                tempo_total += tempo_atual - atendimento[0]
        
        # Adiciona o novo atendimento à fila
        fila.append((chegada, servico))

    # Processa os atendimentos restantes
    while fila:
        atendimento = fila.popleft()
        tempo_atual = max(tempo_atual, atendimento[0]) + atendimento[1]
        tempo_total += tempo_atual - atendimento[0]

    # Calculando a média do tempo de espera
    num_atendimentos = len(dados)
    tempo_medio_espera = tempo_total / num_atendimentos if num_atendimentos > 0 else 0

    return tempo_medio_espera

# Dados de entrada
dados = [
    (3, 17), (6, 16), (9, 16), (3, 20), (6, 16), (4, 11), (1, 12), (3, 20), (14, 23), (6, 14),
    (8, 10), (6, 24), (3, 19), (3, 24), (8, 23), (7, 12), (3, 16), (10, 15), (2, 21), (4, 14),
    (6, 15), (9, 15), (9, 20), (4, 10), (1, 21), (5, 20), (11, 21), (1, 15), (0, 23), (4, 12),
    (2, 22), (3, 22), (4, 23), (13, 16), (6, 18), (0, 15), (7, 10), (3, 16), (8, 16), (1, 24),
    (5, 15), (6, 14), (5, 20), (6, 19), (1, 10), (6, 15), (1, 22), (6, 21), (0, 16), (4, 16),
    (9, 24), (5, 15), (3, 14), (4, 19), (9, 22), (5, 14), (4, 2), (3, 12), (8, 13), (1, 18),
    (4, 16), (6, 17), (7, 24), (3, 22), (2, 23), (4, 20), (3, 24), (2, 17), (8, 19), (3, 14),
    (6, 17), (3, 10), (2, 10), (3, 1), (1, 12), (0, 10), (6, 19), (9, 13), (5, 15), (1, 19),
    (7, 18), (5, 10), (0, 23), (8, 22), (6, 23), (5, 22), (6, 15), (8, 18), (1, 23), (8, 24),
    (2, 10), (4, 10), (4, 5), (2, 6), (2, 8), (3, 13), (3, 5), (15, 14), (5, 24), (0, 18),
    (8, 13), (4, 17), (5, 18), (3, 22), (6, 10), (8, 24), (9, 17), (4, 22), (1, 12), (2, 16),
    (2, 23), (13, 13), (6, 16), (11, 14), (1, 17), (5, 18), (1, 10), (2, 20), (4, 16), (6, 20),
    (6, 10), (8, 24), (6, 15), (5, 13), (0, 10), (5, 14), (7, 19), (6, 12), (5, 12), (9, 17),
    (6, 20), (7, 14), (1, 24), (8, 23), (5, 22), (4, 19), (2, 22), (2, 13), (10, 24), (2, 18),
    (3, 12), (6, 10), (4, 15), (6, 19), (4, 18), (0, 13), (7, 17), (4, 16), (3, 24), (7, 20),
    (0, 12), (5, 24), (7, 15), (7, 22), (5, 16), (1, 18), (6, 19), (3, 23), (6, 15), (0, 23)
]

# Executando o simulador
tempo_medio_espera = simulador_atendimento(dados)

# Exibindo o resultado
print(f"Tempo médio de espera: {tempo_medio_espera:.2f} unidades de tempo")
