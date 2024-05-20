from watchdog.observers import Observer
import time
import move_and_unpack

from settings import app_list

class Event():
    def dispatch(self,event):
        print(event)
        if event.event_type == 'created':
            print("do things with whatsits here")
            move_and_unpack.move_and_unpack()


observer = Observer()

observers = []
for app in app_list.keys():
    print("Observer created for ", app, "in", app_list[app]["source_directory"])
    observer.schedule(Event(), app_list[app]["source_directory"])
    observers.append(observer)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    for o in observers:
        o.unschedule_all()
        o.stop()
        
for o in observers:
    o.join()