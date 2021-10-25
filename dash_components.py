import dash
from dash import  dcc, html, dash_table
import pandas as pd
from datetime import datetime as dt


app = dash.Dash()

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/multiple_y_axis.csv")

table = dash_table.DataTable(
                data= df.to_dict("records"),
                columns= [{'id':c, 'name':c} for c in df.columns],
                fixed_rows = {'headers':True},
    
                style_table = {'maxHeight':'450px'},
                
                style_header = {'backgroundColor':'rgb(224,224,224)',
                                'fontWeight':'bold',
                                'border':'4px solid white'},
                  style_cell = {
                            'textAlign':'center',
                            'border':'4px solid white',
                            'maxWidth':'50px',
                            # 'whiteSpace':'normal'
                            'textOverflow':'ellipsis'}
    
        )


app.layout = html.Div([
               html.Div(id= "dropdown-div",
                    children = [dcc.Dropdown(id='dropdown',
                        options=[{'label':'amazing','value':5},
                                 {'label':'good','value':3},
                                 {'label':'bad','value':1,'disabled':True}
                                ],
                        value='amazing',
                        placeholder="select any rating",
                        multi= True
                )],style = {'width':'30%'}),
            
            html.Br(),

            dcc.Slider( id = 'slider', min = 0,  max = 10,step = 1,value = 0,
                        marks = {i : '{}'.format(i) for i in range(11)}),

            html.Br(),

            dcc.Input(id = 'input',
             type = 'text',
             placeholder = 'Enter your text',
             value = '',
             debounce = True
             ),

             html.Br(),

            dcc.Checklist(id = 'checklist',
                          options = [
                                {'label':'amazing', 'value':'5' },
                                {'label': 'average', 'value':'3'},
                                {'label':'below average', 'value':'1','disabled':True} 
                             ],
                            value = ['5','3'],
                            ),
   
            html.Br(),
            
            dcc.DatePickerRange(id = 'date_pick_range',
                                start_date = dt(1997,5,3),
                                # end_date_placeholder_text = 'Select a date'
                                min_date_allowed = dt(1995,8,5),
                                max_date_allowed = dt(2017,9,19),
                                end_date = dt(2017,8,25)
                                ),

            dcc.Markdown(id = 'markdown', children = ['''
                        ## Dash and Markdown

                        Dash supports [Markdown](http://commonmark.org/help).

                        Markdown is a simple way to write and format text.
                        It includes a syntax for things like **bold text** and *italics*,
                        [links](http://commonmark.org/help), inline `code` snippets, lists,
                        quotes, and more.''']),

            html.Div(id = 'table_div', children = [table])
            
            ])




if __name__ == '__main__':
    app.run_server(debug=True)