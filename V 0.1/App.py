# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 21:20:18 2019

@author: reeff
"""

import dash,copy
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import base64
import os

app = dash.Dash(__name__)
app.title='ICDR'
server = app.server
directory = os.getcwd()

#ICDR Logo:
image_filename = directory+'/assets/icon.PNG' #Get the logo image
encoded_image = base64.b64encode(open(image_filename, 'rb').read()) #Encode the logo image

#data:image/png;base64,{}'.format(encoded_image)

"############################ Navigation Menu ################################"
nav_menu = html.Div([
    html.Ul([
            
            html.Li([
                    dcc.Link('AAAAA', href='/page-a',
                             
                             style={'background-image':'url(/assets/icon.PNG/)',
                                    'background-size':'contain',
                                    'background-repeat':'no-repeat',
                                    'background-position':'right 0vh',
                                    'color':'rgba(0,0,0,0)'}
                             ),                    
                    ],
                    style = {
                             'margin':'0',
                             'padding':'0'
                             },
                            
                    className=''),

            html.Li([
                    dcc.Link('Retinograpy Visualization', href='/page-b')
                    ],

                    style = {
                             'margin':'0',
                             'padding':'0'
                             },

                    className=''),

            html.Li([
                    dcc.Link('Diagnosis Assistant', href='/page-c')
                    ],
            
                    style = {
                             'margin':'0',
                             'padding':'0'
                             },
            
                    className=''),

            ],
            
            style = {'margin':'0',
                     'padding':'0'},
            
            className='nav navbar-nav')
            
], className='navbar navbar-default navbar-static-top',
            
style = {'background-color': 'rgb(111,163,225)',
         'font-size':'3.5vh',
         'margin':'0',
         'padding':'0'}
)
"#############################################################################"

app.layout = html.Div([

    dcc.Location(id='url', refresh=False),
    
    nav_menu,
    
    
    html.Div( [
            
            #Page a: ----------------------------------------------------------
            html.Div([
            
                    html.H4('Welcome to Image Classifier for Diabetic Retinopathy'),
                        
            
            ], id = 'page-a' ),
               
               
           #Page b: -----------------------------------------------------------    
           html.Div([
                   
                   html.H4('Visualize images with different levels of diabetic retinopathy.'),
                   
                   html.Div([
                             dcc.Dropdown(id='dropdown-1',
                                          options=[{'label': i, 'value': i} for i in ['No Retinopathy','Mild Retinopathy','Moderate Retinopathy','Severe Retinopathy']],
                                          placeholder="Select a Retinopathy grade",
                                          style={'background-color': 'rgba(255,255,255,0.5)'},
                                          ),
                                          
                             dcc.Dropdown(id='dropdown-2',
                                          options=[{'label': i, 'value': i} for i in ['No Macular Edema','Moderate Macular Edema','Severe Macular Edema']],
                                          placeholder="Select a macular edema grade",
                                          style={'background-color': 'rgba(255,255,255,0.5)'},
                                          ),
                           
                             dcc.Dropdown(id='dropdown-3',
                                          options=[{'label': i, 'value': i} for i in ['No Risk','Moderate Risk','Severe Risk']],
                                          placeholder="Select a combined grade",
                                          style={'background-color': 'rgba(255,255,255,0.5)'},
                                          ),
                                          
                             dcc.Dropdown(id='dropdown-4',
                                          placeholder="Select an image number",
                                          style={'background-color': 'rgba(255,255,255,0.5)'},
                                          ),
                                          
                           ],
                            style={'width':'20%',
                                   'font-family':'sans-serif'}
                            ),
            
                #Retinograpy Plot:
                html.Div([
                         dcc.Graph(id='retinography-plot',
                                       style={'margin': '0 auto'}),
                        ]),
                   
                                      
           ], id = 'page-b' ),
           
        
           #Page c: -----------------------------------------------------------
           html.Div([
                   
                   html.H4('Diagnosis Assistant')
                   
           ], id = 'page-c' )],
                    
                    
                    
                
          style = {'display':'block'}),
               
],
style={'background-image':'url(/assets/background.PNG/)',
       'height':'100vh',
       'background-size':'cover'}
)

#Options for image numbers:
@app.callback(
    dash.dependencies.Output('dropdown-4','options'),
    [dash.dependencies.Input('dropdown-1','value'), 
     dash.dependencies.Input('dropdown-2','value'), 
     dash.dependencies.Input('dropdown-3','value'), 
    ]
)
def image_numbers(retinopathy_grade,macular_edema_grade,combined_grade):
    from App_Functions import get_images_ids
    list_ids=get_images_ids(retinopathy_grade,macular_edema_grade,combined_grade)
    return [{'label': i, 'value': i} for i in list_ids]

#Retinography Plot:
@app.callback(
    dash.dependencies.Output('retinography-plot','figure'),
    [dash.dependencies.Input('dropdown-4','value')]
)
def get_surface(idImage):
    from App_Functions import get_retinography_image, get_surface_plot
    image=get_retinography_image(idImage)
    figure=get_surface_plot(image)
    return figure

@app.callback(
    Output(component_id='page-a', component_property='style'),
    [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-a':
        return {'display': 'block'}
    else:
        return {'display': 'none'}

@app.callback(
    Output(component_id='page-b', component_property='style'),
    [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-b':
        return {'display': 'block'}
    else:
        return {'display': 'none'}
    
@app.callback(
    Output(component_id='page-c', component_property='style'),
    [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-c':
        return {'display': 'block'}
    else:
        return {'display': 'none'}
    


app.css.append_css({"external_url": [
    "https://codepen.io/chriddyp/pen/bWLwgP.css",
    "https://codepen.io/chriddyp/pen/rzyyWo.css",
    "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
]})

if __name__ == '__main__':
    app.run_server(debug=True)