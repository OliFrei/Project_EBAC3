from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from scipy.stats import gaussian_kde


df = pd.read_csv('ecommerce_estatistica.csv')
top_10_marcas = df['Marca'].value_counts().head(10)
lista_marca = top_10_marcas.index.unique()
options = [{'label': marca, 'value': marca} for marca in lista_marca]


def cria_graficos(selecao_marca):
    # Gráfico de Histograma

    fig1 = px.histogram(df, x='Nota', nbins=15, title='Distribuição de Nota dos Produtos')

    # Gráfico de Dispersão

    fig2 = px.scatter(df, x='N_Avaliações', y='Qtd_Vendidos_Cod', title='Dispersão de Nº de Avaliações e Quantidade Vendida')

    # Mapa de Calor
    df_corr = df[['N_Avaliações', 'Nota', 'Preço', 'Qtd_Vendidos_Cod']].corr()
    fig3 = px.imshow(df_corr, text_auto=True, aspect='auto', color_continuous_scale='Viridis', title='Correlação entre Nº de Avaliações, Nota, Preço, e Quantidade Vendida')

    # Gráfico de Barra
    if not selecao_marca:  # Se não há seleção, deixa todos marcados
        filtro_marcas = df[df['Marca'].isin(lista_marca)]
    else:
        filtro_marcas = df[df['Marca'].isin(selecao_marca)]
    marca_counts = filtro_marcas.groupby('Marca')['Qtd_Vendidos_Cod'].sum().reset_index()
    marca_counts = marca_counts.sort_values(by='Qtd_Vendidos_Cod', ascending=False).head(10)
    marca_counts.columns = ['Marca', 'Quantidade']
    fig4 = px.bar(marca_counts, x='Marca', y='Quantidade', title='Top 10 Marcas Vendidas')

    # Gráfico de Pizza

    fig5 = px.pie(df, names='Gênero', title='Distribuição de Gênero dos Produtos', hole=0.2)

    # Gráfico de Densidade

    data = df['Desconto']
    kde = gaussian_kde(data, bw_method='scott')
    x_range = np.linspace(data.min(), data.max(), 500)
    density = kde(x_range)
    fig6 = go.Figure()

    # Curva de Densidade
    fig6.add_trace(go.Scatter(x=x_range, y=density, fill='tozeroy', line=dict(color='#863e9c'), name='Densidade'))

    # Update Layout
    fig6.update_layout(title='Densidade de Desconto', xaxis_title='Desconto', yaxis_title='Densidade', template='plotly_white', width=800, height=500)

    # # Gráfico de Regressão

    # Regressão Linear
    x = df['Desconto']
    y = df['Qtd_Vendidos_Cod']
    slope, intercept = np.polyfit(x, y, 1)
    line = slope * x + intercept

    # Criar gráfico de Regressão
    fig7 = px.scatter(df, x='Desconto', y='Qtd_Vendidos_Cod', title='Regressão de Desconto e Quantidade Vendida', labels={'Desconto': 'Desconto', 'Qtd_Vendidos_Cod': 'Quantidade Vendida'}, opacity=0.5)

    # Linha de Regressão
    fig7.add_scatter( x=x, y=line, mode='lines', name='Linha de Regressão', line=dict(color='#278f65'))

    return fig1, fig2, fig3, fig4, fig5, fig6, fig7

def cria_app():
    app = Dash(__name__)

    app.layout = html.Div([
        html.H1("Dashboard Interativo"),
        html.Div('''
            Interatividade entre os 
            dados.
            '''),
        html.Br(),
        dcc.Graph(id='id_grafico_histograma'),
        dcc.Graph(id='id_grafico_dispersao'),
        dcc.Graph(id='id_mapa_calor'),
        dcc.Checklist(
            id='id_selecao_marca',
            options=options,
            value=[lista_marca[0]],
            inline=True
        ),
        dcc.Graph(id='id_grafico_barra'),
        dcc.Graph(id='id_grafico_pizza'),
        dcc.Graph(id='id_grafico_densidade'),
        dcc.Graph(id='id_grafico_regressao')
    ])
    return app

if __name__ == '__main__':
    app = cria_app()

    @app.callback(
        [
            Output('id_grafico_histograma', 'figure'),
            Output('id_grafico_dispersao', 'figure'),
            Output('id_mapa_calor', 'figure'),
            Output('id_grafico_barra', 'figure'),
            Output('id_grafico_pizza', 'figure'),
            Output('id_grafico_densidade', 'figure'),
            Output('id_grafico_regressao', 'figure')
        ],
        [Input('id_selecao_marca', 'value')]
    )
    def atualiza_graficos(selecao_marca):
        fig1, fig2, fig3, fig4, fig5, fig6, fig7 = cria_graficos(selecao_marca)
        return [fig1, fig2, fig3, fig4, fig5, fig6, fig7]

    app.run_server(debug=True, port=8050)
