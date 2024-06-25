import os, subprocess, sys

def check_service_exists(svc):
    ret = subprocess.Popen([
        "cmd.exe",
        "@echo off"
        f'SC getdisplayname {svc} | find "does not exist" >nul',
        f"if %ERRORLEVEL% EQU 0 exit 0", ##DOES NOT EXIST
        f"if %ERRORLEVEL% EQU 1 exit 1"  ##EXISTS
    ],
    stdout=sys.stdout)
    result = ret.communicate()[0]
    return result.returncode

def start_service(svc):
    os.system(f"net start {svc}")
    
def stop_service(svc):
    os.system(f"net stop {svc}")
    

def start_website(website):
    ret = subprocess.Popen([
        "powershell.exe",
        f'Start-IISSite -Name "{website}"',
        ""],
        stdout=sys.stdout)
    ret.communicate()
    
def stop_website(website):
    ret = subprocess.Popen([
        "powershell.exe",
        f'Stop-IISSite -Name "{website}"',
        ""],
        stdout=sys.stdout)
    ret.communicate()