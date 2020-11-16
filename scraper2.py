import subprocess
import os
import csv

def createCSV(csvName):
    os.chdir(os.path.join(os.path.dirname(os.getcwd()), 'data', 'fashion-dataset', 'Bags'))
    output = str(subprocess.check_output(['ls']))
    imgsList= output[2:-3].split("\\n")
    with open(csvName, 'w') as f:
        writer = csv.writer(f)
        for img in imgsList:
            writer.writerow([img, "Bags"])



if __name__ == "__main__":
   createCSV('shoes.csv');