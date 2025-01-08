from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')

# Mapa de calor interativo de correlações
df_corr = df[['salario', 'anos_experiencia', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod']].corr()
fig = px.imshow(df_corr, text_auto=True, aspect='auto', color_continuous_scale='Viridis', title='Mapa de Calor de Correlação')
fig.show()

# Área Plot do salário ao longo da idade
fig = px.area(df, x='idade', y='salario', line_group='estado_civil', color='estado_civil', title='Evolução do Salário por Idade e Estado')
fig.show()

# Visualização dos Resultados dos Modelos de Classificação e Regressão

# Gráficos para a Classificação

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns

df['salario_categoria'] = (df['salario'] > df['salario'].median()).astype(int) # 1 - acima da mediana, 0 - abaixo da mediana


X = df[['idade', 'anos_experiencia', 'nivel_educacao_cod', 'area_atuacao_cod']] # Preditor
Y = df['salario_categoria'] # Prever

# Dividir dados: Treinamento e teste
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Criar e treinar modelo - Regressão Logística
modelo_lr = LogisticRegression()
modelo_lr.fit(X_train, Y_train)

# Criar e treinar modelo - Árvore de Decisão
modelo_dt = DecisionTreeClassifier()
modelo_dt.fit(X_train, Y_train)

# Prever valores de teste
Y_prev_lr = modelo_lr.predict(X_test)
Y_prev_dt = modelo_dt.predict(X_test)


# Matriz de confusão para Regressão Logística
cm_lr = confusion_matrix(Y_test, Y_prev_lr)
plt.figure(figsize=(8, 6))
sns.heatmap(cm_lr, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('Matriz de Confusão: Regressão Logística')
plt.xlabel('Valores Previstos')
plt.ylabel('Valores Reais')
plt.show()

# Matriz de confusão para Árvore de Decisão
cm_dt = confusion_matrix(Y_test, Y_prev_dt)
plt.figure(figsize=(8, 6))
sns.heatmap(cm_dt, annot=True, fmt='d', cmap='Greens', cbar=False)
plt.title('Matriz de Confusão: Árvore de Decisão')
plt.xlabel('Valores Previstos')
plt.ylabel('Valores Reais')
plt.show()

# Gráfico para Regressão Linear

import matplotlib.pyplot as plt

modelo_lnr = LinearRegression()
modelo_lnr.fit(X_train, Y_train)

# Prever valores de teste
Y_prev = modelo_lnr.predict(X_test)

# Plot de regressão
plt.figure(figsize=(10, 6))
plt.scatter(Y_test, Y_prev, alpha=0.5)
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], 'k--', lw=4)
plt.title('Valores Reais vs. Predições: Regressão Linear')
plt.xlabel('Valores Reais')
plt.ylabel('Valores Previstos')
plt.show()

# Visualização de Correlação
import seaborn as sns
import matplotlib.pyplot as plt

pearson_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod']].corr()
spearman_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod']].corr(method='spearman')

# Heatmap de correlação de Pearson
# plt.figure(figsize=(10,8))
# sns.heatmap(pearson_corr, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title('Correlação de Pearson entre Variáveis')
# plt.show()

# Heatmap de correlação de Spearman
# plt.figure(figsize=(10,8))
# sns.heatmap(spearman_corr, annot=True, cmap='viridis', fmt=".2f")
# plt.title('Correlação de Spearman entre Variáveis')
# plt.show()


import plotly.express as px

# Visualização interativa usando Plotly para a correlação de Pearson
fig = px.imshow(pearson_corr, text_auto=True, aspect="auto", color_continuous_scale="RdBu", title="Correlação de Pearson Interativa")
fig.show()

# Visualização interativa usando Plotly para a correlação de Spearman
fig = px.imshow(spearman_corr, text_auto=True, aspect="auto", color_continuous_scale="RdBu", title="Correlação de Spearman Interativa")
fig.show()