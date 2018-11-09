'''
Configuration Settings
'''
import compat
import os
import json
settings = None

def load_settings():
    global settings
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.json')) as f:
        settings = json.load(f)

def update_settings(key, val):
    global settings
    load_settings()
    settings[key] = val
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.json'), 'w') as f:
        json.dump(settings, f, indent=4)

def get_setting(key):
    global settings
    load_settings()
    return settings[key]

load_settings()