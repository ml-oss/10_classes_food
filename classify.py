import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import numpy as np
import matplotlib.image as imgage
def load_and_prep_image(filename,img_shape = 224):
    img = imgage.imread(filename)
    img = np.array(img)
    img = img.resize((1,img_shape,img_shape,3))
    img = img/255.
    return img


def pred_plot(filename,class_names):
    
    model = tf.keras.models.load_model("model.sav")
    img = load_and_prep_image(filename)

    pred = model.predict(img)

    pred_class = class_names[pred[0].argmax()]
    
    return pred_class
