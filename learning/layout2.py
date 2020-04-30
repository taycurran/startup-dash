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

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

#The children of an HTML tag are 
# specified through the children keyword argument. 
app.layout = html.Div(children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(
        children='Dash: A web application framework for Python.',
        #The style property in HTML is a semicolon-separated string. 
        # In Dash, you can just supply a dictionary.
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                },
                'title': 'Dash Data Visualization'
            }
        }
    )],
    style={'backgroundColor': colors['background']}
)

if __name__ == '__main__':
    app.run_server()
