import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/dash-stock-ticker-demo.csv')

stock_tickers = df['Stock'].unique()

app.layout = html.Div([
    
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='stock-ticker',
                options=[{'label': i, 'value': i} for i in stock_tickers],
                value='AAPL'
            )
        ],
        style={'width': '48%', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='stock-graphic')
])

@app.callback(
    Output('stock-graphic', 'figure'),
    [Input('stock-ticker', 'value')])
def update_graph(ticker):
    dff=df[df['Stock'] == ticker]

    fig = px.line(dff, x='Date', y='Close')

    fig.update_xaxes(showgrid=False)

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    fig.update_xaxes(title='Time') 
    fig.update_yaxes(title='Price($)') 

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)