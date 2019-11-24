# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:39:41 2019

@author: reeff
"""

import dash_html_components as html
import dash_core_components as dcc
from textwrap import dedent
import base64
import os

#Get current directory:
directory = os.getcwd()

#ICDR Logo:
image_filename = directory+'/assets/icon.PNG' #Get the logo image
encoded_image = base64.b64encode(open(image_filename, 'rb').read()) #Encode the logo image


Home=html.Div([
        
html.Div([
                                
        html.H2('Bienvenido a ACRIA: Asistente para la Clasificación de Retinografías mediante Inteligencia Artificial',
        style={'text-align':'center',
               'margin-top':'0px',
               'color':'rgb(255,255,255)'}
        ),
                
        #Logo hover:
        html.Div([
                html.Div(
                        html.Figure(
                                html.Img(src='assets/icon.PNG',style={'width':'30vw','margin-bottom':'1vh'}),
                                ),                
                        ),
                ],style={'float':'none','margin':'0 auto','margin-bottom':'0.5vh'},className='hover01 column'),
                
        ],
        id='gradient',
        ),

#Horizontal division:
html.Div([
        html.H1('-'),
        ],style={'width':'90vw',
                 'color':'rgba(0,0,0,0)'}),

#Flip Card1:
html.Div([
        html.Div([
                html.Div([
                        html.Img(src='/assets/doctor.png',
                                 style={'width':'10vw'})
                        ],
                        className='side'
                        ),
                html.Div([
                        dcc.Markdown(dedent('''
                                            #### 
                                            #### ACRIA es una herramienta para el soporte de médicos generales y oftalmólogos. 
                                            '''
                                            ))
                        ],
                        className='side back'
                        )
                ],
                className='card'
                )
        ],
className='card-container'
),

#Flip Card 2:
html.Div([
        html.Div([
                html.Div([
                        html.Img(src='/assets/retinography.png',
                                 style={'width':'10vw'})
                        ],
                        className='side'
                        ),
                html.Div([
                        dcc.Markdown(dedent('''
                                            #### 
                                            #### Ha sido diseñada para identificar retinografías y entrenada con más de 7000 imágenes. 
                                            '''
                                            ))
                        ],
                        className='side back'
                        )
                ],
                className='card'
                )
        ],
className='card-container'
),

#Flip Card 3:
html.Div([
        html.Div([
                html.Div([
                        html.Img(src='/assets/ai.png',
                                 style={'width':'10vw'})
                        ],
                        className='side'
                        ),
                html.Div([
                        dcc.Markdown(dedent('''
                                            #### El sistema utiliza una red neuronal para identificar y clasificar las imágenes de forma similar a como lo haría un médico experimentado. 
                                            '''
                                            ))
                        ],
                        className='side back'
                        )
                ],
                className='card'
                )
        ],
className='card-container'
),

#Flip Card 4:
html.Div([
        html.Div([
                html.Div([
                        html.Img(src='/assets/classification.png',
                                 style={'width':'10vw'})
                        ],
                        className='side'
                        ),
                html.Div([
                        dcc.Markdown(dedent('''
                                            #### El clasificador está diseñado para dar soporte en la identificación de imágenes con retinopatía diabética y edema macular. 
                                            '''
                                            ))
                        ],
                        className='side back'
                        )
                ],
                className='card'
                )
        ],
className='card-container'
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