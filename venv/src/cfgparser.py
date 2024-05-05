import configparser
import os


def loadcfg() -> dict:
    """
    Load the configuration file and return a dictionary of all the values.

    Returns:
        A dictionary containing all the values from the configuration file.
    """
    cdir = os.path.dirname(__file__)
    cfgpath = os.path.join(cdir, "..", "config.cfg")

    rconfig = configparser.ConfigParser()
    rconfig.read(cfgpath)

    config = {}

    for section in rconfig.sections():
        for option in rconfig.options(section):
            config[option] = rconfig.get(section, option)

    return config


def loadlang(language) -> dict:
    """
    Load a specific language configuration from a file and return it as a dictionary.

    Parameters:
    language (str): The language code to load.

    Returns:
    dict: A dictionary containing the language configuration.

    Raises:
    FileNotFoundError: If the language configuration file does not exist.
    configparser.ParsingError: If there is an error parsing the language configuration file.

    """
    cdir = os.path.dirname(__file__)
    langpath = os.path.join(cdir, "assets", "lang.cfg")

    lang = {}

    rlang = configparser.ConfigParser()
    rlang.read(langpath)

    if language in rlang:
        for option in rlang.options(language):
            lang[option] = rlang.get(language, option)

    return lang
    