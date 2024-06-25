

from cus_types import AppListItem


def application_function_1():
    print("| app 1 change made")

app_list: dict[str, AppListItem] = {
    "application_name": {
        "source_directory": "C:\\Projects\\work_autodeploy\\testbed\\pipeline_output_folder\\application_name",
        "env_target_directory": "C:\\Projects\\work_autodeploy\\testbed\\d$\\envs\\application_name",
        "code_target_directory": "C:\\Projects\\work_autodeploy\\testbed\\d$\\websites\\application_name",
        "app_name": "application_name",
        "app_type": "fast-api",
        "service_name": "DummyService",
        "website_name": "application_name",
        "powershell_script_path": ""
    }
}

