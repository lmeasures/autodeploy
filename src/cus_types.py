from typing import Literal

class AppListItem:
    app_name: str
    source_directory: str
    env_target_directory: str
    code_target_directory: str
    website_name: str
    app_type: Literal["flask-api","fast-api","python-fe","react-fe","vue-fe"]
    powershell_script_path: str
    service_name = None
    
   