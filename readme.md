- conda activate autodeploy
- python ./src/watchdog_ini.py

---
---

- IMPORTANT NOTE: any instances of repetition in terms of naming conventions are <b>NOT ACCIDENTS</b>. For instance: Where the terminology "application_name" is repeated throughout settings, this represents where the value must be identical for new applications. i.e. if you create a new app and replace "application_name" in one place with your new app's name, you __must__ replace "application_name" for the rest of your settings to be the __exact__ same.

---
---
Okay. So here's the deal:

1. new builds coming from the devops pipeline require the following file structure:
```
- overall_deployment_folder
    - application_name
        - \build#\
            - \deployment_scripts\
                - \first_time_setup\
                    - 01-script_name.ps1
                    - 02-script_name.ps1
                    - 03-script_name.ps1
                    - ...
                - 01-script_name.ps1
                - 02-script_name.ps1
                - 03-script_name.ps1
                - 04-script_name.ps1
                - ...
                - deployment_settings.json
            - application_name_env.zip
            - application_name_code.zip
```
---
2. The app (autodeploy) will perform the following actions:
    - get latest build
    - get the deployment settings from said build
    - determine if this is a first-time setup
    - if first time:
        - create new directories/ folders for deployment
        - gather up the first-time-setup scripts ready to be executed
    - gather up the regular pipeline scripts
    - execute the gathered scripts in order, reporting on the start-finish of each

3. TODO - The app will run as an auto-restarting service.
4. TODO - The app will provide text logs for each watchdog instance it has created (one per application)
5. App has a core settings file in `src` that contains individual high-level app settings, and base watchdog settings.
6. App uses the high-level app settings in `src/settings.py` in order to spin up watchdog instances. One per application. The query_timer comes from `src/settings.py` 'watchdog_app_settings'.
7. New applications will require an addition to the internal settings.py file in `src` (`src/settings.py`), and subsequently, the application will need restarting. Best practise for this will be to restart the service itself, don't faff with terminals and such.
8. The "Most Recent build" or "latest build" that the app will target is defined by the created/modified date of folders inside each `application_name` directory. For instance, in the example, `application_name/` contains two builds. If I were to modify a file 2 layers deep in the older build, this would not tell windows that the higher-level folder had been modified.
9. The scripts in the deployment_scripts section are numbered to be executed in that order. i.e. `01-*.ps1` will be executed before `02-*.ps1`


---
---

todo:
- ~~add watchdog capability (watchdog installed)~~
- ~~https://pypi.org/project/watchdog/~~
- ~~need multiple watchdogs- one per directory with clean spin up and down.~~
- ~~https://stackoverflow.com/questions/32923451/how-to-run-an-function-when-anything-changes-in-a-dir-with-python-watchdog~~
- ~~https://stackoverflow.com/questions/19991033/generating-multiple-observers-with-python-watchdog~~
- ~~see both of the above for further info.~~



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