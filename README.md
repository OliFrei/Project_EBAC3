# Dashboard Interativo de Análise de Ecommerce

Este projeto é um dashboard interativo desenvolvido com **Dash** e **Plotly** para análise de dados de vendas e avaliações de produtos em uma plataforma de ecommerce. O objetivo é permitir a exploração de várias visualizações de dados de forma dinâmica e interativa, permitindo aos usuários selecionar diferentes marcas para filtrar os gráficos e obter insights sobre o desempenho dos produtos.

## Tecnologias Utilizadas

- **Dash**: Framework para criação de aplicações web interativas.
- **Plotly**: Biblioteca para criação de gráficos interativos.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **Scipy**: Biblioteca para estatísticas avançadas, utilizada para o gráfico de densidade.

## Funcionalidades

O dashboard oferece as seguintes visualizações:

1. **Histograma de Notas**: Exibe a distribuição das notas atribuídas aos produtos.
2. **Gráfico de Dispersão**: Exibe a relação entre o número de avaliações e a quantidade de produtos vendidos.
3. **Mapa de Calor**: Exibe a correlação entre o número de avaliações, nota, preço e quantidade de produtos vendidos.
4. **Gráfico de Barras (Top 10 Marcas Vendidas)**: Exibe as 10 marcas mais vendidas, com a quantidade de produtos vendidos por marca.
5. **Gráfico de Pizza (Distribuição de Gênero)**: Exibe a distribuição de gênero dos produtos.
6. **Gráfico de Densidade (Desconto)**: Exibe a distribuição de descontos aplicados aos produtos.
7. **Gráfico de Regressão**: Exibe a relação entre o desconto e a quantidade de produtos vendidos, com uma linha de regressão linear.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/ecommerce-dashboard.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Certifique-se de que você tem o arquivo `ecommerce_estatistica.csv` no mesmo diretório do script ou forneça o caminho correto para o arquivo CSV.

4. Execute o aplicativo:
   ```bash
   python app.py
   ```

5. Abra o navegador e acesse `http://127.0.0.1:8050/` para visualizar o dashboard.

## Como Usar

1. No canto superior, você verá uma lista de marcas disponíveis. Use a caixa de seleção para escolher uma ou mais marcas que deseja analisar.
2. O dashboard atualizará automaticamente os gráficos com base na seleção das marcas, permitindo que você explore a distribuição de dados, correlações, e muito mais.
3. O gráfico de barras mostrará as quantidades vendidas das marcas selecionadas, enquanto outros gráficos como histograma e dispersão irão refletir as informações dos produtos filtrados pelas marcas.


## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
