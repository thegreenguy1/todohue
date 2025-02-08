import json
import os


file = "index.json"
a = {"tasks":[]}
def makedware():
    global file
    if os.path.isfile(file):
        with open(file,"r") as f:
            ...
    else:
        try:
            file = open("index.json","r")
            data = file.read()
        except FileNotFoundError:
            ...
        finally:
            file = open("index.json","w")
            json.dump(a,file)
            file.close()