import pandas as pd


# Dados das notas dos estudantes
notas = pd.Series([8, 7, 9, 6, 10, 8, 9, 7, 6, 7, 8, 8, 7, 9, 6])

# Cálculos Estatísticos
media = notas.mean()
mediana = notas.median()
moda = notas.mode().iloc[0]  # Pega a primeira moda, se houver mais de uma
q1 = notas.quantile(0.25)
p90 = notas.quantile(0.90)
desvio_padrao = notas.std()
amplitude = notas.max() - notas.min()

# Impressão dos resultados
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Primeiro Quartil (Q1): {q1}")
print(f"Percentil 90 (P90): {p90}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print(f"Amplitude: {amplitude}")
#Questão 1 – Análise de Avaliações de um Curso Online
# Resumo dos dados:
#Notas de 15 estudantes variam de 6 a 10.
#Média: 7,67
#Moda: 7
#A nota mais comum foi 7, considerada razoavelmente alta (em uma escala de 0 a 10), indicando uma boa aceitação do curso