import requests
import socket
import json
from cfgparser import loadcfg
import base64

class api:

    def __init__(self, JWS) -> None:
        """
        It's an init, what about it?.

        Args:
            JWS (str): The user's JWT.
        """
        #load config
        self.config = loadcfg()

        #create thoudsands of variables
        self.user = {}
        self.device_id = socket.gethostname()
        self.JWS = JWS
        self.email = None
        self.password = None
        self.platform = None
        self.clientId = None
        self.credentials = {}
        self.BASEURL = "https://api.warframe.market/v1"

        #create the request session
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "MarketManager/0.2.0, Developer: Araytar",
            "authorization": "JWT " + self.JWS
        })


    def setUser(self, email, password, platform, clientId="Client") -> None:
        """Sets the user credentials for the API.
        Args:
            email (str): The user's email address.
            password (str): The user's password.
            platform (str): The user's platform.
            clientId (str): default: <Client>, The  Client id .
        Returns:
            void
        """
        self.email = email
        self.password = password
        self.clientId = clientId
        self.platform = platform
        self.credentials = {
            "email": self.email,
            "password": self.password,
            "deviceId": str(self.device_id),
            "clientId": self.clientId
        }

    def login(self) -> None:
        """
        Logs the user into the Warframe Market API.

        Returns:
            None
        """

        def getStorageCreds() -> dict:
            """
            Reads the stored user credentials from the local storage.

            Returns:
                dict: The stored user credentials.
            """
            try:
                with open(".\storage\credentials.json", "r", encoding="utf-8") as file:
                    encdata = json.load(file)
                    data = base64.b64decode(encdata.encode()).decode()
                    return json.loads(data)
            except:
                return None

        def writeStorageCreds(data) -> None:
            """
            Writes the user credentials to the local storage.

            Args:
                data (dict): The user credentials to be stored.
            """
            json_data = json.dumps(data)
            data = base64.b64encode(json_data.encode()).decode()
            with open(".\storage\credentials.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

        if self.config["autologin"] == "true" and getStorageCreds() != None:
            self.credentials = getStorageCreds()
            response = self.session.post(url=self.BASEURL + "/auth/signin", json=self.credentials)
            data = response.json()["payload"]["user"]
            self.user = {
                "ingame_name": data["ingame_name"],
                "id": data["id"],
                "banned": data["banned"],
                "platform": data["platform"],
                "anonymous": data["anonymous"],
                "has_mail": data["has_mail"],
                "unread_messages": data["unread_messages"],
                "verification": data["verification"],
                "region": data["region"],
                "written_reviews": data["written_reviews"],
                "reputation": data["reputation"],
                "preferred_lang": data["locale"],
                "region": data["region"],
                "role": data["role"],
                "avatar": data["avatar"],
                "background": data["background"],
                "check_code": data["check_code"],
                "linked_steam_profile": data["linked_accounts"]["steam_profile"],
                "linked_patreon_profile": data["linked_accounts"]["patreon_profile"],
                "linked_xbox_profile": data["linked_accounts"]["xbox_profile"],
                "linked_discord_profile": data["linked_accounts"]["discord_profile"],
                "linked_github_profile": data["linked_accounts"]["github_profile"],
            }


        elif self.config["autologin"] == "true" and getStorageCreds() == None:
            response = self.session.post(url=self.BASEURL + "/auth/signin", json=self.credentials)
            data = response.json()["payload"]["user"]
            self.user = {
                "ingame_name": data["ingame_name"],
                "id": data["id"],
                "banned": data["banned"],
                "platform": data["platform"],
                "anonymous": data["anonymous"],
                "has_mail": data["has_mail"],
                "unread_messages": data["unread_messages"],
                "verification": data["verification"],
                "region": data["region"],
                "written_reviews": data["written_reviews"],
                "reputation": data["reputation"],
                "preferred_lang": data["locale"],
                "region": data["region"],
                "role": data["role"],
                "avatar": data["avatar"],
                "background": data["background"],
                "check_code": data["check_code"],
                "linked_steam_profile": data["linked_accounts"]["steam_profile"],
                "linked_patreon_profile": data["linked_accounts"]["patreon_profile"],
                "linked_xbox_profile": data["linked_accounts"]["xbox_profile"],
                "linked_discord_profile": data["linked_accounts"]["discord_profile"],
                "linked_github_profile": data["linked_accounts"]["github_profile"],
            }
            writeStorageCreds(self.credentials)

        elif self.config["autologin"] == "false":
            response = self.session.post(url=self.BASEURL + "/auth/signin", json=self.credentials)
            data = response.json()["payload"]["user"]
            self.user = {
                "ingame_name": data["ingame_name"],
                "id": data["id"],
                "banned": data["banned"],
                "platform": data["platform"],
                "anonymous": data["anonymous"],
                "has_mail": data["has_mail"],
                "unread_messages": data["unread_messages"],
                "verification": data["verification"],
                "region": data["region"],
                "written_reviews": data["written_reviews"],
                "reputation": data["reputation"],
                "preferred_lang": data["locale"],
                "region": data["region"],
                "role": data["role"],
                "avatar": data["avatar"],
                "background": data["background"],
                "check_code": data["check_code"],
                "linked_steam_profile": data["linked_accounts"]["steam_profile"],
                "linked_patreon_profile": data["linked_accounts"]["patreon_profile"],
                "linked_xbox_profile": data["linked_accounts"]["xbox_profile"],
                "linked_discord_profile": data["linked_accounts"]["discord_profile"],
                "linked_github_profile": data["linked_accounts"]["github_profile"],
            }