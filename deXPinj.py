import os
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def update_expG(obj):
    if isinstance(obj, dict):
        for key in obj:
            if key == "experienceGained" and isinstance(obj[key], dict): #check parent field; format dict
                if "Int32" in obj[key] and isinstance(obj[key]["Int32"], (int, float)): #check child field, format int
                    obj[key]["Int32"] += 10008
            else:
                update_expG(obj[key]) #recurse to keep seaching with increased depth.
    elif isinstance(obj, list):
        for item in obj:
            update_expG(item) 


#mainline================================
file_path = "profile.bin.json"

with open(file_path, "r") as f:
    data = json.load(f)

update_expG(data) #py mods dict (mutable obj) by ref

with open(file_path, "w") as f:
    json.dump(data, f, indent=4)
