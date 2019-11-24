# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 21:20:18 2019

@author: reeff
"""
#Import packages:
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import os
import plotly.graph_objs as go
import pandas as pd

#Import pages:
from Home import Home
from Retinography_Visualization import Retinography_Visualization
from Diagnosis_Assistant import Diagnosis_Assistant
from References import References
from Contact import Contact

app = dash.Dash(__name__)
app.title='ACRIA'
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
                    dcc.Link('Visualizador de retinografías', href='/Retinography-Visualization')
                    ],

                    style = {
                             'margin':'0',
                             'padding':'0'
                             },

                    className=''),

            html.Li([
                    dcc.Link('Asistente de clasificación', href='/Diagnosis-Assistant')
                    ],
            
                    style = {
                             'margin':'0',
                             'padding':'0'
                             },
            
                    className=''),
            
            
            html.Li([
                    dcc.Link('Referencias', href='/References')
                    ],
            
                    style = {
                             'margin':'0',
                             'padding':'0'
                             },
            
                    className=''),
            
            
            html.Li([
                    dcc.Link('Contacto', href='/Contact')
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

    dcc.Location(id='url',refresh=False,pathname='/Home'),
    
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
     Output('Image_Classification','children'),
    [Input('dropdown-4','value')] #Batch
    )
def get_image_class(idImage):
    from App_Functions import get_image_classifications
    if idImage is not None:
        classifications=get_image_classifications(idImage)
        return classifications.to_json(orient='split')
    else:
        return '0'

#Callbacks to indicators:
@app.callback(
     Output('Gauge-1','value'),
    [Input('Image_Classification','children')] #Batch
    )    
def get_diabetic_retinopathy_grade(json_classification): 
    if json_classification!='0':
        classification=pd.read_json(json_classification,orient='split')
        drg=classification['Retinopathy_Grade'][0]
        return int(drg)
    else:
        return 0

@app.callback(
     Output('Gauge-2','value'),
    [Input('Image_Classification','children')] #Batch
    )    
def get_macular_edema_grade(json_classification):
    if json_classification!='0':
        classification=pd.read_json(json_classification,orient='split')
        meg=classification['Macular_Edema_Grade'][0]
        return int(meg)
    else:
        return 0

@app.callback(
     Output('Gauge-3','value'),
    [Input('Image_Classification','children')] #Batch
    )    
def get_combined_grade(json_classification):
    if json_classification!='0':
        classification=pd.read_json(json_classification,orient='split')
        cg=classification['Classification'][0]
        return int(cg)
    else:
        return 0
    
#Options for image numbers:
@app.callback(
     Output('dropdown-4','options'),
    [Input('dropdown-1','value'), 
     Input('dropdown-2','value'), 
     Input('dropdown-3','value'), 
    ]
)
def image_numbers(retinopathy_grade,macular_edema_grade,combined_grade):
    from App_Functions import get_images_ids
    list_ids=get_images_ids(retinopathy_grade,macular_edema_grade,combined_grade)
    return [{'label': i, 'value': i} for i in list_ids]

#Retinography Plot:
@app.callback(
    [Output('retinography-plot','figure'),
     Output('retinography-plots-div','style')],
    [Input('dropdown-4','value')]
)
def get_surface(idImage):
    from App_Functions import get_retinography_image, get_surface_plot
    if idImage is not None:
        image=get_retinography_image(idImage)
        figure1=get_surface_plot(image)
        return figure1,{'display':'block'}
    else:
        return go.Figure(),{'display':'none'}

#Retinography Plot 2D:
@app.callback(
     Output('retinography-plot2D','figure'),
    [Input('dropdown-4','value')]
)
def get_2D_plot(idImage):
    from App_Functions import get_2D_Img
    import time
    if idImage is not None:
        try:
            figure2=get_2D_Img(idImage)
        except:
            time.sleep(3)
            figure2=get_2D_Img(idImage)
        return figure2
    else:
        return go.Figure()
        
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
    if src is not None:
        predictions=get_predictions(src)
        return predictions[0], predictions[1], predictions[2]
    else:
        return '0','0','0'

@app.callback(Output('conf-indicator','value'),
              [Input('Confidence','children')])
def update_conf_indicator(conf):
    if conf is not None:
        conf_num=float(conf)*10
        return conf_num
    else:
        return 0
 
"###################### Callbacks for Navigation Bar #########################"
@app.callback(
    Output(component_id='Home', component_property='style'),
    [Input('url', 'pathname')])
def display_page0(pathname):
    if pathname == '/Home':
        return {'display': 'block'}
    else:
        return {'display': 'none'}

@app.callback(
    Output(component_id='Retinography-Visualization', component_property='style'),
    [Input('url', 'pathname')])
def display_page1(pathname):
    if pathname == '/Retinography-Visualization':
        return {'display': 'block'}
    else:
        return {'display': 'none'}
    
@app.callback(
    Output(component_id='Diagnosis-Assistant', component_property='style'),
    [Input('url', 'pathname')])
def display_page2(pathname):
    if pathname == '/Diagnosis-Assistant':
        return {'display': 'block'}
    else:
        return {'display': 'none'}
    
@app.callback(
    Output(component_id='References', component_property='style'),
    [Input('url', 'pathname')])
def display_page3(pathname):
    if pathname == '/References':
        return {'display': 'block'}
    else:
        return {'display': 'none'}
    
@app.callback(
    Output(component_id='Contact', component_property='style'),
    [Input('url', 'pathname')])
def display_page4(pathname):
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
               
app.scripts.config.serve_locally=True

if __name__ == '__main__':
    app.run_server(debug=True)