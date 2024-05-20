from watchdog.observers import Observer
from watchdog.observers.api import BaseObserver
import time
import move_and_unpack

from settings import app_list

class Event():
    def dispatch(self,event):
        if event.event_type == 'created':
            app_settings = app_list[event.src_path.split("\\")[-1].split(".")[0]]
            move_and_unpack.move_and_unpack(app_settings)



observers: list[BaseObserver] = []
for app in app_list.keys():
    observer = Observer()
    print("Observer created for", app, "in", app_list[app]["source_directory"])
    observer.schedule(Event(), app_list[app]["source_directory"])
    observer.name = f"Observer_{app}"
    observers.append(observer)
observer.start()

try:
    print("Watching")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Terminating watchdog")
    for o in observers:
        o.unschedule_all()
        o.stop()
        
for o in observers:
    o.join()