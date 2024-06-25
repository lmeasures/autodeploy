from watchdog.observers import Observer
from watchdog.observers.api import BaseObserver
import time
import move_and_unpack

from settings import app_list

class Event():
    def dispatch(self,event):
        if event.event_type == 'created' or event.event_type == 'modified' or event.event_type == 'moved':
            app_settings = app_list[event.src_path.split("\\")[-2]]
            ## determine if it's a first time deployment
            ## perform first-time setup operations
            ##### _WHAT ARE FIRST TIME SETUP OPERATIONSSSS_ #####
            ## stop service < API only?
            ## stop website
            move_and_unpack.move_and_unpack(app_settings)
        ## rely on powershell script- one for each type of application
        ## have powershell script be in repo for source-control
        ## have application run script 
        
        ### POWERSHELL 4 OR 3
        ### EXTRACT ARCHIVE


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
    