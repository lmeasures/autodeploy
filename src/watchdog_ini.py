from watchdog.observers import Observer
import time
import move_and_unpack

import settings

class Event():
    def dispatch(self,event):
        if event.event_type == 'created':
            print("do things with whatsits here")
            move_and_unpack.move_and_unpack()

    
path = settings.source_directory

observer = Observer()
observer.schedule(Event(), path)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()