from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

app = Dash(__name__)

# Definição dos dados do mapa de calor para abril e maio para duas unidades
heatmap_data_abril_unidade1 = [
    [100, 29, 90, 80, 50, 60, 70],
    [150, 89, 74, 45, 55, 65, 75],
    [87, 30, 40, 50, 60, 70, 80],
    [92, 35, 45, 55, 65, 75, 85],
    [30, 40, 50, 60, 99, 80, 90],
]

heatmap_data_maio_unidade1 = [
    [0, 40, 30, 60, 24, 100, 99],
    [10, 45, 50, 25, 70, 97, 100],
    [15, 40, 32, 60, 99, 100, 98],
    [17, 37, 30, 60, 24, 95, 100],
    [11, 40, 30, 60, 89, 100, 99],
]

heatmap_data_abril_unidade2 = [
    [12, 22, 32, 42, 52, 62, 72],
    [17, 27, 37, 47, 57, 67, 77],
    [22, 32, 42, 52, 62, 72, 82],
    [27, 37, 47, 57, 67, 77, 87],
    [32, 42, 52, 62, 72, 82, 92],
]

heatmap_data_maio_unidade2 = [
    [2, 42, 32, 62, 26, 102, 101],
    [12, 47, 52, 27, 72, 99, 102],
    [17, 42, 34, 62, 101, 102, 100],
    [19, 39, 32, 62, 26, 97, 102],
    [13, 42, 32, 62, 91, 102, 101],
]

# Números dos dias correspondentes ao heatmap_data
days_numbers = [
    [1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19, 20, 21],
    [22, 23, 24, 25, 26, 27, 28],
    [29, 30, 31]
]

# Função para criar o gráfico de calor
def create_heatmap(month, unit):
    if unit == 'Unidade 1':
        if month == 'Abril':
            heatmap_data = heatmap_data_abril_unidade1
        else:
            heatmap_data = heatmap_data_maio_unidade1
    else:
        if month == 'Abril':
            heatmap_data = heatmap_data_abril_unidade2
        else:
            heatmap_data = heatmap_data_maio_unidade2
    
    fig = go.Figure(data=go.Heatmap(z=heatmap_data, text=days_numbers, colorscale='blues'))
    fig.update_layout(
        title={
            'text': f"{month} - {unit}",
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
    fig.update_traces(textfont=dict(color='black'))
    return fig

# Definindo os dados do gráfico de linha
horas_do_dia = np.arange(6, 24)  # Horas de funcionamento: 6h às 23h
quantidade_de_pessoas_por_hora = [30, 70, 80, 75, 70, 60, 50, 40, 30, 25, 25, 30, 70, 100, 140, 130, 160, 170, 180, 167, 100, 50, 100, 20]

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
                html.H2("15", className="body-do-painel-texto")  # Quantidade de funcionários ativos
            ]),
            html.Div(className="painel-lateral", style={'marginTop': '20px'}, children=[
                html.Label("Selecione o Mês:", className="dropmes"),
                dcc.Dropdown(
                    id='month-dropdown',
                    options=[
                        {'label': 'Janeiro', 'value': 'Janeiro'},
                        {'label': 'Fevereiro', 'value': 'Fevereiro'},
                        {'label': 'Março', 'value': 'Março'},
                        {'label': 'Abril', 'value': 'Abril'},
                        {'label': 'Maio', 'value': 'Maio'},
                        {'label': 'Junho', 'value': 'Junho'},
                        {'label': 'Julho', 'value': 'Julho'},
                        {'label': 'Agosto', 'value': 'Agosto'},
                        {'label': 'Setembro', 'value': 'Setembro'},
                        {'label': 'Outubro', 'value': 'Outubro'},
                        {'label': 'Novembro', 'value': 'Novembro'},
                        {'label': 'Dezembro', 'value': 'Dezembro'},
                    ],
                    value='Maio',
                    clearable=False,
                    className='lateral-dropdown'
                ),
                html.Label("Selecione a Unidade:", className="dropmes", style={'marginTop': '20px'}),
                dcc.Dropdown(
                    id='unit-dropdown',
                    options=[
                        {'label': 'Unidade 1', 'value': 'Unidade 1'},
                        {'label': 'Unidade 2', 'value': 'Unidade 2'}
                    ],
                    value='Unidade 1',
                    clearable=False,
                    className='lateral-dropdown'
                ),
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
        dcc.Graph(id='heatmap', figure=create_heatmap('Maio', 'Unidade 1'))
    ]),
    html.Div(className="grafico-de-linha", children=[
        dcc.Graph(figure=fig_linha)
    ]),
    html.Div(className="nao-definido", children=[
        html.Label("PRODUTOS MAIS VENDIDOS:", className="body-do-painel-texto"),
        html.Ul(style={'textAlign': 'left'}, children=[
            html.Li(produto) for produto in produtos_mais_vendidos
        ])
    ])
])

# Callback para atualizar o gráfico de calor com base na seleção do mês e da unidade
@app.callback(
    Output('heatmap', 'figure'),
    Input('month-dropdown', 'value'),
    Input('unit-dropdown', 'value')
)
def update_heatmap(selected_month, selected_unit):
    return create_heatmap(selected_month, selected_unit)

# Função de callback para atualizar o contador
@app.callback(Output('contador-texto', 'children'), [Input('interval-component', 'n_intervals')])
def update_counter(n):
    # Retorna o valor do contador como o número de segundos desde o início do aplicativo
    return str(n)

if __name__ == '__main__':
    app.run_server(debug=True)