# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:39:41 2019

@author: reeff
"""

import dash_html_components as html
import base64
import os

#Get current directory:
directory = os.getcwd()

#ICDR Logo:
image_filename = directory+'/assets/icon.PNG' #Get the logo image
encoded_image = base64.b64encode(open(image_filename, 'rb').read()) #Encode the logo image


Home=html.Div([
        
html.Div([
        html.H2('Welcome to Image Classifier for Diabetic Retinopathy',
        style={'text-align':'center'}
        ),
        
        html.Div(id='three-container'),
        
        #3D Image:    
            html.Ul(
                    html.Li([
                            html.Div([
                                    
                                     html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
                                              style = {
                                                      'width':'40vw',
                                                      },
                                              ),
                                    
                                    ],
        
                                    className='image'),
                                    
                            html.Div(className='shadow'),
                            
                            ],
                            style = {
                                      'display':'block',
                                      'margin':'0 auto',
                                      },
                            ),
                       
                    ),
                
        ],

        style={'background-color': 'rgba(183,183,183,0.5)',
               'box-shadow':'5px 1px 10px 1px grey'
               },                            
        ),            
])

'''
html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
             style = {
                      'display':'block',
                      'margin':'0 auto',
                      'width':'40%',
                      },
             ),
'''