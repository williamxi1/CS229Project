import pandas as pd
import os

filenames = os.listdir("./images_train_2/train")
categories = []
for filename in filenames:
    category = filename.split('.')[0].split('_')[1]
    if category == 'bag':
        categories.append('bag')
    elif category == 'shoe':
        categories.append('shoe')
    else:
        continue

# print(len(filenames))
# print(len(categories))
df = pd.DataFrame({
    'filename': filenames,
    'category': categories
})

df = df.sample(frac=1).reset_index(drop=True)
df.to_csv('train2.csv')

##############################################
filenames = os.listdir("./images_validation_2/validation")
categories = []
for filename in filenames:
    category = filename.split('.')[0].split('_')[1]
    if category == 'bag':
        categories.append('bag')
    elif category == 'shoe':
        categories.append('shoe')
    else:
        continue

df = pd.DataFrame({
    'filename': filenames,
    'category': categories
})

df = df.sample(frac=1).reset_index(drop=True)
df.to_csv('validation2.csv')

##############################################
filenames = os.listdir("./images_test_2/test")
categories = []
for filename in filenames:
    category = filename.split('.')[0].split('_')[1]
    if category == 'bag':
        categories.append('bag')
    elif category == 'shoe':
        categories.append('shoe')
    else:
        continue

df = pd.DataFrame({
    'filename': filenames,
    'category': categories
})

df = df.sample(frac=1).reset_index(drop=True)
df.to_csv('test2.csv')
