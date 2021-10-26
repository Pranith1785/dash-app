
import dash
from dash import html,dcc,Input,Output
import plotly.express as px
import numpy as np

df = px.data.gapminder()


fig = px.scatter(df,x="gdpPercap",y="lifeExp",
                 size = "pop",color='continent',hover_name='country',
                 log_x=True,size_max=55,
                 range_x=[100,100000],range_y = [25,90]
                 )


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
                    html.Div(id = "output-text"),
                    html.Button(id="button-div",children="Click here",n_clicks=0),
                    html.Br(),
                    html.Div(id="output-clicks"),

                    dcc.Slider(id="year-slider",
                                min=df['year'].min(),
                                max=df['year'].max(),
                                value=df['year'].min(),
                                marks = {str(year): str(year) for year in df['year'].unique()},
                                step=None
                                ),
                    
                    dcc.Dropdown(id = "dropdown-con", 
                                options=[{ 'label':i,'value':i} for i in np.append(['All'],df['continent'].unique())],
                                value = 'All'
                                ),

                    html.Div(id = 'filters-selected', style = {'textAlign':'center'}),

                    dcc.Graph(id='scatter-plot')         
                    
                    
                ])

@app.callback(Output(component_id="output-text",component_property='children'), 
              Input(component_id="dropdown",component_property='value')
              )
def getDropdownSelection(input_value):
    return html.Div(input_value)


@app.callback(Output(component_id = "output-clicks",component_property='children'),
             Input(component_id = "button-div",component_property="n_clicks")
            )
def getButtonClick(value):
    return html.Div(str(value) + " clicks")



@app.callback([Output(component_id = "filters-selected",component_property='children'),
             Output(component_id = "scatter-plot",component_property="figure")],
             [Input(component_id = 'year-slider',component_property = 'value'),
             Input(component_id = 'dropdown-con',component_property = 'value')]
             )
def update_scatterPlot(sliderValue,dropDownValue):

    if dropDownValue == 'All':
        filtered_df = df.loc[(df.year == sliderValue)]
    else:
        filtered_df = df.loc[(df.year == sliderValue) & (df['continent']== dropDownValue)]

    fig = px.scatter(filtered_df,x="gdpPercap",y="lifeExp",
                 size = "pop",color='continent',hover_name='country',
                 log_x=True,size_max=55,
                 range_x=[100,100000],range_y = [25,90]
                 )

    return html.Div("Selected year {} and continent {}".format(sliderValue,dropDownValue)),fig






if __name__ == '__main__':
    app.run_server(debug=True)