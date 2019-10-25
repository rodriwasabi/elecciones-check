import sys, os, re
import requests

baseUrl = "https://trep.oep.org.bo/resul/imgActa/{0}.jpg"

def downloadImages(tables):
    tablesWithError = []
    for table in tables:
        tableNumber = table.replace('\n', '')
        if re.search('^[0-9]+$', tableNumber): 
            getUrl = baseUrl.format(tableNumber)
            imageFile = './results/{0}.jpg'.format(tableNumber)
            print getUrl
            r = requests.get(getUrl, stream=True)
            if r.status_code == 200:
                with open(imageFile, 'wb') as f:
                    for chunk in r:
                        if 'ERROR' in chunk:
                            print "ReDo needed: {}".format(tableNumber)
                            tablesWithError.append(tableNumber)
                        f.write(chunk)
                # Deletes file if it is a file with error
                if tableNumber in tablesWithError:
                    os.remove(imageFile)

    return tablesWithError


def scrap(args):

    path = './mesas/'
    files = []
    
    with open("withError.txt", 'w') as f:
        f.write("")

    for r, d, f in os.walk(path):
        for file in f:
            if '.mesa' in file:
                files.append(os.path.join(r, file))

    for file in files:
        with open(file) as fp:
            tables = fp.readlines()

        # r=root, d=directories, f = files
        tablesWithError = downloadImages(tables)

        if len(tablesWithError) > 0:
            for tableWithError in tablesWithError:
                with open("withError.txt", 'a') as f:
                    f.write("{}1\n".format(tableWithError))

            if len(tablesWithError) > 0:
                with open("withError.txt") as fp:
                    tablesWithErrorFromFile = fp.readlines()
                tablesWithError = downloadImages(tablesWithErrorFromFile)
                if len (tablesWithError) > 0:
                    print "still tables with error: "
                    for tableError in tablesWithError:
                        print "{}\r\n".format(tableError)

if __name__ == "__main__":
   scrap(sys.argv[1:])