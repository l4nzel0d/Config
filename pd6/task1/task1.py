import json

data_dict = {}

with open('civgraph.json', 'r') as file:
    print("succesfully opened file")
    data_dict = json.load(file)

with open('Makefile', 'w') as file:
    for key in data_dict:
        file.write(f"{key}:")
        for dependency in data_dict[key]:
            file.write(f" {dependency}")
        file.write(f"\n\t@echo {key}\n")



