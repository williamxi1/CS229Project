import sys
import pandas as pd
import os
import numpy as np

from tensorflow.python.keras.applications.resnet import ResNet50
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.keras.applications.resnet import preprocess_input
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator

from data import train_generator, validation_generator, test_generator

validation_data = pd.read_csv('validation.csv')
test_data = pd.read_csv('test.csv')

# Testing
# validation_data = validation_data.head(100)

checkpoint_path = "model_checkpoints/cp-0015.ckpt"
resnet_weights_path = 'resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5'
num_classes = 2

#Load model from checkpoint
model = Sequential()
model.add(ResNet50(include_top=False, pooling='avg', weights=resnet_weights_path))
model.add(Dense(num_classes, activation='softmax'))
model.load_weights(checkpoint_path)

prediction_prob = model.predict(test_generator, steps = 8, verbose = 1)

d = {0: 'Max', 1: 'Will'}

predictions = np.argmax(prediction_prob, axis=1)
predictions = [d[predict] for predict in predictions]
predictions_df = pd.DataFrame({
    'filename': test_data['filename'],
    'prediction': predictions,
    'ground truth': test_data['category']
})
predictions_df.to_csv('predictions.csv')

with open('predictions.txt', 'w') as file:
     print(prediction_prob, file=file)
