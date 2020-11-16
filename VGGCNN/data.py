import pandas as pd
import itertools

from tensorflow.python.keras.applications.resnet import preprocess_input
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator

train_df = pd.read_csv('train.csv')
validation_df = pd.read_csv('validation.csv')
test_df = pd.read_csv('test.csv')

# train_df = train_df.head(100)
# validation_df = validation_df.head(100)

image_size = 224
data_generator = ImageDataGenerator(preprocessing_function=preprocess_input)

train_generator = data_generator.flow_from_dataframe(
    train_df,
    "images_train/train",
    x_col='filename',
    y_col='category',
    target_size=(image_size, image_size),
    batch_size=5,
    class_mode='categorical',
    shuffle=False)

validation_generator = data_generator.flow_from_dataframe(
    validation_df,
    "images_validation/validation",
    x_col='filename',
    y_col='category',
    target_size=(image_size, image_size),
    batch_size=5,
    class_mode='categorical',
    shuffle=False)

test_generator = data_generator.flow_from_dataframe(
    test_df,
    "images_test/test",
    x_col='filename',
    y_col='category',
    target_size=(image_size, image_size),
    batch_size=5,
    class_mode='categorical',
    shuffle=False)
