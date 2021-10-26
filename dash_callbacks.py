
import dash
from dash import html,dcc,Input,Output


app = dash.Dash()

app.layout = html.Div(id = "parent-div",children=[
                    html.H2(id='h3',children= "Call backs example"),
                    html.Br(),
                    dcc.Dropdown(id="dropdown",
                                options=[
                                    { 'label': 'amazing','value':5}, 
                                    {'label':'average','value':3},
                                     {'label':'below average', 'value':1}
                                    ],
                                value= 5),
                    html.Br(),
                    html.Div(id = "output-text")
                ])

@app.callback(Output(component_id="output-text",component_property='children'), 
              Input(component_id="dropdown",component_property='value')
              )
def getDropdownSelection(input_value):
    return html.Div(input_value)





if __name__ == '__main__':
    app.run_server(debug=True)