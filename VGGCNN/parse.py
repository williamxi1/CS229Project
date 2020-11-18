import pandas as pd
import os

filenames = os.listdir("./images_train/train")
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
df.to_csv('train.csv')

##############################################
filenames = os.listdir("./images_validation/validation")
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
df.to_csv('validation.csv')

##############################################
filenames = os.listdir("./images_test/test")
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
df.to_csv('test.csv')
