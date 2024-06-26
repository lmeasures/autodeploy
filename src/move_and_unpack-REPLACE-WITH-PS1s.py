import errno
import shutil
import time
from zipfile import ZipFile as zf
import os

from gen_ops import mkdir_p

## TODO recreate this functionality in powershell scripts

def move_and_unpack (application_settings, latest_build_folder):
    print("|| Removing old backups")
    if os.path.exists(f"{application_settings["code_target_directory"]}_backup"): shutil.rmtree(f"{application_settings["code_target_directory"]}_backup")
    if os.path.exists(f"{application_settings["env_target_directory"]}_backup"): shutil.rmtree(f"{application_settings["env_target_directory"]}_backup")
    
    print("|| Creating new backups from old deployment")
    if os.path.exists(f"{application_settings["code_target_directory"]}"): os.rename(f"{application_settings["code_target_directory"]}", f"{application_settings["code_target_directory"]}_backup")
    if os.path.exists(f"{application_settings["env_target_directory"]}"): os.rename(f"{application_settings["env_target_directory"]}", f"{application_settings["env_target_directory"]}_backup")
    
    print("|| Creating new directories")
    mkdir_p(f"{application_settings["code_target_directory"]}\\")
    mkdir_p(f"{application_settings["env_target_directory"]}\\")
    
    print("|| Moving new .zips")
    shutil.copy(f"{latest_build_folder}\\{application_settings["app_name"]}_env.zip",f"{application_settings["env_target_directory"]}\\{application_settings["app_name"]}_env.zip")
    shutil.copy(f"{latest_build_folder}\\{application_settings["app_name"]}_code.zip",f"{application_settings["code_target_directory"]}\\{application_settings["app_name"]}.zip")

    print("|| Unpacking .zips")
    with zf(f"{application_settings["code_target_directory"]}\\{application_settings["app_name"]}_code.zip", 'r') as zip_ref:
        zip_ref.extractall(application_settings["code_target_directory"])
    with zf(f"{application_settings["env_target_directory"]}\\{application_settings["app_name"]}_env.zip", 'r') as zip_ref:
        zip_ref.extractall(application_settings["env_target_directory"])
        
    print("|| Removing leftover .zips")
    os.remove(f"{application_settings["env_target_directory"]}\\{application_settings["app_name"]}_env.zip")
    ### TODO Conda packs this into a zip, need to also run the conda unpack executable
    os.remove(f"{application_settings["code_target_directory"]}\\{application_settings["app_name"]}_code.zip")