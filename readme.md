- conda activate autodeploy
- python ./src/watchdog_ini.py


todo:
- ~~add watchdog capability (watchdog installed)~~
- ~~https://pypi.org/project/watchdog/~~
- ~~need multiple watchdogs- one per directory with clean spin up and down.~~
- https://stackoverflow.com/questions/32923451/how-to-run-an-function-when-anything-changes-in-a-dir-with-python-watchdog
- https://stackoverflow.com/questions/19991033/generating-multiple-observers-with-python-watchdog
- see both of the above for further info.



- make into a windows service (not started)
- https://oxylabs.io/blog/python-script-service-guide


---


    ## This is taken care of by the powershell
    ##EXTRACT ARCHIVE
    ##EXTRACT CONDA ENVIRONMENT - CONDA_UNPACK_SCRIPT
    ##REGISTER WFASTCGI
    ##COPY APP CODE
    ##
    
    ##powershell module - "webadministration" <need python version
    ## - stopwebsite startwebsite <need python versions
    
    ## TODO MAKE WINDOWS SERVICE
    ### TODO Make windows service auto-restart?
    #### TODO make it check for changes to itself?

    ### TODO Conda packs this into a zip, need to also run the conda unpack executable <handled by the powershell?


# what do I need to do now?
- have the application stop a service and an iis website prior to running the important bits
 - check if service and website exist first
- have the application move and unpack the files to the appropriate places, based on settings.py
- have the application run a defined powershell script after moving and unpacking
    - where are the powershell scripts going to be? version controlled in each build??
    - yes, best call
- have the application start up the service and website again after
 - maybe check if exist here or use variable from earlier check, if not exist then create?
  - what are the create new steps involved? need configuration examples


- what differences are needed for a first-time deploy??

- do i package it up into an easily runnable format?
- do i just have it run like a standard executable into a service? <- this one