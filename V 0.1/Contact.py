# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:54:52 2019

@author: reeff
"""

import dash_html_components as html

Contact=html.Div([

html.Div([
        
           html.H3('Contacto:'),
           html.Label(['-Dr. Esther Rodrigo Morales (Oftalmóloga): ', html.A('esther.rodrigo.morales@gmail.com',href='mailto:esther.rodrigo.morales@gmail.com')]),
           html.H4(''),
           html.Label(['-Dr. Fernando Pérez Roca (Oftalmólogo): ', html.A('oftalmofer@gmail.com',href='mailto:oftalmofer@gmail.com')]),
           html.H4(''),
           html.Label(['-Dr. Ana Alfaro Juárez (Oftalmóloga): ', html.A('alfaro.juarez@hotmail.com',href='mailto:alfaro.juarez@hotmail.com')]),
           html.H4(''),
           html.Label(['-Fernando Ferrer Perruca (Científico de Datos): ', html.A('fernando.ferrer.perruca@gmail.com', href='mailto:fernando.ferrer.perruca@gmail.com')]),
           html.H4(''),
           html.Label(['-Gonzalo Hernández Muñoz (Científico de Datos): ', html.A('gonzalo.hernandez.1293@gmail.com', href='mailto:gonzalo.hernandez.1293@gmail.com')]),                 
        ],
         style = {'background-image':'linear-gradient(to bottom right, rgba(183,183,183,0.7), rgba(111,163,225,0.7))',
                  'font-size':'medium',
                  'box-shadow':'5px 1px 10px 1px grey'}),
             
])