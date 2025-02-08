import json
import random

def clear():
    file1 = open("index.json","r")
    data=json.load(file1)
    data["tasks"].clear()
    file2 = open("index.json","w")
    json.dump(data,file2,indent=4)


def lst():
    file2 = open("index.json","r")
    data = json.load(file2)
    for i in range(1,len(data["tasks"])+1):
        a = random.randint(31,38)
        print(f"\033[1;{a}m{i}" + ". "+ data["tasks"][i-1])

def add(value):
    file1 = open("index.json","r")
    data=json.load(file1)
    data["tasks"].append(value)
    file2 = open("index.json","w")
    json.dump(data,file2,indent=4)

def done(d):
    file1 = open("index.json","r")
    data = json.load(file1)
    try:
        data["tasks"].remove(data["tasks"][d-1])
    except IndexError:
        ...
    finally:
        print(f"It seems you are done with tasks {d}.")
    file2 = open("index.json","w")
    json.dump(data,file2,indent=4)
def edit(num):
    file = open("index.json","r")
    data = json.load(file)
    try:    
        data["tasks"][num-1] = input(f"Editing Taks #{num}> ")
        file2 = open("index.json","w")
        json.dump(data,file2)
    except IndexError:
        print(f"Task {num} doesn't exsist")