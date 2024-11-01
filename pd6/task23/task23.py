import json

FOLDER_WITH_DONE_FILES = "dones"

data_dict = {}

with open('civgraph.json', 'r') as file:
    print("Successfully opened file")
    data_dict = json.load(file)

with open('Makefile', 'w') as file:
    # Add target to create the 'dones' directory in the Makefile
    file.write(f"dones:\n")
    file.write(f"\t@mkdir -p {FOLDER_WITH_DONE_FILES}\n\n")  # Create the 'dones' directory silently

    for key in data_dict:
        # Create a target and its dependencies
        file.write(f"{key}: dones")  # Ensure 'dones' is created first
        for dependency in data_dict[key]:
            file.write(f" {dependency}")
        file.write("\n")
        
        # Add commands to avoid outputting already executed tasks
        file.write(f"\t@if [ ! -f {FOLDER_WITH_DONE_FILES}/{key}.done ]; then \\\n")
        file.write(f"\t\techo \"{key}\"; \\\n")  # Echo the task being executed
        file.write(f"\t\ttouch {FOLDER_WITH_DONE_FILES}/{key}.done; \\\n")
        file.write(f"\tfi\n")

    # Combine clean and cleanall into a single clean command
    file.write(f"\nclean:\n")
    file.write(f"\t@rm -rf {FOLDER_WITH_DONE_FILES}/* {FOLDER_WITH_DONE_FILES}\n")  # Remove all files and the directory itself silently
