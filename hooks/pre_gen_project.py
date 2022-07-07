from keyword import iskeyword
from sys import exit

PROJECT_PACKAGE_NAME = "{{ cookiecutter.project_package_name }}"


def validate_project_package_name(package_name: str) -> None:
    if not package_name.isidentifier() or iskeyword(package_name):
        print(
            "The project package name (project_package_name) must "
            "be a valid python package name"
        )
        exit(1)


VALIDATIONS = {
    PROJECT_PACKAGE_NAME: validate_project_package_name,
}


for setting_value, validation_function in VALIDATIONS.items():
    validation_function(setting_value)
