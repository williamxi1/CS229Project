import subprocess
import os
from PIL import Image, ImageOps
import csv

def modifyImgs():
    os.chdir(os.path.join(os.path.dirname(os.getcwd()), 'data', 'fashion-dataset', 'Bags'))
    output = str(subprocess.check_output(['ls']))
    imgsList= output[2:-3].split("\\n")
    os.chdir(os.path.dirname(os.getcwd()))
    if not os.path.exists('BagsResized'):
        os.mkdir('BagsResized')
    with open("bagsResized.csv", 'w') as f:
        writer = csv.writer(f)
        for img in imgsList:
            print(img)
            im = Image.open('Bags/' + img)
            print(im.size)
            try:
                im = im.resize((128, 128))
                #im = ImageOps.grayscale(im)
                print(im.size)
                im.save('BagsResized/' + img)
                writer.writerow([img, "Bag"])
            except:
                print("image not valid")



if __name__ == "__main__":
   modifyImgs()