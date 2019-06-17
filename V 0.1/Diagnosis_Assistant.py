# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:50:45 2019

@author: reeff
"""

import dash_html_components as html
import dash_core_components as dcc

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
                'background-color':'rgba(183,183,183,0.5)'
            },
                
        # Allow multiple files to be uploaded
        multiple=False
        ),

html.H1('AAA',style={'color':'rgba(0,0,0,0)'}),  

html.Div(id='output-image-upload'),
  
])