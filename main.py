import sys
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras import models
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator

#from PIL import image
import json

#print("4")
model = models.load_model('model.tflearn')
import os
#train_generator.class_indices
#print("5")
# r'C:/Users/hp/Desktop/Major/project/CovidDataset/Val/Covid/xray1.jpg'
#path = r"C:/Users/hp/Desktop/Major/project/CovidDataset/Val/Covid/xray1.jpg"
path = sys.argv[1]
#print(path)
img = image.load_img(path, target_size = (224,224))
img = image.img_to_array(img)
img = np.expand_dims(img , axis=0)
p = model.predict_classes(img)
#print(p)
#print("Python")
x = { "data": int(p[0][0])}
print(json.dumps(x))
