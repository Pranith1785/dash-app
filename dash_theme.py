import dash
from dash import html, Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG, dbc.themes.MINTY])

# Use this to find the url to use in the clientside callback
print(dbc.themes.CYBORG)
print(dbc.themes.MINTY)


switch = dbc.Form(
    [
        dbc.Label("Select theme"),
        dbc.Checklist(
            options=[{"label": "dark theme", "value": 1},],
            value=[],
            id="switch",
            switch=True,
        ),
    ]
)

buttons = html.Div(
    [
        dbc.Button("Primary", color="primary", className="mr-1"),
        dbc.Button("Secondary", color="secondary", className="mr-1"),
        dbc.Button("Success", color="success", className="mr-1"),
        dbc.Button("Warning", color="warning", className="mr-1"),
        dbc.Button("Danger", color="danger", className="mr-1"),
        dbc.Button("Info", color="info", className="mr-1"),
        dbc.Button("Light", color="light", className="mr-1"),
        dbc.Button("Dark", color="dark", className="mr-1"),
        dbc.Button("Link", color="link"),
    ],
    className="m-4",
)

alerts = html.Div(
    [
        dbc.Alert("This is a primary alert", color="primary"),
        dbc.Alert("This is a secondary alert", color="secondary"),
        dbc.Alert("This is a success alert! Well done!", color="success"),
        dbc.Alert("This is a warning alert... be careful...", color="warning"),
    ]
)

"""
===============================================================================
Layout
"""
app.layout = dbc.Container(
    dbc.Row(
        [
            dbc.Col(switch, width=3),
            dbc.Col([buttons, alerts]),
            html.Div(id="blank_output"),
        ],
    ),
    className="m-4",
    fluid=True,
)


# Using 2 stylesheets with the delay reduces the annoying flicker when the theme changes
app.clientside_callback(
    """
    function(selected) {

        let url = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/minty/bootstrap.min.css"
        if (selected.length > 0) {
            url= "https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/cyborg/bootstrap.min.css"
        }

        // Select the theme stylesheets .
        var stylesheets = document.querySelectorAll('link[rel=stylesheet][href^="https://stackpath"]')
        // Update the url of the main stylesheet.
        stylesheets[stylesheets.length - 1].href = url
        // Delay update of the url of the buffer stylesheet.
        setTimeout(function() {stylesheets[0].href = url;}, 100);
    }
    """,
    Output("blank_output", "children"),
    Input("switch", "value"),
)

if __name__ == "__main__":
    app.run_server(debug=True)