#This is created by Mohammed Obeidi
#This is where the prediction occurs based on the dataset downloaded and trained to make the model

#imports
from tensorflow import keras
import numpy as np
from PIL import Image

#load the saved model from the h5 file
model = keras.models.load_model('model.h5')

#define the path to the archive folder
archive_folder = "Archive"

#create an instance of the ImageDataGenerator for retrieving class labels
datagen = keras.preprocessing.image.ImageDataGenerator()

#load the class labels
class_labels = datagen.flow_from_directory(
    directory=archive_folder,
    target_size=(48, 48),
    color_mode="grayscale",
    batch_size=1,
    class_mode="categorical",
    shuffle=False
).class_indices

def predi():
    #load and preprocess the image
    image_path = 'face.jpg'
    image = Image.open(image_path)
    #resize the image to match the input shape of the model
    image = image.resize((48, 48))
    #convert the image to grayscale
    image = image.convert('L')
    #normalize pixel values between 0 and 1
    input_data = np.array(image) / 255.0
    #add a batch dimension
    input_data = np.expand_dims(input_data, axis=0)

    #make predictions using the loaded model without the defualt loader sending to terminal
    predictions = model.predict(input_data, verbose=0)

    #get the predicted class label
    predicted_class_index = np.argmax(predictions)
    predicted_class_label = list(class_labels.keys())[predicted_class_index]

    return predicted_class_label
