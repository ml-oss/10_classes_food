import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np


def load_and_prep_image(filename,img_shape = 224):
    img = tf.io.read_file(filename)
    img = tf.image.decode_image(img)
    img = tf.image.resize(img , size = [img_shape,img_shape])
    img = img/255.
    return img


def pred_plot(model,filename,class_names):
    
    model = tf.keras.models.load_model("model.sav")
    img = load_and_prep_image(filename)

    pred = model.predict(tf.expand_dims(img,axis=0))

    pred_class = class_names[tf.argmax(pred[0])]
    
    return pred_class
