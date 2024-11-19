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

def showOutliers(df):
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


