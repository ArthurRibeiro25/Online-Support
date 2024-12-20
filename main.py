import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import functions
import os

# Dados fornecidos
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

# Convertendo para DataFrame
df = pd.DataFrame(dados, columns=["Tempo Chegada", "Tempo Serviço"])

# 3. 3 metricas de desempenho
num1, num2 = functions.calcular_taxas_media(df)

avg_arrival_rate = float(f"{num1: .3f}")
avg_service_rate = float(f"{num2: .3f}")

#Metricas:

op = 1

while(op != 0):
    op = int(input('SUPORTE ONLINE' +
               '\n0 - Finalizar' +
               '\n1 - Gráfico de métricas' + 
               '\n2 - Estatísticas descritivas' +
               '\n3 - Mostrar Outliers' +
               '\n4 - Mostrar correlação' + 
               '\n5 - Distribuição de tempo' + 
               '\nOpção: '))
    if(op == 1):
        os.system('clear')
        #Taxa de utilização do profissinal de suporte
        employee_count = float(input('Número de funcionários: '))
        usage_fee = functions.calcular_taxa_utilizacao(avg_arrival_rate, avg_service_rate, employee_count)

        #Tempo medio de espera
        service_fee = functions.service_fee(avg_service_rate)

        #Probabilidade de espera
        waiting_prob = functions.calcular_probabilidade_espera(avg_arrival_rate, avg_service_rate)

        #Gráfico das metricas
        functions.metrics_graph(usage_fee, service_fee, waiting_prob)
    elif(op == 2):
        os.system('clear')
        # a. Estatísticas descritivas
        functions.descriptive_stats(df)
    elif(op == 3):
        os.system('clear')
        # b. Análise de Outliers - utilizando o IQR (Interquartile Range)
        functions.showOutliers(df)
    elif(op == 4):
        os.system('clear')
        # c. Análise de correlação
        functions.correlation(df)
    elif(op == 5):
        os.system('clear')
        # d. Análises Gráficas
        functions.time_distribuition(df)
    elif(op == 0):
        print('Finalizando')
    elif(op > 6):
        print('Digite uma opção válida!')