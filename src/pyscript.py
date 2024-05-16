from zipfile import ZipFile as zf
import settings
import os

os.rename(f"{settings.source_directory}/{settings.app_name}.zip",f"{settings.code_target_directory}/{settings.app_name}.zip")
os.rename(f"{settings.source_directory}/{settings.app_name}_env.zip",f"{settings.env_target_directory}/{settings.app_name}_env.zip")

with zf(f"{settings.code_target_directory}/{settings.app_name}.zip", 'r') as zip_ref:
    zip_ref.extractall(settings.code_target_directory)
with zf(f"{settings.env_target_directory}/{settings.app_name}_env.zip", 'r') as zip_ref:
    zip_ref.extractall(settings.env_target_directory)
    
os.remove(f"{settings.code_target_directory}/{settings.app_name}.zip")
os.remove(f"{settings.env_target_directory}/{settings.app_name}_env.zip")