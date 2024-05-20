from zipfile import ZipFile as zf
import os

def move_and_unpack (application_settings):
    print(f"Change detected, deploying {application_settings["app_name"]}")
    
    os.replace(f"{application_settings["source_directory"]}\\{application_settings["app_name"]}_env.zip",f"{application_settings["env_target_directory"]}\\{application_settings["app_name"]}_env.zip")
    os.replace(f"{application_settings["source_directory"]}\\{application_settings["app_name"]}.zip",f"{application_settings["code_target_directory"]}\\{application_settings["app_name"]}.zip")

    with zf(f"{application_settings["code_target_directory"]}\\{application_settings["app_name"]}.zip", 'r') as zip_ref:
        zip_ref.extractall(application_settings["code_target_directory"])
    with zf(f"{application_settings["env_target_directory"]}\\{application_settings["app_name"]}_env.zip", 'r') as zip_ref:
        zip_ref.extractall(application_settings["env_target_directory"])
        
    # system not finding *_env.zip < - TODO
        
    os.remove(f"{application_settings["env_target_directory"]}\\{application_settings["app_name"]}_env.zip")
    os.remove(f"{application_settings["code_target_directory"]}\\{application_settings["app_name"]}.zip")