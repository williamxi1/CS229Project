import subprocess
import os
from PIL import Image
import csv

def modifyImgs():
    os.chdir(os.path.join(os.path.dirname(os.getcwd()), 'data', 'fashion-dataset', 'Shoes'))
    output = str(subprocess.check_output(['ls']))
    imgsList= output[2:-3].split("\\n")
    os.chdir(os.path.dirname(os.getcwd()))
    if not os.path.exists('ShoesResized'):
        os.mkdir('ShoesResized')
    with open("shoesResized.csv", 'w') as f:
        writer = csv.writer(f)
        for img in imgsList:
            print(img)
            im = Image.open('Shoes/' + img)
            print(im.size)
            try:
                im = im.resize((128, 128))
                print(im.size)
                im.save('ShoesResized/' + img)
                writer.writerow([img, "Shoe"])
            except:
                print("image not valid")



if __name__ == "__main__":
   modifyImgs()