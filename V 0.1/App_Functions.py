# -*- coding: utf-8 -*-
"""
Created on Thu May  2 20:44:51 2019

@author: F. Ferrer
"""
#Imports:
import pandas as pd
import os
import pickle
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.cm as cm
import plotly.plotly as py
import plotly
import plotly.graph_objs as go
import base64

"Create connection to MySQL db------------------------------------------------"
def db_connection():
    import pymysql.cursors
    con= pymysql.connect(host="127.0.0.1",
                             port=3306,
                             user="root",        
                             passwd="Ratagigante222",
                             db="icdr_db")
    return con


"Filter id images based on diagnosis criteria---------------------------------"
def get_images_ids(retinopathy_grade,macular_edema_grade,combined_grade):    
    con=db_connection()
    
    query='SELECT icdr.idImage, icdr.Retinopathy_Grade, icdr.Macular_Edema_Grade, icdr.Classification from icdr_db.icdr'
    
    table=pd.read_sql_query(query,con)
    
    con.close()
    
    #Dictionaries for disease levels:
    r_g_dic={'No Retinopathy':0,'Mild Retinopathy':1,'Moderate Retinopathy':2,'Severe Retinopathy':3,'Proliferative Retinopathy':4} #Retinopathy grade
    m_e_dic={'No Macular Edema':0,'Moderate Macular Edema':1,'Severe Macular Edema':2} #Macular edema grade
    c_g_dic={'Low Risk':0,'Moderate Risk':1,'Severe Risk':2} #Combined grade
    
    if retinopathy_grade and not macular_edema_grade and not macular_edema_grade:
        table=table.loc[table['Retinopathy_Grade']==r_g_dic[retinopathy_grade]]
        
    elif macular_edema_grade and not retinopathy_grade and not combined_grade:
        table=table.loc[table['Macular_Edema_Grade']==m_e_dic[macular_edema_grade]]
        
    elif combined_grade and not retinopathy_grade and not macular_edema_grade:
        table=table.loc[table['Classification']==c_g_dic[combined_grade]]
        
    elif retinopathy_grade and macular_edema_grade and not combined_grade:
        table=table.loc[table['Retinopathy_Grade']==r_g_dic[retinopathy_grade]]
        table=table.loc[table['Macular_Edema_Grade']==m_e_dic[macular_edema_grade]]
        
    elif retinopathy_grade and not macular_edema_grade and combined_grade:
        table=table.loc[table['Retinopathy_Grade']==r_g_dic[retinopathy_grade]]
        table=table.loc[table['Classification']==c_g_dic[combined_grade]]
        
    elif macular_edema_grade and not retinopathy_grade and combined_grade:
        table=table.loc[table['Macular_Edema_Grade']==m_e_dic[macular_edema_grade]]
        table=table.loc[table['Classification']==c_g_dic[combined_grade]]
        table=table.loc[table['Classification']==c_g_dic[combined_grade]]
        
    if retinopathy_grade and macular_edema_grade and combined_grade:
        table=table.loc[table['Retinopathy_Grade']==r_g_dic[retinopathy_grade]]
        table=table.loc[table['Macular_Edema_Grade']==m_e_dic[macular_edema_grade]]
        table=table.loc[table['Classification']==c_g_dic[combined_grade]]
    
    if len(table['idImage'])>0: 
        id_images=list(table['idImage'])
    else:
        id_images=['No images with this criteria']
    return id_images

"Convert flat image to RGB----------------------------------------------------"
#Input= numpy array of flattened image
#Output= RGB imagr
def flat_to_RGB(arr):
    img= arr.reshape(1,3,146,146).transpose(0,2,3,1).astype("uint8")
    return img[0]


"Generate retinograpy image---------------------------------------------------"
def get_retinography_image(idImage):
    directory = os.getcwd()
    
    id_img=int(idImage)
    con=db_connection()
    query="SELECT * FROM icdr_db.icdr where idImage=%i" %id_img
    image_data=pd.read_sql_query(query,con)
    con.close()
    image_flat=pickle.loads(image_data['Image'][0])
    image=flat_to_RGB(image_flat)
    
    #See if the image is in directory and save it of not:
    images_saved=os.listdir(directory+'/assets/')
    if str(idImage)+'.png' not in images_saved:
        image_mirrored=np.flipud(image)
        plt.imsave(directory+'/assets/'+str(idImage)+'.png',image_mirrored)
    
    return image

"Get Image Classifications----------------------------------------------------"
def get_image_classifications(idImage):    
    id_img=int(idImage)
    con=db_connection()
    query="SELECT Retinopathy_Grade, Macular_Edema_Grade, Classification FROM icdr_db.icdr where idImage=%i" %id_img
    image_data=pd.read_sql_query(query,con)
    con.close()
    
    return image_data

