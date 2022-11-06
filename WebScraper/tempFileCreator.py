import os
import shutil


def createFolder(path=os.path.dirname(__file__), folderName = 'tmp'):
    
    abs_path = f"{path}\\{folderName}"

    if not os.path.exists(abs_path):
      
        # if the demo_folder directory is not present 
        # then create it.
        os.makedirs(abs_path)
        
    else:
        print(f"{abs_path} already exists")

    return abs_path
    


def delFolder(path=os.path.dirname(__file__), folderName = 'tmp'):
    abs_path = f"{path}\\{folderName}"

    if os.path.exists(abs_path):
      
        # if the demo_folder directory is not present 
        # then create it.
        shutil.rmtree(abs_path)
    else:
        print(f"{abs_path} doesn't exist")
    


if __name__ == "__main__":
    import time

    createFolder()
    time.sleep(4)
    delFolder()

