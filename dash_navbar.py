import dash
import  dash_bootstrap_components as dbc
from dash import dcc,html

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

##App
app = dash.Dash(external_stylesheets = [ dbc.themes.DARKLY])


navbar = dbc.Navbar(id='navbar',
                    children = [
                        dbc.Row([
                            dbc.Col(html.Img(src = PLOTLY_LOGO, height = "70px")),
                            dbc.Col(dbc.NavbarBrand("App Title",
                                     style = {'color':'black', 'fontSize':'25px','fontFamily':'Times New Roman'})
                                    )],align = "center"),
                        dbc.Button(id = 'button', children = "Click Me!", color = "primary", className = 'ml-auto')
                    ])


card_content = [
    dbc.CardHeader("Card Header"),
    dbc.CardBody([
            html.H5("Card Title", className = "card-title"),  
            html.P("This is some card content that we will reuse",
                   className = "card-text")
            ])  
    ]


app.layout = html.Div(id = 'parent', children = [navbar,
                             dbc.Row([
                                    dbc.Col(dbc.Card(card_content, color = 'primary', inverse = True)),
                                    dbc.Col(dbc.Card(card_content, color = 'info', inverse = True)),
                                    dbc.Col(dbc.Card(card_content, color = 'secondary', outline = True))
                                 ])
                             ])


if __name__ == '__main__':
    app.run_server(debug=True)