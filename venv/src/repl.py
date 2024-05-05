import warframemarket
from cfgparser import loadcfg, loadlang
from colorama import Fore, init
from datetime import datetime
from database import Database
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

def cmdlogin(_in, logged_in) -> None:
    if  spit(_in)["identifier"].lower() == "login":
        if logged_in == True:
            cout(lang["cmdlogin.already_logged_in"], Fore.RED)
            time.sleep(2)
            os.system('cls')
            cout(lang["startup.header"]  + config["version"], Fore.LIGHTBLUE_EX)
            if logged_in:
                cout(lang["startup.loggedin"] + " " + wfm.user["ingame_name"], Fore.LIGHTBLUE_EX)
            cout(lang["startup.subheader"], Fore.LIGHTBLUE_EX)

        else:
            #                     0 = email,                1 = password,              2 = platform
            wfm.setUser(spit(_in)["parameter"][0], spit(_in)["parameter"][1], spit(_in)["parameter"][2], "Client")
            cout(lang["cmdlogin.loginheader"], Fore.BLUE)
            try:
                wfm.login()
                cout(lang["cmdlogin.login_success"], Fore.GREEN)
                logged_in = True
                time.sleep(0.2)
                cout(lang["cmdlogin.restarting"], Fore.GREEN)
                time.sleep(0.7)
                os.system('cls')
                cout(lang["startup.header"]  + config["version"], Fore.LIGHTBLUE_EX)
                if logged_in:
                    cout(lang["startup.loggedin"] + " " + wfm.user["ingame_name"], Fore.LIGHTBLUE_EX)
                cout(lang["startup.subheader"], Fore.LIGHTBLUE_EX)

            except Exception as e:
                cout(lang["cmdlogin.login_failure"] + e, Fore.RED)

def cmdclear(_in) -> None:
    if  spit(_in)["identifier"].lower() == "clear":
        os.system('cls')
        cout(lang["startup.header"]  + config["version"], Fore.LIGHTBLUE_EX)
        if logged_in:
            cout(lang["startup.loggedin"] + " " + wfm.user["ingame_name"], Fore.LIGHTBLUE_EX)
        cout(lang["startup.subheader"], Fore.LIGHTBLUE_EX)

def cmdexit(_in) -> None:
    if spit(_in)["identifier"].lower() == "exit":
        cout(lang["cmdexit.exiting"], Fore.GREEN)
        time.sleep(0.7)
        exit(0)


def REPL() -> None:
    try:
        while True:
            #try:
                _in = input("WFMConsole >> ")
                cmdlogin(_in, logged_in)
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
    lang = loadlang(config["language"])

    if config["jwt"] == "none":
        cout(datetime.now().strftime(ftimestamp) + " " + lang["startup.jwt_failure"], Fore.RED)
        exit()
    else:
        wfm = warframemarket.api(config["jwt"])

    if config["autologin"] == "true" and __getStorageCreds() != None:
        wfm.login()
        logged_in = True

    cout(lang["startup.header"]  + config["version"], Fore.LIGHTBLUE_EX)
    if logged_in:
        cout(lang["startup.loggedin"] + " " + wfm.user["ingame_name"], Fore.LIGHTBLUE_EX)
    cout(lang["startup.subheader"], Fore.LIGHTBLUE_EX)
    print()
    REPL()