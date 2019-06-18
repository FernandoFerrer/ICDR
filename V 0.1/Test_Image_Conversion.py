# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:57:14 2019

@author: reeff
"""
def get_predictions(src):
    #Import libraries
    import base64
    import os
    import io
    import numpy as np    
    from PIL import Image
    
    #Import Model
    from Settings import ICDR_Model, TH
    
    #Get current directory:
    directory = os.getcwd()
    
    #Encode to src:
    image_filename = directory+'/assets/22.png' #Get the logo image
    encoded_image = base64.b64encode(open(image_filename, 'rb').read()) #Encode the logo image
    src='data:image/png;base64,{}'.format(encoded_image.decode())
    
    #Decode from src to image:
    m = Image.open(io.BytesIO(base64.b64decode(src.split(',')[1]))) #Get image from src
    arr=np.asarray(m)[...,:3] #Convert to numpy array and remove transparency layer
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
    return prediction, Conf, Cat
        
        
        