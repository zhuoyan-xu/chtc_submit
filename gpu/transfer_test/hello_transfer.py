print("hello word gpu")
import json
import time 
import os
import sys

# Function to load JSON data from a file
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path, indent = 4):
    print(f"save to {file_path}, data length {len(data)}")
    with open(file_path, 'w') as file:
        json.dump(data, file, indent = indent)


print("os list dir")
print(os.listdir())


output = {'a': [1,2,3], 'b':"I am transfer dir"}

save_json(output, "transfer_output.json")



