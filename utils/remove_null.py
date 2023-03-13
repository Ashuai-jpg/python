import os

# get the current directory path
dir_path = os.getcwd()

# iterate through all the files in the directory
for file_name in os.listdir(dir_path):
    print(file_name)
    # get the full path of the file
    file_path = os.path.join(dir_path, file_name)
    
    # check if the file is a regular file and has size 0
    if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
        # delete the file
        os.remove(file_path)
        print(f"Deleted file: {file_name}")
