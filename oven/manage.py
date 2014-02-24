#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    settings = {
        'test': "oven.settings.test",
        'dev': "oven.settings.local"
    }

    if sys.argv[1] == 'test':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings['test'])
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings['dev'])

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
