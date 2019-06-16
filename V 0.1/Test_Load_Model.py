# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:24:16 2019

@author: reeff
"""

from keras.models import load_model
import keras_metrics
import keras

Learning_Rate=0.0001

#Define the custom metrics used in the model:
Precision=keras_metrics.binary_precision(label=2)
Recall=keras_metrics.binary_recall(label=2)

#Load the model:
model=load_model("ICDR_Model_37", custom_objects={"binary_precision": Precision,
                                                  "binary_recall": Recall})
#Compile model   
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adamax(lr=Learning_Rate,
                                              beta_1=0.9,
                                              beta_2=0.999,
                                              epsilon=0.00000001,
                                              decay=0.0),
              metrics=['accuracy',Precision,Recall])
