from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

app = Dash(__name__)

# Definição dos dados do mapa de calor
heatmap_data = [
    [00, 40, 30, 60, 24, 100, 99],
    [10, 45, 50, 25, 70, 97, 100],
    [15, 40, 32, 60, 99, 100, 98],
    [17, 37, 30, 60, 24, 95, 100],
    [11, 40, 30, 60, 89, 100, 99],
]

# Números dos dias correspondentes ao heatmap_data
days_numbers = [
    [1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19, 20, 21],
    [22, 23, 24, 25, 26, 27, 28],
    [29, 30, 31]
]

# Criação do objeto Heatmap com os dados e configurações
fig_heatmap = go.Figure(data=go.Heatmap(z=heatmap_data, text=days_numbers, colorscale='blues'))
fig_heatmap.update_layout(
    title={
        'text': "Maio",
        'x': 0.5,  # Define a posição horizontal do título
        'xanchor': 'center',  # Ancora o título ao centro horizontal
        'yanchor': 'top'  # Ancora o título ao topo vertical
    },
    xaxis=dict(
        showgrid=True, 
        gridwidth=1, 
        gridcolor='rgba(0,0,0,0.1)',  # Mostra as linhas verticais entre os dias
        showticklabels=False  # Remove os números de legenda do eixo x
    ),
    yaxis=dict(
        showgrid=True, 
        gridwidth=1, 
        gridcolor='rgba(0,0,0,0.1)',  # Mostra as linhas horizontais entre os dias
        showticklabels=False  # Remove os números de legenda do eixo y
    )
)
fig_heatmap.update_traces(textfont=dict(color='black'))

# Definindo os dados do gráfico de linha
horas_do_dia = np.arange(6, 24)  # Horas de funcionamento: 6h às 23h
quantidade_de_pessoas_por_hora = [10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 190, 180, 150]

# Criando o gráfico de linha
fig_linha = go.Figure()

# Adicionando os dados ao gráfico de linha
fig_linha.add_trace(go.Scatter(
    x=horas_do_dia,
    y=quantidade_de_pessoas_por_hora,
    mode='lines+markers',
    name='Quantidade de Pessoas',
    marker=dict(color='blue')
))

# Configurando o layout do gráfico de linha
fig_linha.update_layout(
    title='Quantidade de Pessoas na Padaria por Hora',
    xaxis=dict(title='Hora do Dia'),
    yaxis=dict(title='Quantidade de Pessoas'),
    hovermode='x',
    template='plotly_white',
    height=330,  # Altura do gráfico
    width=600   # Largura do gráfico
)

# Lista dos 3 produtos mais vendidos
produtos_mais_vendidos = ["Pão Francês", "Frios", "Leite"]

# Layout do aplicativo
app.layout = html.Div([
    html.Div(className="body", children=[
        html.Div(className="header", children=[
            html.H1('SMARTCOUNT', className="header-logo"),
        ]),
        html.Div(className="body-do-painel", children=[
            html.Img(src="./assets/imagens/contabilidade.png", alt="logo", className='logo'),
            html.Div(className="notificacao", children=[
                html.H3(children='Notificações', className="body-do-painel-texto"),
                html.Img(src="./assets/imagens/sino.png", alt="sino", className='sino'),
            ]),
            html.Div(className="quantidade-funcionarios-ativos", children=[
                html.Label("Funcionários Ativos:", className="body-do-painel-texto"),
                html.H2("50", className="body-do-painel-texto")  # Quantidade de funcionários ativos
            ]),
 
        ]),
        html.Div(className="contador", children=[
            html.Label("PESSOAS", style={'marginBottom': '10px'}),
            # Componente de texto para exibir o contador
            html.H1(id='contador-texto', style={'fontSize': 50}),
            # Intervalo para atualizar o contador a cada segundo
            dcc.Interval(
                id='interval-component',
                interval=3100,  # em milissegundos
                n_intervals=0
            )
        ]),
    ]),
    html.Div(className="calendario", children=[
        html.Label("CALENDARIO"),
        dcc.Graph(figure=fig_heatmap)
    ]),
    html.Div(className="grafico-de-linha", children=[
        dcc.Graph(figure=fig_linha)
    ]),
    html.Div(className="nao-definido", children=[
    html.Label("PODUTOS MAIS VENDIDOS:", className="body-do-painel-texto"),
    html.Ul([
    html.Li(produto) for produto in produtos_mais_vendidos
                ])
            ])
])

# Função de callback para atualizar o contador
@app.callback(Output('contador-texto', 'children'), [Input('interval-component', 'n_intervals')])
def update_counter(n):
    # Retorna o valor do contador como o número de segundos desde o início do aplicativo
    return str(n)

if __name__ == '__main__':
    app.run_server(debug=True)