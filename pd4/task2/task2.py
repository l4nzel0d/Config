import json
import os

data_dict = {}

with open('civgraph.json', 'r') as file:
    print("Successfully opened file")
    data_dict = json.load(file)

# Create the 'dones' directory if it doesn't exist
os.makedirs('dones', exist_ok=True)

with open('Makefile', 'w') as file:
    for key in data_dict:
        # Create a target and its dependencies
        file.write(f"{key}:")
        for dependency in data_dict[key]:
            file.write(f" {dependency}")
        file.write("\n")
        
        # Add commands to avoid outputting already executed tasks
        file.write(f"\t@if [ ! -f dones/{key}.done ]; then \\\n")
        file.write(f"\t\techo \"{key}\"; \\\n")
        file.write(f"\t\ttouch dones/{key}.done; \\\n")
        file.write(f"\tfi\n")

