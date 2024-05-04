import warframemarket
from cfgparser import loadcfg
from colorama import Fore, init
from datetime import datetime
import database
import time
import os
import json
import base64

def __getStorageCreds() -> dict:
    try:
        with open(".\storage\credentials.json", "r", encoding="utf-8") as file:
            encdata = json.load(file)
            data = base64.b64decode(encdata.encode()).decode()
            return json.loads(data)
    except:
        return None

def cout(text, color) -> None:
    print(f"{color}{text}")

def spit(data):
    data = data.split()
    identifier = data[0]
    parameter = data[1:]
    command = {"identifier": identifier, "parameter": parameter}
    return command

def cmdlogin(_in) -> None:
    if  spit(_in)["identifier"].lower() == "login":
        #                     0 = email,                1 = password,              2 = platform,        3 = clientId
        wfm.setUser(spit(_in)["parameter"][0], spit(_in)["parameter"][1], spit(_in)["parameter"][2], spit(_in)["parameter"][3])
        cout("logging in", Fore.BLUE)
        try:
            wfm.login()
            cout("logged in sucessfully", Fore.GREEN)
            logged_in = True
            time.sleep(0.2)
            cout("Restarting...", Fore.GREEN)
            time.sleep(0.7)
            os.system('cls')
            cout("Warframe Market Manager v"  + config["version"], Fore.LIGHTBLUE_EX)
            if logged_in:
                cout("Logged in as: " + wfm.user["ingame_name"], Fore.LIGHTBLUE_EX)
            cout("use command exit to quit", Fore.LIGHTBLUE_EX)

        except Exception as e:
            cout("failed to login, " + e, Fore.RED)

def cmdclear(_in) -> None:
    if  spit(_in)["identifier"].lower() == "clear":
        os.system('cls')
        cout("Warframe Market Manager v"  + config["version"], Fore.LIGHTBLUE_EX)
        if logged_in:
            cout("Logged in as: ")
            cout("Logged in as: " + wfm.user["ingame_name"], Fore.LIGHTBLUE_EX)
        cout("use command exit to quit", Fore.LIGHTBLUE_EX)

def cmdexit(_in) -> None:
    if spit(_in)["identifier"].lower() == "exit":
        cout("Exiting...", Fore.GREEN)
        time.sleep(0.7)
        exit(0)


def REPL() -> None:
    try:
        while True:
            #try:
                _in = input("WFMConsole >> ")
                cmdlogin(_in)
                cmdexit(_in)
                cmdclear(_in)

            #except Exception as e:
                #cout(f"{datetime.now().strftime(ftimestamp)} - WFMConsole >> Error: {e}", Fore.RED)
    except KeyboardInterrupt as interrupt:
        print("\nClosing REPL")


if __name__ == "__main__":
    init(autoreset=True)

    logged_in = False
    config = loadcfg()
    ftimestamp = "%Y-%m-%d %H:%M:%S"

    if config["JWT"] == "none":
        cout(f"{datetime.now().strftime(ftimestamp)} - WFMConsole >> Error: JWT token not defined, open config.cfg for instructions.\nExiting...", Fore.RED)
        exit()
    else:
        wfm = warframemarket.api(config["JWT"])

    if config["autologin"] == "true" and __getStorageCreds() != None:
        wfm.login()
        logged_in = True

    cout("Warframe Market Manager v"  + config["version"], Fore.LIGHTBLUE_EX)
    if logged_in:
        cout("Logged in as: " + wfm.user["ingame_name"], Fore.LIGHTBLUE_EX)
    cout("use command exit to quit", Fore.LIGHTBLUE_EX)
    print()
    REPL()