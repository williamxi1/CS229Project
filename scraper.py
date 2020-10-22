import subprocess
import os
import pandas as pds


def getAttributes():
    styleCSVPath = os.path.join(os.path.dirname(os.getcwd()), "data", "fashion-dataset")
    fashionData = pds.read_csv(os.path.join(styleCSVPath, 'styles.csv'))
    idList = {}
    for i in range(len(fashionData)):
        if fashionData['subCategory'][i] in idList:
            idList[fashionData['subCategory'][i]].append(fashionData['id'][i])
        else:
            idList[fashionData['subCategory'][i]] = [fashionData['id'][i]]
    return idList

def createDirectories(idList):
    os.chdir(os.path.join(os.path.dirname(os.getcwd()), "data/fashion-dataset"))
    for clothType in idList:
        subprocess.run(["mkdir", clothType])
        for clothID in idList[clothType]:
            subprocess.run(["mv", "images/" + str(clothID) + ".jpg", clothType])


if __name__ == "__main__":
   idList =  getAttributes()
   createDirectories(idList)
