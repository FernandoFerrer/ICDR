# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:50:45 2019

@author: reeff
"""

import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq

Diagnosis_Assistant=html.Div([
        
html.H4('Diagnosis Assistant'),

dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Retinography')
        ]),

        style={
                'width': '90%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'display':'block',
                'margin':'0 auto',
                'background-image':'linear-gradient(to bottom right, rgba(183,183,183,0.7), rgba(111,163,225,0.7))'
            },
                
        # Allow multiple files to be uploaded
        multiple=False
        ),

html.H1('AAA',style={'color':'rgba(0,0,0,0)'}),

html.Div([
        
        html.Img(id='output-image-upload',style={'display':'inline-block'}),
        
        ],

        style={'display':'flex',
               'justify-content':'center'}
),

html.Div([
                
        html.H1(id='Category',style={'color':'rgba(255,255,255,1)',
                                     'display':'inline-block'}),

        html.H1('A',style={'color':'rgba(0,0,0,0)',
                             'display':'inline-block'}),

        daq.GraduatedBar(
                        id='conf-indicator',
                        color={"ranges":{"rgba(255,0,0,0.6)":[0,3],"rgba(255,255,0,0.6)":[3,7],"rgba(69,161,99,0.6)":[7,10]}},
                        showCurrentValue=True,
                        label="Confidence %",
                        style={'display':'inline-block'}
                        )

        ],
        style={'display':'flex',
               'justify-content':'center'}
        ),

#Hidden division to store image classfications:
html.Div(id='Prediction',style={'display': 'none'}),
html.Div(id='Confidence',style={'display': 'none'}),

  
])