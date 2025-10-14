import json
import sys
import os

default_version={"major":1,"minor":0,"patch":0}

VERSION_FILE="docker_version.json"

def get_version():
    if not os.path.exists(VERSION_FILE):
        return default_version
    with open(VERSION_FILE,"r") as f:
        return json.load(f)
def save_version(version):
    with open(VERSION_FILE,"w") as f:
        json.dump(version,f,indent=2)

def format_version(version):
    major=version["major"]
    minor=version["minor"]
    patch=version["patch"]
    if patch==0:
        if minor==0:
            return f"{major}"
        else:
            return f"{major}.{minor}"
    else:
        return f"{major}.{minor}.{patch}"

def show_version():
    v=get_version()
    return format_version(v)

def update_version(version):
    save_version(version)
    return format_version(version)

def increment_major():
    v=get_version()
    v["major"]+=1
    v["minor"]=0
    v["patch"]=0
    return update_version(v)

def increment_minor():
    v=get_version()
    v["minor"]+=1
    v["patch"]=0
    return update_version(v)

def increment_patch():
    v=get_version()
    v["patch"]+=1
    return update_version(v)

if __name__ == '__main__':

    if len(sys.argv)==1:
        print(show_version())
        sys.exit(0)
    if len(sys.argv)>2:
        print("Usage: pyv <major|minor|patch|show>")
        sys.exit(1)

    command=sys.argv[1]

    if command=="major":
        print(increment_major())
    elif command=="minor":
        print(increment_minor())
    elif command=="patch":
        print(increment_patch())
    elif command=="show":
        print(show_version())
    else:
        print("Invalid command. Use major|minor|patch|show as argument.")
        sys.exit(1)

































