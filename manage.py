#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    # Django settings batata hai
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sticky_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc
    # command line se execute karta hai
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
