import json
from os import walk
import os
import subprocess
import sys
from watchdog.observers import Observer
from watchdog.observers.api import BaseObserver
import time

from gen_ops import get_most_recently_modified_directory, mkdir_p, run_script, website_exists
from settings import app_list, watchdog_app_settings

import glob

from pprint import pprint

 
class Event():
    def dispatch(self,event):
        if event.event_type == 'created' or event.event_type == 'modified':
            time.sleep(5)
            app_settings = app_list[event.src_path.split("\\")[-2]]
            print("|> Change Detected in", app_settings["app_name"])
            
            print("| Getting latest build path")
            latest_build_folder = get_most_recently_modified_directory(f"{app_settings["source_directory"]}\\")
            
            print("| Getting deployment settings from newest build")
            with open(f"{latest_build_folder}\\deployment_scripts\\deployment_settings.json") as deployment_settings_file:
                deployment_settings = json.load(deployment_settings_file)
            
            scripts = []
            
            print("| Determining if first-time-setup required")
            if not website_exists(app_settings["app_name"]):
                print("| Website does not exist. Adding first time setup scripts to pipeline")
                scripts.append(glob.glob(f"{latest_build_folder}\\deployment_scripts\\first_time_setup\\*.ps1"))
                print("| Creating fresh directories:")
                print(f"| > {deployment_settings["env_target_directory"]}")
                mkdir_p(f"{deployment_settings["env_target_directory"]}\\")
                print(f"| > {deployment_settings["code_target_directory"]}")
                mkdir_p(f"{deployment_settings["code_target_directory"]}\\")
            
            print("| Adding standard scripts to pipeline")
            scripts.append(glob.glob(f"{latest_build_folder}\\deployment_scripts\\*.ps1"))
            
            print("| Executing pipeline")
            for group in scripts:
                for script in group:
                    print(f"|> Executing: {script.split("\\")[-1]}")
                    response = run_script(script)
                    print(f"| {response}")
            
# def begin_running():      
#     observers: list[BaseObserver] = []
#     for app in app_list.keys():
#         observer = Observer()
#         print("| Observer created for", app, "in", app_list[app]["source_directory"])
#         observer.schedule(Event(), app_list[app]["source_directory"])
#         observer.name = f"Observer_{app}"
#         observers.append(observer)
#     observer.start()

#     try:
#         print("| Watching")
#         while True:
#             time.sleep(watchdog_app_settings["query_timer"])
#     except KeyboardInterrupt:
#         print("| Terminating watchdog")
#         for o in observers:
#             o.unschedule_all()
#             o.stop()
        
#     for o in observers:
#         o.join()
    
    
# begin_running()