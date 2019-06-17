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

                 html.Script(src='https://static.codepen.io/assets/common/stopExecutionOnTimeout-de7e2ef6bfefd24b79a3f68b414b87b8db5b08439cac3f1012092b2290c719cd.js'),
        html.Script(src='//cdnjs.cloudflare.com/ajax/libs/three.js/r75/three.min.js'),
        html.Script(src='//cdnjs.cloudflare.com/ajax/libs/gsap/1.18.0/TweenMax.min.js'),
        html.Script(src='https://s3-us-west-2.amazonaws.com/s.cdpn.io/175711/bas.js'),
        html.Script(src='https://s3-us-west-2.amazonaws.com/s.cdpn.io/175711/OrbitControls-2.js'),
        html.Script(id='ImgTrans'),
        
                html.Canvas(width='1258',
                            height='312',
                            style={'width':'1007px',
                                   'height':'250px'}
                            ),


'''