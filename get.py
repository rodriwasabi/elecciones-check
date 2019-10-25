import sys
import requests

def scrap(args):

    source_url = "https://trep.oep.org.bo/resul/imgActa/204611.jpg"
    sink_path = "204611.jpg"

    r = requests.get(source_url, stream=True)
    if r.status_code == 200:
        with open(sink_path, 'wb') as f:
            for chunk in r:
                f.write(chunk)

if __name__ == "__main__":
   scrap(sys.argv[1:])