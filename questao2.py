import pandas as pd

# Dados de vendas mensais de 12 produtos
vendas = pd.Series([34, 22, 50, 28, 44, 60, 20, 39, 55, 18, 75, 33])

# Cálculos Estatísticos
media = vendas.mean()
mediana = vendas.median()
moda = vendas.mode().iloc[0] if not vendas.mode().empty else None  # Verifica se existe moda
q1 = vendas.quantile(0.25)
q2 = vendas.quantile(0.50)
q3 = vendas.quantile(0.75)
valor_minimo = vendas.min()
valor_maximo = vendas.max()
amplitude = valor_maximo - valor_minimo
desvio_padrao = vendas.std()

# Impressão dos resultados
print(f"Média: {media:.2f}")
print(f"Mediana (Q2): {mediana}")
print(f"Moda: {moda} (ocorre apenas uma vez, pode não ser significativa)")
print(f"Q1 (25%): {q1}")
print(f"Q3 (75%): {q3}")
print(f"Valor mínimo: {valor_minimo}")
print(f"Valor máximo: {valor_maximo}")
print(f"Amplitude: {amplitude}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")