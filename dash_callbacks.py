
import dash
from dash import html,dcc,Input,Output,State
import plotly.express as px
import numpy as np
import pandas as pd

df = px.data.gapminder()
options_all = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'India': ['Delhi', 'Mumbai', 'Bangalore']
}
city_df=pd.DataFrame(options_all)


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
                    dcc.Graph(id='scatter-plot') ,

                    html.Br(),
                    html.Br(),
                    html.H3("State Call backs"),
                    
                    dcc.Input(id='input-1-state',value="India",type="text"),
                    dcc.Input(id="input-2-state",type="text",value="usa"),
                    html.Button(id="submit-state",n_clicks=0,children='Submit'),
                    html.Div(id='Output-state'),

                    html.Br(),
                    html.Br(),
                    html.H3("Multi chain Call backs"),
                    dcc.Dropdown(id = "country-drpDown", 
                                options =[{'label':i,'value':i}  for i in city_df.columns],
                                value = 'India'),
                    html.Br(),
                    dcc.Dropdown(id="city-dropDwn"),
                    html.Br(),
                    html.Div(id="display-country-city")
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


@app.callback(Output(component_id ='Output-state',component_property='children'),
             [Input(component_id='submit-state',component_property='n_clicks'),
             State(component_id='input-1-state',component_property='value'),
             State(component_id='input-2-state',component_property='value')
             ])
def update_state_text(n_clicks,text1, text2):
    return '''The button is pressed {} times,
    Input 1 is {} and
    Input 2 is {}
    '''.format(n_clicks,text1,text2)


@app.callback(Output(component_id='city-dropDwn',component_property='options'),
              Input(component_id='country-drpDown',component_property='value'))
def update_city_dropdown(countryValue):
    return [{'label':i, 'value':i} for i in city_df['{}'.format(countryValue)]]


@app.callback(Output(component_id='city-dropDwn',component_property='value'),
             [Input(component_id='city-dropDwn',component_property='options')])
def set_state_value(state_options):
    return state_options[0]['value']


@app.callback(Output(component_id="display-country-city",component_property='children'),
             [Input(component_id='country-drpDown',component_property='value'),
             Input(component_id='city-dropDwn',component_property='value')])
def update_display_details(countryValue,cityValue):
    return "Country {} and city {}".format(countryValue,cityValue)




if __name__ == '__main__':
    app.run_server(debug=False)