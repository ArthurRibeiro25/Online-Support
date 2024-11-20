import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os

os.environ['TCL_LIBRARY'] = 'C:/Users/ribei/AppData/Local/Programs/Python/Python313/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'C:/Users/ribei/AppData/Local/Programs/Python/Python313/tcl/tk8.6'

def time_distribuition(df):
    # Histograma para ver a distribuição dos tempos
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.hist(df["Tempo Chegada"], bins=20, color='blue', alpha=0.7)
    plt.title("Distribuição do Tempo de Chegada")
    plt.xlabel("Tempo Chegada")
    plt.ylabel("Frequência")
    plt.subplot(1, 2, 2)
    plt.hist(df["Tempo Serviço"], bins=20, color='green', alpha=0.7)
    plt.title("Distribuição do Tempo de Serviço")
    plt.xlabel("Tempo Serviço")
    plt.ylabel("Frequência")
    plt.tight_layout()
    plt.show()

def identificar_outliers(df):
    outliers = {}

    for coluna in df.select_dtypes(include=[np.number]).columns:
        Q1 = df[coluna].quantile(0.25)
        Q3 = df[coluna].quantile(0.75)
        IQR = Q3 - Q1

        # Limites para outliers moderados e extremos
        limite_inferior_moderado = Q1 - 1.5 * IQR
        limite_superior_moderado = Q3 + 1.5 * IQR
        limite_inferior_extremo = Q1 - 3 * IQR
        limite_superior_extremo = Q3 + 3 * IQR

        # Identificar outliers
        outliers[coluna] = {
            'outliers_moderados': df[(df[coluna] < limite_inferior_moderado) | (df[coluna] > limite_superior_moderado)][coluna].tolist(),
            'outliers_extremos': df[(df[coluna] < limite_inferior_extremo) | (df[coluna] > limite_superior_extremo)][coluna].tolist()
        }

    return outliers

def showOutliers(df):

    #Identifica e lista os outliers
    print(identificar_outliers(df))

    # Boxplot para detectar outliers
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.boxplot(x=df["Tempo Chegada"])
    plt.title("Boxplot do Tempo de Chegada")

    plt.subplot(1, 2, 2)
    sns.boxplot(x=df["Tempo Serviço"])
    plt.title("Boxplot do Tempo de Serviço")

    plt.tight_layout()
    plt.show()

def correlation(df):
    
    #Extraindo valores
    arrivalTime = df["Tempo Chegada"]
    serviceTime = df["Tempo Serviço"]

    #Calculando media
    avg_arrivalTime = np.mean(arrivalTime)
    avg_serviceTime = np.mean(serviceTime)

    # Calculando os desvios padrão
    arrivalDeviation = np.std(arrivalTime, ddof=1)
    serviceDeviation = np.std(serviceTime, ddof=1)

    #Calculando a covariância
    cov = np.sum((arrivalTime - avg_arrivalTime) * (serviceTime - avg_serviceTime)) / (len(arrivalTime) - 1)

    #Calculando correlação
    correlacao = cov / (serviceDeviation * arrivalDeviation)

    print(f'A correlação entre tempo de chegada e tempo de serviço é: {correlacao:.2f}')

    plt.scatter(arrivalTime, serviceTime, label='Correlação', color='blue')
    plt.xlabel('Tempo de chegada')
    plt.ylabel('Tempo de atendimento')
    plt.title(f'Gráfico de Dispersão entre tempo de chegada e tempo de serviço: ')
    plt.axhline(y=avg_serviceTime, color='r', linestyle='--', label='Média de tempo de atendimento')
    plt.axvline(x=avg_arrivalTime, color='g', linestyle='--', label='Média de tempo de chegada')
    plt.legend()
    plt.grid()
    plt.show()


def descriptive_stats(df):

    arrivalTime = df["Tempo Chegada"]
    serviceTime = df["Tempo Serviço"]

    #Calculando média
    avg_arrivalTime = np.mean(arrivalTime)
    avg_serviceTime = np.mean(serviceTime)

    #Calculando mediana
    median_arrivalTime = np.median(arrivalTime)
    median_serviceTime = np.median(serviceTime)

    #Calculando os desvios padrão
    arrivalDeviation = np.std(arrivalTime, ddof=1)
    serviceDeviation = np.std(serviceTime, ddof=1)

    #Calculando variância
    variancia_arrival = np.var(arrivalTime, ddof=1)
    variancia_service = np.var(serviceTime, ddof=1)

    #return avg_arrivalTime, avg_serviceTime, median_arrivalTime, median_serviceTime, arrivalDeviation, serviceDeviation, variancia_arrival, variancia_service

    labels = ['Média', 'Mediana', 'Desvio Padrão', 'Variância']
    arrival_values = [avg_arrivalTime, median_arrivalTime, arrivalDeviation, variancia_arrival]
    service_values = [avg_serviceTime, median_serviceTime, serviceDeviation, variancia_service]

    x = np.arange(len(labels))  # Posições das barras no eixo x
    width = 0.35  # Largura das barras

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, arrival_values, width, label='Tempo de chegada')
    rects2 = ax.bar(x + width/2, service_values, width, label='Tempo de serviço')

    # Adicionar rótulos, título e legenda
    ax.set_ylabel('Valores')
    ax.set_title('Estatísticas Descritivas')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    # Ajustar o layout do gráfico
    fig.tight_layout()

    # Exibir o gráfico
    plt.show()
