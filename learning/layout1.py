# -*- coding: utf-8 -*-

# app library
import dash
# has a component for every HTML tag
import dash_core_components as dcc
# offers higher-level, interactive components that are generated 
# with JavaScript, HTML, and CSS through the React.js library
import dash_html_components as html 

# launch dash instance
app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='Dash: A web application framework for Python'),

    dcc.Graph(
        id='example-graph',
        # figure in place of children
        figure={
            # plotly
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            # plotly
            'layout': {
                'title': 'Dash Data Visualization'

            }
        }
    )
])

if __name__ == '__main__':
    app.run_server()