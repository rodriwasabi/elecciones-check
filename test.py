import sys, os, re
import requests

baseUrl = "https://trep.oep.org.bo/resul/imgActa/{0}.jpg"

def scrap(args):

    path = './mesas/'
    files = []

    for r, d, f in os.walk(path):
        for file in f:
            if '.mesa' in file:
                files.append(os.path.join(r, file))
                fileName = "{}".format(file.replace('.mesa', ''))
                pathName = "./results/{}".format(fileName)
                if not os.path.exists(pathName):
                    os.mkdir(pathName)
    
    
if __name__ == "__main__":
   scrap(sys.argv[1:])