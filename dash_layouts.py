## Dash layout

## libraries
import dash
from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px
import dash_bootstrap_components as dbc

#import dash_html_components as html 
#import dash_core_components as dcc


## app initialisation
app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])


df = px.data.gapminder().query("country=='India'")
df2 = px.data.gapminder().query("country=='United States'")


def bar_chart(df,df2):
    
    fig = go.Figure([go.Bar(x = df['year'], y = df['gdpPercap'], marker_color = 'indianred',name = 'India'),
                     go.Bar(x = df2['year'], y = df2['gdpPercap'], marker_color = 'blue', name = 'US')
                     ])
    
    fig.update_layout(title = 'GDP per capita over the years',
                      xaxis_title = 'Years',
                      yaxis_title = 'GDP per capita', 
                       barmode = 'group'
                      )

    return fig  

    
def line_chart(df, df2):
    fig = go.Figure(data = [go.Scatter(x = df['year'], y = df['lifeExp'],\
                                       line = dict(color = 'firebrick', width = 4), text = df['country'], name = 'India'),
                            go.Scatter(x = df2['year'], y = df2['lifeExp'],\
                                       line = dict(color = 'firebrick', width = 4), text = df2['country'], name = 'US')])
    
        
    fig.update_layout(title='Life Expectency over the years',
                       xaxis_title='Years',
                       yaxis_title='Life Expectancy (years)',
                       )


    return fig 


app.layout = dbc.Container([
                    dbc.Row([dbc.Col([html.H1(id="h1",children="Styling using bootstrap components")],xl=12,lg=12,md = 12,sm=12,xs = 12)],style={'textAlign':'center','marginTop':30}),
                    dbc.Row([dbc.Col([dcc.Graph(id = 'bar_plot',figure = bar_chart(df, df2))],xl=6,lg=6,md = 6,sm=12,xs = 12),
                            dbc.Col([dcc.Graph(id = 'line_plot', figure = line_chart(df, df2))],xl=6,lg=6,md = 6,sm=12,xs = 12)
                            ])



                    ],fluid=True)


# html.Div(id = "Parent",
#                      children= [html.H1(id="h1",children="styling using html components",style={'textAlign':'center'}),
#                                 html.Div(id="bar_div",children=[dcc.Graph(id="bar_plot",figure=bar_chart(df,df2))],style = {'width':'50%','display':'inline-block'}),
#                                 html.Div(id="line_div",children=[dcc.Graph(id="line_plot",figure=line_chart(df, df2))],style = {'width':'50%','display':'inline-block'})     
#                     ])



if __name__ == '__main__':
    app.run_server(debug=True)