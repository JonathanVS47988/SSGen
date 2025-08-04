#copy_static.py

import os
import shutil

def copy_src_to_dest(src_dir, dest_dir):
    copied_files = []
    
    print(f"Passed src_dir: {src_dir} Passed dest_dir: {dest_dir}")
    
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
        os.mkdir(dest_dir)
    else: 
        os.mkdir(dest_dir)
    
    dirs = [item for item in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, item))]
    files = [item for item in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, item))]

    for file in files:
        try:
            shutil.copy(os.path.join(src_dir, file), os.path.join(dest_dir, file))
            copied_files.append(os.path.join(src_dir, file))
        except:
            print(f"An error occured while copying the file {file}")

    for dir in dirs:
        try:
            copy_src_to_dest(os.path.join(src_dir, dir), os.path.join(dest_dir, dir))
        except:
            print(f"An error occured while copying directory {dir}")
        
    print(copied_files)