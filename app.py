from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

app = Dash(__name__)

# Função para criar um gráfico de exemplo
def create_graph(start_date, end_date):
    # Criar um DataFrame de exemplo
    df = pd.DataFrame({
        'Date': pd.date_range(start_date, end_date),
        'Value': [i for i in range((end_date - start_date).days + 1)]
    })

    # Criar um gráfico de linha
    graph = dcc.Graph(
        figure={
            'data': [
                go.Scatter(
                    x=df['Date'],
                    y=df['Value'],
                    mode='lines+markers'
                )
            ],
            'layout': {
                'title': 'Exemplo de Gráfico de Linha',
                'xaxis': {'title': 'Data'},
                'yaxis': {'title': 'Valor'}
            }
        }
    )

    return graph

# Layout do Dash com o link para o arquivo CSS externo
app.layout = html.Div(className="body", children=[
    html.Link(rel='stylesheet', href='/assets/styles.css'),
    html.Div(
        className="header",
        children=[
            html.H1('SMARTCOUNT', className="header-logo"),
        ]
    ),

    html.Div(
        className="body-do-painel",
        children=[
            html.Img(
                src="./assets/imagens/contabilidade.png", alt="logo", className='logo'),
                            html.Div( className="notificacao", children=[
                html.H3(
                children='Notificações', className="body-do-painel-texto"),
                html.Img(
                src="./assets/imagens/sino.png", alt="sino", className='sino'),
            ]),  # Espaçamento entre os dropdowns

            html.H3(
                children='Selecione para filtrar:', className="body-do-painel-texto"),



            # Dropdown seleção do ano
            html.Div(
                className="painel-lateral",
                children=[
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
                ],
            ),
            html.Div(style={"margin-bottom": "20px"}),  # Espaçamento entre os dropdowns

            # Dropdown seleção do ano
            html.Div(
                className="painel-lateral",
                id='base-dados-dropdown',
                children=[
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
                ],
            ),
        ]
    ),
    html.Div(
        className="contador",
        children=[
            html.Label("Contador"),
        ]
    ),
        html.Div(
        className="nao-definido",
        children=[
            html.Label(""),
        ]
    ),
    
        html.Div(
        className="calendario",
        children=[
            html.Label("calendario"),
        ]
    ),

        html.Div(
        className="grafico",
        children=[
            html.Label("grafico"),
        ]
    ),
    
])
if __name__ == '__main__':
    app.run_server(debug=True)
