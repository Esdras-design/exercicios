import pandas as pd

# Dados: horas de estudo por dia de 10 alunos
estudo = pd.Series([2, 3, 2, 4, 5, 3, 3, 6, 4, 2])

# Cálculos Estatísticos
media = estudo.mean()
moda = estudo.mode().iloc[0] if not estudo.mode().empty else None
mediana = estudo.median()
desvio_padrao = estudo.std()

# Cálculo dos percentis
p25 = estudo.quantile(0.25)
p50 = estudo.quantile(0.50)
p75 = estudo.quantile(0.75)
p90 = estudo.quantile(0.90)

# Impressão dos resultados
print(f"Média: {media:.1f}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print("Percentis:")
print(f"P25: {p25}")
print(f"P50: {p50}")
print(f"P75: {p75}")
print(f"P90: {p90}")
