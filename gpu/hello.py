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



import torch
print(torch.cuda.is_available())

print(torch.version.cuda)
print(torch.cuda.get_device_properties(0).major)
print(torch.cuda.get_device_properties(0).minor)

print("see GPU")
print(torch.cuda.device_count())
print(torch.cuda.current_device())
print(torch.cuda.device(0))
print(torch.cuda.get_device_name(0))

print("os list dir")
print(os.listdir())


output = {'a': [1,2,3], 'b':"I am gpu dir"}

save_json(output, "output.json")



