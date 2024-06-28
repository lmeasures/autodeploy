
import errno
import os
import subprocess
import sys


def get_most_recently_modified_directory(search_path):
    return max([f for f in os.scandir(search_path)], key=lambda x: x.stat().st_mtime).path


def mkdir_p(path):
    print("||| Attempting to create directory", path)
    try:
        os.makedirs(path)
        print("|| Success")
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            print("|| Directory Exists")
            pass
        else: raise
        
          
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
    ret = subprocess.run([
        "powershell.exe",
        "Set-ExecutionPolicy -ExecutionPolicy Bypass;",
        "Import-Module IISAdministration;",
        f"$response = Get-IISSite {website} 3>&1;",
        '''if ($response -match "does not")
        { exit 0 }
        else { exit 1 }
        '''
    ])

