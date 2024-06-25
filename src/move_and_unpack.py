import errno
import shutil
import time
from zipfile import ZipFile as zf
import os

def mkdir_p(path):
    print("||| Attempting to create directory", path)
    try:
        os.makedirs(path)
        print("|| Success")
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            print("|| Directory Exists")
            pass
        else: raise
        
def get_most_recently_modified_directory(search_path):
    return max([f for f in os.scandir(search_path)], key=lambda x: x.stat().st_mtime).path

def move_and_unpack (application_settings):
    print(f"|| Change detected, deploying {application_settings["app_name"]}")
    
    latest_build_folder = get_most_recently_modified_directory(f"{application_settings["source_directory"]}\\")
    
    print("|| Removing old backups")
    if os.path.exists(f"{application_settings["code_target_directory"]}_backup"): shutil.rmtree(f"{application_settings["code_target_directory"]}_backup")
    if os.path.exists(f"{application_settings["env_target_directory"]}_backup"): shutil.rmtree(f"{application_settings["env_target_directory"]}_backup")
    
    time.sleep(1)
    
    print("|| Creating new backups from old deployment")
    if os.path.exists(f"{application_settings["code_target_directory"]}"): os.rename(f"{application_settings["code_target_directory"]}", f"{application_settings["code_target_directory"]}_backup")
    if os.path.exists(f"{application_settings["env_target_directory"]}"): os.rename(f"{application_settings["env_target_directory"]}", f"{application_settings["env_target_directory"]}_backup")
    
    time.sleep(1)
    
    print("|| Creating new directories")
    mkdir_p(f"{application_settings["code_target_directory"]}\\")
    mkdir_p(f"{application_settings["env_target_directory"]}\\")
    
    time.sleep(1)
    
    print("|| Moving new .zips")
    shutil.copy(f"{latest_build_folder}\\{application_settings["app_name"]}_env.zip",f"{application_settings["env_target_directory"]}\\{application_settings["app_name"]}_env.zip")
    shutil.copy(f"{latest_build_folder}\\{application_settings["app_name"]}.zip",f"{application_settings["code_target_directory"]}\\{application_settings["app_name"]}.zip")

    time.sleep(1)

    print("|| Unpacking .zips")
    with zf(f"{application_settings["code_target_directory"]}\\{application_settings["app_name"]}.zip", 'r') as zip_ref:
        zip_ref.extractall(application_settings["code_target_directory"])
    with zf(f"{application_settings["env_target_directory"]}\\{application_settings["app_name"]}_env.zip", 'r') as zip_ref:
        zip_ref.extractall(application_settings["env_target_directory"])
        
    time.sleep(1)
        
    print("|| Removing leftover .zips")
    os.remove(f"{application_settings["env_target_directory"]}\\{application_settings["app_name"]}_env.zip")
    ### TODO Conda packs this into a zip, need to also run the conda unpack executable
    os.remove(f"{application_settings["code_target_directory"]}\\{application_settings["app_name"]}.zip")