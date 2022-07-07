FROM python:3.10


ARG PROJECT_PACKAGE_NAME={{ cookiecutter.project_package_name }}

ARG WORK_DIR=/code
ARG REQUIREMENTS_FILENAME=requirements.frozen


WORKDIR ${WORK_DIR}


COPY ${PROJECT_PACKAGE_NAME} .


RUN pip install -r ${REQUIREMENTS_FILENAME}


CMD python run.py
