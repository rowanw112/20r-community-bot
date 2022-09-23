import os
import yaml

Path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "Configuration"))


def configfile():
    with open(Path + os.sep + "bot.yml") as file:
        configfile = yaml.full_load(file)
    return configfile


def update():
    pass


