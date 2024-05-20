from zipfile import ZipFile as zf
import os

def move_and_unpack (application_settings):
    print("Change detected, deploying")
    os.rename(f"{application_settings["source_directory"]}/{application_settings["app_name"]}.zip",f"{application_settings["code_target_directory"]}/{application_settings["app_name"]}.zip")
    os.rename(f"{application_settings["source_directory"]}/{application_settings["app_name"]}_env.zip",f"{application_settings["env_target_directory"]}/{application_settings["app_name"]}_env.zip")

    with zf(f"{application_settings["code_target_directory"]}/{application_settings["app_name"]}.zip", 'r') as zip_ref:
        zip_ref.extractall(application_settings["code_target_directory"])
    with zf(f"{application_settings["env_target_directory"]}/{application_settings["app_name"]}_env.zip", 'r') as zip_ref:
        zip_ref.extractall(application_settings["env_target_directory"])
        
    os.remove(f"{application_settings["code_target_directory"]}/{application_settings["app_name"]}.zip")
    os.remove(f"{application_settings["env_target_directory"]}/{application_settings["app_name"]}_env.zip")