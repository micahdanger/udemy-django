#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    # ADDED THIS TO HELP MANAGE.PY FIND SITE-PACKAGES
    sys.path.append('/Users/micahbeckman/codeprojects/udemy-django/first_project/djangoenv_first_project/lib/python3.7/site-packages')

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
