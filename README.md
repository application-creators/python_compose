# Python Project Template with Docker Compose

This is a template used by [create_app](https://github.com/application-creators/create_app) to create a 
new Python project with Docker Compose.

To create your new project from this template, simply run:

```shell
pip install create_app
python -m create_app python_compose
```


## What's in this template

 * Project structure
 * Virtualenv
 * Unit tests
 * Docker Compose containerization
 * Pre-commit GIT hooks
   * [Black](https://github.com/psf/black)
   * [Isort](https://pycqa.github.io/isort/)
   * [Flake8](https://flake8.pycqa.org/en/latest/)
 * Makefile with useful commands


## Git hooks

This template uses [pre-commit](https://pre-commit.com/) to run GIT hooks in your repo:
 * [Black](https://github.com/psf/black)
 * [Isort](https://pycqa.github.io/isort/)
 * [Flake8](https://flake8.pycqa.org/en/latest/)

This helps developers to keep the same code styling in the project.

To install the hooks in your repo, first [install pre-commit](https://pre-commit.com/#install) in your system. Then run:
```shell
make install_git_hooks
```


## Docker compose

The project structure has been designed keeping in mind that you may need to have multiple services in your project 
(such as an API and a database, for example). Thus, Docker compose is a good way to get them running together. If you 
need just one container, [python_simple](https://github.com/application-creators/python_simple) may be the way to go.

By default, you get a service named the same as you project package name. You can add as many services you need in the
[root](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D) of your repo, each in their own folder, and declare the
services in 