"Generate retinograpy surface plot---------------------------------------------"
def get_surface_plot(image):            
    img1=image[:,:,0]
    img2=image[:,:,1]
    img3=image[:,:,2]
        
    x=np.linspace(0,5,146)
    y=np.linspace(5,10,146)
    X,Y=np.meshgrid(x,y)
    z1=np.ones((146,146))
    z2=z1*9
    z3=z1*20
    
    surf1=go.Surface(x=x, y=y, z=z1,
                 surfacecolor=img1,
                 showscale=False,
                 opacity=1,
                 name='R Channel'
                )
    
    surf2=go.Surface(x=x, y=y, z=z2,
                 surfacecolor=img2,
                 showscale=False,
                 opacity=1,
                 name='G Channel'
                )
    
    surf3=go.Surface(x=x, y=y, z=z3,
                 surfacecolor=img3,
                 showscale=False,
                 opacity=1,
                 name='B Channel'
                )
    
    noaxis=dict( 
                showbackground=False,
                showgrid=False,
                showline=False,
                showticklabels=False,
                ticks='',
                title='',
                zeroline=False)
    
    layout = go.Layout(
             paper_bgcolor='rgba(0,0,0,0)',
             plot_bgcolor='rgba(0,0,0,0)',
             autosize=True,
             height=800,
             width=1000,
             margin=dict(t=1),
             scene=dict(xaxis=dict(noaxis),
                         yaxis=dict(noaxis), 
                         zaxis=dict(noaxis), 
                         aspectratio=dict(x=1,
                                          y=1,
                                          z=1
                                         ),
                        )
            )
                         
    fig=go.Figure(data=[surf1,surf2,surf3], layout=layout)
    #plotly.offline.plot(fig, filename='name.html')
    return fig

"Generate 2D Image PLot-------------------------------------------------------"
def get_2D_Img(ID):    
    directory = os.getcwd()
    
    image_filename=directory+'\\assets\\'+str(ID)+'.png'
                
    encoded_image=base64.b64encode(open(image_filename, 'rb').read())
    decoded_image='data:image/png;base64,{}'.format(encoded_image.decode())

    noaxis=dict( 
                showgrid=False,
                showline=False,
                showticklabels=False,
                ticks='',
                title='',
                zeroline=False)
        
    trace1= go.Scatter(x=[0,1,2,3,4,5],
                       y=[0,1,2,3,4,5],
                       mode = 'markers',
                       line = dict(color = ('rgba(0,0,0,0)')),
                       hoverinfo='skip')
    
    layout= go.Layout(paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)',
                      xaxis=dict(noaxis),
                      yaxis=dict(noaxis), 
                      images= [dict(
                              source=decoded_image,
                              xref= "x",
                              yref= "y",
                              x= 0,
                              y= 5,
                              sizex= 4,
                              sizey= 7,
                              opacity= 1,
                              layer= "below")]
            )
    
    fig=go.Figure(data=[trace1],layout=layout)
    #py.iplot(fig,filename='EXAMPLES/background')
    return fig
    
"Get Predictions from src image-----------------------------------------------"
def get_predictions(src):
    #Import libraries
    import base64
    import io
    import numpy as np    
    from PIL import Image
    
    #Import Model
    from Settings import ICDR_Model, TH
    
    #Decode from src to image:
    m = Image.open(io.BytesIO(base64.b64decode(src.split(',')[1]))) #Get image from src
    arr=np.asarray(m)[...,:3] #Convert to numpy array and remove transparency layer
    arr=arr.astype('float32')/255 #Convert to float
    arr=np.expand_dims(arr,axis=0) #Expand dimension to convert it to keras tensor
    
    #Load Model and compile it:
    from keras.models import load_model
    import keras_metrics
    import keras
    
    Learning_Rate=0.0001
    
    #Define the custom metrics used in the model:
    Precision=keras_metrics.binary_precision(label=2)
    Recall=keras_metrics.binary_recall(label=2)
    
    #Load the model:
    model=load_model(ICDR_Model, custom_objects={"binary_precision": Precision,
                                                      "binary_recall": Recall})
    #Compile model   
    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adamax(lr=Learning_Rate,
                                                  beta_1=0.9,
                                                  beta_2=0.999,
                                                  epsilon=0.00000001,
                                                  decay=0.0),
                  metrics=['accuracy',Precision,Recall])
    
    #Get prediction:
    result=model.predict(arr)
    
    #Reset model:
    keras.backend.clear_session()
    
    #Apply Threshold:
    prob_cat_0=result[0][0]
    prob_cat_1=result[0][1]
    prob_cat_2=result[0][2]
    if prob_cat_2>TH:
        prediction=2
        Conf=prob_cat_2
        Cat='High DR ME Risk'
    else:
        if prob_cat_0>prob_cat_1:
            prediction=0
            Conf=prob_cat_0
            Cat='Low DR ME Risk'
        else:
            prediction=1
            Conf=prob_cat_1
            Cat='Medium DR ME Risk'
    print(Conf)
    return str(prediction), str(Conf), Cat
