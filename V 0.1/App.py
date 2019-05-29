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
import plotly.graph_objs as go
import dash_daq as daq

app = dash.Dash(__name__)
app.title='ICDR'
server = app.server
directory = os.getcwd()

#ICDR Logo:
image_filename = directory+'/assets/icon.PNG' #Get the logo image
encoded_image = base64.b64encode(open(image_filename, 'rb').read()) #Encode the logo image


"########################### Visual Components ###############################"

#No axis for graph:
noaxis=dict( 
            showbackground=False,
            showgrid=False,
            showline=False,
            showticklabels=False,
            ticks='',
            title='',
            zeroline=False)

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
         'padding':'0'}
)
"#############################################################################"

app.layout = html.Div([

    dcc.Location(id='url', refresh=False),
    
    nav_menu,
    
    
    html.Div( [
            
            #Page Home: ----------------------------------------------------------
            html.Div([
                    
                    
                    html.Div([
                            html.H2('Welcome to Image Classifier for Diabetic Retinopathy',
                            style={'text-align':'center'}
                            ),
                            
                            html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
                                         style = {
                                                  'display':'block',
                                                  'margin':'0 auto',
                                                  },
                                         ),
                            
                            ],
            
                            style={'background-color': 'rgba(183,183,183,0.5)',
                                   },                            
                            ),
                    
                        
            
            ], id = 'Home' ),
               
               
           #Page Retinograpy-Visualization: -----------------------------------------------------------    
           html.Div([
                                      
                   html.Div([
                             dcc.Dropdown(id='dropdown-1',
                                          options=[{'label': i, 'value': i} for i in ['No Retinopathy','Mild Retinopathy','Moderate Retinopathy','Severe Retinopathy','Proliferative Retinopathy']],
                                          placeholder="Select a Retinopathy grade",
                                          style={'background-color': 'rgba(255,255,255,0.5)',
                                                 'width':'15vw',
                                                 'display':'inline-block',
                                                 'vertical-align':'top'},
                                          ),
                                          
                             dcc.Dropdown(id='dropdown-2',
                                          options=[{'label': i, 'value': i} for i in ['No Macular Edema','Moderate Macular Edema','Severe Macular Edema']],
                                          placeholder="Select a macular edema grade",
                                          style={'background-color': 'rgba(255,255,255,0.5)',
                                                 'width':'15vw',
                                                 'display':'inline-block',
                                                 'vertical-align':'top'},
                                          ),
                           
                             dcc.Dropdown(id='dropdown-3',
                                          options=[{'label': i, 'value': i} for i in ['No Risk','Moderate Risk','Severe Risk']],
                                          placeholder="Select a combined grade",
                                          style={'background-color': 'rgba(255,255,255,0.5)',
                                                 'width':'15vw',
                                                 'display':'inline-block',
                                                 'vertical-align':'top'},
                                          ),
                                          
                             dcc.Dropdown(id='dropdown-4',
                                          placeholder="Select an image number",
                                          style={'background-color': 'rgba(255,255,255,0.5)',
                                                 'width':'15vw',
                                                 'display':'inline-block',
                                                 'vertical-align':'top'},
                                          ),
                                          
                             html.H4('Space',
                                     style={'display':'inline-block',
                                            'color':'rgba(0,0,0,0)'},
                                     ),
                                          
                             daq.Gauge( id='Gauge-1',
                                        color={"gradient":True,"ranges":{"green":[0,2],"yellow":[2,3],"red":[3,4]}},
                                        label='Diabetic Retinopathy',
                                        scale={'start': 0, 'interval': 1, 'labelInterval': 1},
                                        size=100,
                                        max=4,
                                        min=0,
                                        style={'display':'inline-block',
                                               'padding':'0',
                                               'margin':'0'},
                                        ),
                                     
                             daq.Gauge( id='Gauge-2',
                                        color={"gradient":True,"ranges":{"green":[0,1],"yellow":[1,1],"red":[1,2]}},
                                        label='Macular Edema',
                                        scale={'start': 0, 'interval': 1, 'labelInterval': 1},
                                        size=100,
                                        max=2,
                                        min=0,
                                        style={'display':'inline-block',
                                               'padding':'0',
                                               'margin':'0'},
                                        ),
                                     
                             daq.Gauge( id='Gauge-3',
                                        color={"gradient":True,"ranges":{"green":[0,1],"yellow":[1,1],"red":[1,2]}},
                                        label='Combined Grade',
                                        scale={'start': 0, 'interval': 1, 'labelInterval': 1},
                                        size=100,
                                        max=2,
                                        min=0,
                                        style={'display':'inline-block',
                                               'padding':'0',
                                               'margin':'0'},
                                        ),
                           ],
                            style={'width':'100%',
                                   'font-family':'sans-serif',
                                   'padding':'0',
                                   'margin':'0'}
                            ),
                
                html.Div([
                #3D Retinograpy Plot:
                html.Div([
                         dcc.Graph(id='retinography-plot',
                                   style={'margin': '0 auto',
                                          'padding-top':'1px'},
                                   figure={
                                           'layout' : go.Layout(
                                                                 paper_bgcolor='rgba(0,0,0,0)',
                                                                 plot_bgcolor='rgba(0,0,0,0)',
                                                                 autosize=True,
                                                                 height=500,
                                                                 margin=dict(t=2),
                                                                 scene=dict(xaxis=dict(noaxis),
                                                                             yaxis=dict(noaxis), 
                                                                             zaxis=dict(noaxis), 
                                                                             ),
                                                             )
                                           }
                                )
                        ],
            
                        style={
                               'display':'inline-block',
                               'width':'50vw'},
            
                        ),
            
                #2D Retinography Plot:
                html.Div([
                        
                        dcc.Graph(id='retinography-plot2D',
                                  style={'margin': '0 auto',
                                          'padding-top':'1px'},
                                   figure={
                                           'layout' : go.Layout(
                                                                 paper_bgcolor='rgba(0,0,0,0)',
                                                                 plot_bgcolor='rgba(0,0,0,0)',
                                                                 autosize=True,
                                                                 height=500,
                                                                 margin=dict(t=2),
                                                                 scene=dict(xaxis=dict(noaxis),
                                                                             yaxis=dict(noaxis), 
                                                                             zaxis=dict(noaxis), 
                                                                             ),
                                                             )
                                           }
                                  )
                        ],
            
                         style={
                               'display':'inline-block',
                               'width':'40vw',
                               'vertical-align':'top'},
            
                        ), 

                ]),               
                
                #Hidden division to store image classfications:
                html.Div(id='Image_Classification',style={'display': 'none'}),
                   
                                      
           ],
            style={
                   'padding':'0',
                   'margin':'0'},
                    
            id = 'Retinography-Visualization' ),
           
        
           #Page Diagnosis-Assistant: -----------------------------------------------------------
           html.Div([
                   
                   html.H4('Diagnosis Assistant')
                   
           ], id = 'Diagnosis-Assistant'),
            
            
           #Page References: -----------------------------------------------------------
           html.Div([
                   
                     html.Div([
                   
                               html.H3('References'),
                               html.Label(['-Indian Diabetic Retinopathy Image Dataset (IDRiD)  ', html.A('Link', href='https://ieee-dataport.org/open-access/indian-diabetic-retinopathy-image-dataset-idrid', target='_blank')]),
                               html.H4(''),
                               html.Label(['-Decencière et al.. Feedback on a publicly distributed database: the Messidor database. Image Analysis & Stereology, v. 33, n. 3, p. 231-234, aug. 2014. ISSN 1854-5165.  ', html.A('Link 1', href='http://www.ias-iss.org/ojs/IAS/article/view/1155',  target='_blank')]),
                               html.Label(['', html.A('Link 2', href='http://dx.doi.org/10.5566/ias.1155',  target='_blank')]),
                               html.H4(''),
                               html.Label(['-Kaggle: Diabetic Retinopathy Detection  ', html.A('Link', href='https://www.kaggle.com/c/diabetic-retinopathy-detection',  target='_blank')]),
                               html.H4(''),
                               html.Label(['-Source Code in GitHub  ', html.A('https://fernandoferrer.github.io/ICDR/', href='https://fernandoferrer.github.io/ICDR/',  target='_blank')]),
                               
                             ],style = {'background-color':'rgba(183,183,183,0.5)',
                                        'font-size':'medium'},
                            ),
           ],
           id = 'References' ),
            
           #Page Contact: -----------------------------------------------------------
           html.Div([
                   
                   html.H4('Contact')
                   
           ], id = 'Contact' ), 
            

            
        ],style = {'display':'block'}),
               
],
style={'background-image':'url(/assets/background.PNG/)',
       'height':'100vh',
       'background-size':'cover'}
)
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