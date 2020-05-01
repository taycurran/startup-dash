import dash
import dash_html_components as html 

app = dash.Dash()

app.layout = html.Div([
    'This is the outermost Div',
    html.Div(
        'This is an inner Div',
        style={'color':'blue', 'border':'2px blue solid', 'borderRadius': 10,
        'padding': 10, 'width': 220}
    ),
    html.Div(
        'This is another inner Div.',
        style={'color': 'green', 'border':'2px green solid',
        'margin': 10, 'width':220}
    ),
],
# This Styles the Outermost Div
style={'width':700, 'height':200, 'color':'red', 'border':'2px red dotted'})

if __name__ == '__main__':
    app.run_server()