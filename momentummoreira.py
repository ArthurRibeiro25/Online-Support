import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

# a. Estatísticas descritivas
estatisticas = df.describe()

# b. Análise de Outliers - utilizando o IQR (Interquartile Range)
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR)))

# c. Análise de Correlação
correlacao = df.corr()

# d. Análises Gráficas
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

# e. Principais interpretações
interpretacoes = {
    "Estatísticas Descritivas": estatisticas,
    "Outliers": outliers.sum(),  # Contagem de outliers por coluna
    "Correlação": correlacao,
}

interpretacoes