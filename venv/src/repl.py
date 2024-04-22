import warframemarket
from cfgparser import loadcfg
from colorama import Fore, init
from datetime import datetime

def cout(text, color) -> None:
    print(f"{color}{text}")

def spit(data):
    data = data.split()
    identifier = data[0]
    parameter = data[1:]
    command = {"identifier": identifier, "parameter": parameter}
    return command


def REPL() -> None:
    try:
        while True:
            try:
                _in = input("WFMConsole >> ")
                if  spit(_in)["identifier"].lower() == "login":
                    #                     0 = email,                1 = password,              2 = platform,        3 = clientId
                    wfm.setUser(spit(_in)["parameter"][0], spit(_in)["parameter"][1], spit(_in)["parameter"][2], spit(_in)["parameter"][3])
                    cout("logging in", Fore.BLUE)
                    try:
                        wfm.login()
                        cout("logged in sucessfully", Fore.GREEN)
                    except:
                        cout("failed to login", Fore.RED)


            except Exception as e:
                cout(f"{datetime.now().strftime(ftimestamp)} - WFMConsole >> Error: {e}", Fore.RED)
    except KeyboardInterrupt as interrupt:
        print("\nClosing REPL")


if __name__ == "__main__":
    init(autoreset=True)
    config = loadcfg()
    ftimestamp = "%Y-%m-%d %H:%M:%S"

    if config["JWT"] == "none":
        cout(f"{datetime.now().strftime(ftimestamp)} - WFMConsole >> Error: JWT token not defined, open config.cfg for instructions.\nExiting...", Fore.RED)
        exit()
    else:
        wfm = warframemarket.api(config["JWT"])

    if config["autologin"] == "true":
        wfm.login()

    cout("Warframe Market Manager v"  + config["version"], Fore.LIGHTBLUE_EX)
    cout("exit() to quit", Fore.LIGHTBLUE_EX)
    print()
    REPL()