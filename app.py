from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

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
            html.H3(children='Selecione para filtrar:', className="body-do-painel-texto"),
            html.Div(className="painel-lateral", children=[
                html.Label("Mês"),
                dcc.Dropdown(
                    options=[
                        {"label": "2021", "value": "opcao1"},
                        {"label": "2022", "value": "opcao2"},
                    ],
                    style={'align-items': 'center', 'justify-content': 'center', 'width': '95%'},
                    searchable=False,
                    id='demo-dropdown',
                    placeholder="Selecione o mês",
                    className='lateral-dropdown'
                ),
            ]),
            html.Div(style={"margin-bottom": "20px"}),  # Espaçamento entre os dropdowns
            html.Div(className="painel-lateral", id='base-dados-dropdown', children=[
                html.Label("Unidade"),
                dcc.Dropdown(
                    options=[
                        {"label": "Todas as regiões", "value": "Todas as regioes"},
                        {"label": "Leste", "value": "LESTE"},
                        {"label": "Norte", "value": "NORTE"},
                        {"label": "Sul", "value": "SUL"},
                        {"label": "Oeste", "value": "OESTE"},
                    ],
                    placeholder="Selecione a unidade",
                    style={'align-items': 'center', 'justify-content': 'center', 'width': '95%'},
                    searchable=False,
                    id='dropdown-regiao',
                    className='lateral-dropdown'
                )
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
    html.Div(className="nao-definido", children=[
        html.Label(""),
    ]),
    html.Div(className="calendario", children=[
        html.Label("CALENDARIO"),
        dcc.Graph(figure=fig_heatmap)
    ]),
    html.Div(className="grafico", children=[
        html.Label("grafico"),
    ]),
])

# Função de callback para atualizar o contador
@app.callback(Output('contador-texto', 'children'), [Input('interval-component', 'n_intervals')])
def update_counter(n):
    # Retorna o valor do contador como o número de segundos desde o início do aplicativo
    return str(n)

if __name__ == '__main__':
    app.run_server(debug=True)