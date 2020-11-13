import subprocess
import os
from PIL import Image

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
            print(imgfile)
            im = Image.open('Shoes/' + imgfile)
            print(im.size)
            try:
                im = im.resize((128, 128))
                print(im.size)
                im.save('ShoesResized/' + imgfile)
                writer.writerow([img, "Shoe"])
            except:
                print("image not valid")



if __name__ == "__main__":
   modifyImgs()