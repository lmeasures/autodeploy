
def application_function_1():
    print("app 1 change made")
def application_function_2():
    print("app 2 change made")

app_list = {
    "application_name": {
        "source_directory": "C:\\Projects\\work_autodeploy\\testbed\\pipeline_output_folder\\application_name",
        "env_target_directory": "C:\\Projects\\work_autodeploy\\testbed\\env_deployment_folder\\application_name",
        "code_target_directory": "C:\\Projects\\work_autodeploy\\testbed\\code_deployment_folder\\application_name",
        "app_name": "application_name",
        "service_name": "",
        "website_name": "",
        "function": application_function_1
    },
    "application_name_2": {
        "source_directory": "C:\\Projects\\work_autodeploy\\testbed\\pipeline_output_folder\\application_name_2",
        "env_target_directory": "C:\\Projects\\work_autodeploy\\testbed\\env_deployment_folder\\application_name_2",
        "code_target_directory": "C:\\Projects\\work_autodeploy\\testbed\\code_deployment_folder\\application_name_2",
        "app_name": "application_name_2",
        "service_name": "",
        "website_name": "",
        "function": application_function_2
    },
}