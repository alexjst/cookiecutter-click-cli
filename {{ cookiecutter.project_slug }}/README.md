#{{ cookiecutter.project_name }}
{{ cookiecutter.description }}

{% if cookiecutter.repo_url %}
#Installation
{{ cookiecutter.project_name }} can be installed with pip:
```
pip install {{ cookiecutter.repo_url }}
```
{% endif %}
#Usage
```
Usage: {{ cookiecutter.command }} [OPTIONS] COMMAND [ARGS]...

  {{ cookiecutter.command }} is a command line tool generated from
  https://github.com/cjohnhanson/cookiecutter-click-cli

Options:
  --help  Show this message and exit.

Commands:
  version  Print the version and exit
```
