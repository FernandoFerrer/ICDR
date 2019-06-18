# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 21:20:18 2019

@author: reeff
"""
#Import packages:
import dash,copy
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import base64
import os
import plotly.graph_objs as go
import dash_daq as daq

#Import pages:
from Home import Home
from Retinography_Visualization import Retinography_Visualization
from Diagnosis_Assistant import Diagnosis_Assistant
from References import References
from Contact import Contact

app = dash.Dash(__name__)
app.title='ICDR'
server = app.server
directory = os.getcwd()

"############################ Navigation Menu ################################"
nav_menu = html.Div([
    html.Ul([
            
            html.Li([
                    dcc.Link('AAAAA', href='/Home',
                             
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
                    dcc.Link('Retinography Visualization', href='/Retinography-Visualization')
                    ],

                    style = {
                             'margin':'0',
                             'padding':'0'
                             },

                    className=''),

            html.Li([
                    dcc.Link('Diagnosis Assistant', href='/Diagnosis-Assistant')
                    ],
            
                    style = {
                             'margin':'0',
                             'padding':'0'
                             },
            
                    className=''),
            
            
            html.Li([
                    dcc.Link('References', href='/References')
                    ],
            
                    style = {
                             'margin':'0',
                             'padding':'0'
                             },
            
                    className=''),
            
            
            html.Li([
                    dcc.Link('Contact', href='/Contact')
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
         'padding':'0',
         'box-shadow':'5px 1px 10px 1px grey'}
)
"#############################################################################"

app.layout = html.Div([

    dcc.Location(id='url', refresh=False),
    
    nav_menu,
    
    
    html.Div( [
            
            #Page Home: ----------------------------------------------------------
            html.Div([
                    
                    Home,
                      
            ], id = 'Home' ),
               
               
           #Page Retinograpy-Visualization: -----------------------------------------------------------    
           html.Div([
                   
                   Retinography_Visualization,
                                      
           ],
            style={
                   'padding':'0',
                   'margin':'0'},
                    
            id = 'Retinography-Visualization' ),
           
        
           #Page Diagnosis-Assistant: -----------------------------------------------------------
           html.Div([
                   
                   Diagnosis_Assistant,
                   
           ], id = 'Diagnosis-Assistant'),
            
            
           #Page References: -----------------------------------------------------------
           html.Div([
                   
                   References,
                   
           ],
           id = 'References' ),
            
           #Page Contact: -----------------------------------------------------------
           html.Div([
                   
                   Contact,
                   
           ], id = 'Contact' ), 
            

            
        ],style = {'display':'block'}),
               
],
style={'background-image':'url(/assets/background.PNG/)',
       'height':'100vh',
       'background-size':'cover'}
)
           
"############### Callbacks for Retinography Visualization ####################"
#Callback to hidden division:
@app.callback(
    dash.dependencies.Output('Image_Classification','children'),
    [dash.dependencies.Input('dropdown-4','value')] #Batch
    )
def get_image_class(idImage):
    from App_Functions import get_image_classifications
    classifications=get_image_classifications(idImage)
    return classifications.to_json(orient='split')

#Callbacks to indicators:
@app.callback(
    dash.dependencies.Output('Gauge-1','value'),
    [dash.dependencies.Input('Image_Classification','children')] #Batch
    )    
def get_diabetic_retinopathy_grade(json_classification):
    import pandas as pd
    classification=pd.read_json(json_classification,orient='split')
    drg=classification['Retinopathy_Grade'][0]
    return int(drg)

@app.callback(
    dash.dependencies.Output('Gauge-2','value'),
    [dash.dependencies.Input('Image_Classification','children')] #Batch
    )    
def get_macular_edema_grade(json_classification):
    import pandas as pd
    classification=pd.read_json(json_classification,orient='split')
    meg=classification['Macular_Edema_Grade'][0]
    return int(meg)

@app.callback(
    dash.dependencies.Output('Gauge-3','value'),
    [dash.dependencies.Input('Image_Classification','children')] #Batch
    )    
def get_combined_grade(json_classification):
    import pandas as pd
    classification=pd.read_json(json_classification,orient='split')
    cg=classification['Classification'][0]
    return int(cg)
    
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
    figure1=get_surface_plot(image)
    return figure1

#Retinography Plot 2D:
@app.callback(
    dash.dependencies.Output('retinography-plot2D','figure'),
    [dash.dependencies.Input('dropdown-4','value')]
)
def get_2D_plot(idImage):
    from App_Functions import get_2D_Img
    import time
    try:
        figure2=get_2D_Img(idImage)
    except:
        time.sleep(3)
        figure2=get_2D_Img(idImage)
    return figure2

"################### Callbacks for Diagnosis Assistant #######################"
@app.callback(Output('output-image-upload', 'src'),
              [Input('upload-image', 'contents')])
def update_output(content):
    return content
          
@app.callback([Output('Prediction','children'),
               Output('Confidence','children'),
               Output('Category','children')],
              [Input('output-image-upload','src')])
def get_predictions_from_src(src):
    from App_Functions import get_predictions
    predictions=get_predictions(src)
    return predictions[0], predictions[1], predictions[2]

@app.callback(Output('conf-indicator','value'),
              [Input('Confidence', 'children')])
def update_conf_indicator(conf):
    conf_num=float(conf)*10
    return conf_num
 
"###################### Callbacks for Navigation Bar #########################"
@app.callback(
    Output(component_id='Home', component_property='style'),
    [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Home':
        return {'display': 'block'}
    else:
        return {'display': 'none'}

@app.callback(
    Output(component_id='Retinography-Visualization', component_property='style'),
    [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Retinography-Visualization':
        return {'display': 'block'}
    else:
        return {'display': 'none'}
    
@app.callback(
    Output(component_id='Diagnosis-Assistant', component_property='style'),
    [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Diagnosis-Assistant':
        return {'display': 'block'}
    else:
        return {'display': 'none'}
    
@app.callback(
    Output(component_id='References', component_property='style'),
    [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/References':
        return {'display': 'block'}
    else:
        return {'display': 'none'}
    
@app.callback(
    Output(component_id='Contact', component_property='style'),
    [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Contact':
        return {'display': 'block'}
    else:
        return {'display': 'none'}

app.css.append_css({"external_url": [
    "https://codepen.io/chriddyp/pen/bWLwgP.css",
    "https://codepen.io/chriddyp/pen/rzyyWo.css",
    "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css",
    "https://codepen.io/chriddyp/pen/brPBPO.css"
]})
               
app.css.config.serve_locally = False

if __name__ == '__main__':
    app.run_server(debug=True)