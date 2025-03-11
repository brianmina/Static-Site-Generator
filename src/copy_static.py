import os
import shutil

def copy_static(source_path, dest_path):
    """
    Recursively copy files from source_path to dest_path
    """
    # Remove destination directory if it exists
    if os.path.exists(dest_path):
        print(f"Removing {dest_path}")
        shutil.rmtree(dest_path)
    
    # Create destination directory
    os.mkdir(dest_path)
    print(f"Created {dest_path}")
    
    # Walk through source directory
    for item in os.listdir(source_path):
        source_item = os.path.join(source_path, item)
        dest_item = os.path.join(dest_path, item)
        
        if os.path.isfile(source_item):
            # Copy file
            shutil.copy(source_item, dest_item)
            print(f"Copied {source_item} to {dest_item}")
        else:
            # Recursively copy directory
            copy_static(source_item, dest_item)
