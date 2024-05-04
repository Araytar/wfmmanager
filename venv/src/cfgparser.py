import configparser
import os

def loadcfg():
    """
    Load the configuration file and return a dictionary of all the values.

    Returns:
        A dictionary containing all the values from the configuration file.
    """
    cdir = os.path.dirname(__file__)
    cfgpath = os.path.join(cdir, "..", "config.cfg")

    rconfig = configparser.ConfigParser()
    rconfig.read(cfgpath)

    #Add all new config points to this dictionary
    config = {
        "version": rconfig.get("development", "version"),
        "autologin": rconfig.get("auth", "autologin"),
        "JWT": rconfig.get("auth", "JWT")
    }
    return config


def loadlang() -> dict:
    lang = {}

    rlang = configparser.ConfigParser()
    rlang.read("lang.cfg")
    