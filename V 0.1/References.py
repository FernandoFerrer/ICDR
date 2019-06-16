# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:52:22 2019

@author: reeff
"""

import dash_html_components as html

References=html.Div([

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
                    'font-size':'medium',
                    'box-shadow':'5px 1px 10px 1px grey'},
        ),
        
])