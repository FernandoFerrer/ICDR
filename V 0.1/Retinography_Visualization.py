# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:44:00 2019

@author: reeff
"""

import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq
import plotly.graph_objs as go

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
"#############################################################################"

Retinography_Visualization=html.Div([
        
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
        
        
])