import socket
import time

import win32serviceutil

import servicemanager
import win32event
import win32service
from settings import app_list, watchdog_app_settings

from watchdog_ini import Event
from os import walk
from watchdog.observers import Observer
from watchdog.observers.api import BaseObserver
import time

from settings import app_list, watchdog_app_settings

class AutoDeploy_Watchdog(win32serviceutil.ServiceFramework):
    '''Base class to create winservice in Python'''

    _svc_name_ = 'autodeploy_watchdog'
    _svc_display_name_ = 'AutoDeploy Watchdog'
    _svc_description_ = 'Watchdog based service for monitoring directories and deploying applications'

    @classmethod
    def parse_command_line(cls):
        '''
        ClassMethod to parse the command line
        '''
        win32serviceutil.HandleCommandLine(cls)

    def __init__(self, args):
        '''
        Constructor of the winservice
        '''
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        '''
        Called when the service is asked to stop
        '''
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        '''
        Called when the service is asked to start
        '''
        self.start()
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def start(self):
        '''
        Override to add logic before the start
        eg. running condition
        '''
        self.isrunning = True
        pass

    def stop(self):
        '''
        Override to add logic before the stop
        eg. invalidating running condition
        '''
        self.isrunning = False
        pass

    def main(self):
        '''
        Main class to be ovverridden to add logic
        '''
        print("| Service Starting!")
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
            while self.isrunning:
                time.sleep(watchdog_app_settings["query_timer"])
            if self.isrunning == False:
                print("| Terminating watchdog")
                for o in observers:
                    o.unschedule_all()
                    o.stop()
        except KeyboardInterrupt:
            print("| Terminating watchdog")
            for o in observers:
                o.unschedule_all()
                o.stop()
        
        for o in observers:
            o.join()
            pass

# entry point of the module: copy and paste into the new module
# ensuring you are calling the "parse_command_line" of the new created class
if __name__ == '__main__':
    AutoDeploy_Watchdog.parse_command_line()