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
    return False if result.returncode == "0" else True

def start_service(svc):
    os.system(f"net start {svc}")
    
def stop_service(svc):
    os.system(f"net stop {svc}")
    
    
def run_script(path):
    ret = subprocess.run([
        "powershell.exe",
        "Set-ExecutionPolicy -ExecutionPolicy Bypass;",
        f"{path}",
        ],
        shell=True,
        stdout=sys.stdout)
    return "Success" if ret.returncode == 0 else f"Error: {ret.returncode}"
    

def website_exists(website):
    path = os.path.abspath("./src/scripts/check_website_exists.ps1")
    ret = subprocess.run([
        "powershell.exe",
        "Set-ExecutionPolicy -ExecutionPolicy Bypass;",
        f"{path}",
        f"{website}",
        ],
        shell=True,
        stdout=sys.stdout)
    return False if ret.returncode == 0 else True

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