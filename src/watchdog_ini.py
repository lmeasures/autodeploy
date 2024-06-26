import subprocess
from watchdog.observers import Observer
from watchdog.observers.api import BaseObserver
import time

from gen_ops import get_most_recently_modified_directory
from move_and_unpack import move_and_unpack
from server_controls import check_service_exists, check_website_exists, start_service, start_website, stop_service, stop_website
from settings import app_list

class Event():
    def dispatch(self,event):
        if event.event_type == 'created' or event.event_type == 'modified' or event.event_type == 'moved':
            app_settings = app_list[event.src_path.split("\\")[-2]]
            
            latest_build_folder = get_most_recently_modified_directory(f"{app_settings["source_directory"]}\\")
            
            ## determine if it's a first time deployment
            # if website doesn't exist- do first time setup
                ## perform first-time setup operations
                    ##### _WHAT ARE FIRST TIME SETUP OPERATIONSSSS_ #####
                        #### for fastcgi apps- these are.. which apps? TODO
                            # wfastcgi-enable
                            # create website
                        #### for react apps 
                            # create website
                        #### for vue apps
                            # service?? TODO
                            # create website
                        #### for flask apps
                        #
                        #### for fast-api apps
                        #
                        
            if check_website_exists(app_settings["website_name"]):
                stop_website(app_settings["website_name"])
                            
            if check_service_exists(app_settings["service_name"]):
                stop_service(app_settings["service_name"])
                
            move_and_unpack(app_settings, latest_build_folder)
            
            # fire off powershell script
            subprocess.call([f"{latest_build_folder}deployment_script.ps1"])
            
            start_service(app_settings["service_name"])
            start_website(app_settings["website_name"])
            
        ## rely on powershell script- one for each type of application
            ## have powershell script be in repo for source-control
            ## have application run script 
        


observers: list[BaseObserver] = []
for app in app_list.keys():
    observer = Observer()
    print("| Observer created for", app, "in", app_list[app]["source_directory"])
    observer.schedule(Event(), app_list[app]["source_directory"])
    observer.name = f"Observer_{app}"
    observers.append(observer)
observer.start()

try:
    print("| Watching")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("| Terminating watchdog")
    for o in observers:
        o.unschedule_all()
        o.stop()
        
for o in observers:
    o.join()
    