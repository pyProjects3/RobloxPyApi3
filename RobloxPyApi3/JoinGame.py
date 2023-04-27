import RobloxPyApi3.Utilities as Utilities
import subprocess
from RobloxPyApi3.Errors import JoinGameFailed,NoRobloxProcessFound,APIConnectFailed,AuthenticationError
import random
import socket
import requests

import psutil
def Get_Authentication_ticket(cookie,gameid,showErrors=True):
    try:
        socket.create_connection(('google.com',80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    API = requests.post("https://auth.roblox.com/v1/authentication-ticket/",headers={"Accept": "application/json","x-csrf-token":Utilities.GetToken(),"referer":f"https://www.roblox.com/games/{gameid}","cookie":f".ROBLOSECURITY={cookie}"})
    if "rbx-authentication-ticket" in API.headers:
        return API.headers["rbx-authentication-ticket"]
    else:
        if showErrors == True:
            raise AuthenticationError("Failed to find 'rbx-authentication-ticket' in the headers.")
        else:
            return
def Get_Authentication_ticket_Session(session,gameid,showErrors=True):
    try:
        socket.create_connection(('google.com',80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    if session:
        API = session.post("https://auth.roblox.com/v1/authentication-ticket/",
                            headers={"Accept": "application/json", "x-csrf-token": Utilities.GetToken(session),
                                     "referer": f"https://www.roblox.com/games/{gameid}"})
        if "rbx-authentication-ticket" in API.headers:
            return API.headers["rbx-authentication-ticket"]
        else:
            if showErrors == True:
                raise AuthenticationError("Failed to find 'rbx-authentication-ticket' in the headers.")
            else:
                return
    else:

        API = requests.post("https://auth.roblox.com/v1/authentication-ticket/",headers={"Accept": "application/json","x-csrf-token":Utilities.GetToken(),"referer":f"https://www.roblox.com/games/{gameid}"})
        if "rbx-authentication-ticket" in API.headers:
            return API.headers["rbx-authentication-ticket"]
        else:
            if showErrors == True:
                raise AuthenticationError("Failed to find 'rbx-authentication-ticket' in the headers.")
            else:
                return
def FindRobloxLauncherProcess():
    processName = "RobloxPlayerBeta"

    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess) as a:
            raise NoRobloxProcessFound("RobloxPlayerBeta")
    return False
def JoinGame(cookie, gameId=int, showErrors=bool):
    try:
        x_csrf_token = Get_Authentication_ticket(cookie=cookie,gameid=gameId,showErrors=showErrors)
        browserId = random.randint(1000000, 10000000)
        #os.chdir("C:\\Program Files (x86)\\Roblox\\Versions")
        subprocess.run(f'start roblox-player:1+launchmode:play+gameinfo:{x_csrf_token}+launchtime:{browserId}+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{browserId}%26placeId%3D{gameId}%26isPlayTogetherGame%3Dfalse+browsertrackerid:{browserId}+robloxLocale:en_us+gameLocale:en_us+channel:',shell=True)
        return 200
    except Exception as error:
        if showErrors:
            raise JoinGameFailed(f"During the command execution, an error has been accrued, Exception: {error} ")
        else:
            return

def JoinGameSession(session, gameId=int, showErrors=True):
    try:
        x_csrf_token = Get_Authentication_ticket_Session(session=session,gameid=gameId,showErrors=showErrors)
        browserId = random.randint(1000000, 10000000)
        print(browserId)
        print(x_csrf_token)
        #os.chdir("C:\\Program Files (x86)\\Roblox\\Versions")
        subprocess.run(f'start roblox-player:1+launchmode:play+gameinfo:{x_csrf_token}+launchtime:{browserId}+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{browserId}%26placeId%3D{gameId}%26isPlayTogetherGame%3Dfalse+browsertrackerid:{browserId}+robloxLocale:en_us+gameLocale:en_us+channel:',shell=True)
        return 200
    except Exception as error:
        if showErrors:
            raise JoinGameFailed(f"During the command execution, an error has been accrued, Exception: {error} ")
        else:
            return

def JoinServerWithLocateName(cookie, gameId=int, showErrors=True):
    try:
        x_csrf_token = Get_Authentication_ticket(cookie=cookie,gameid=gameId,showErrors=showErrors)
        browserId = random.randint(1000000, 10000000)
        #os.chdir("C:\\Program Files (x86)\\Roblox\\Versions")
        subprocess.run(f'start roblox-player:1+launchmode:play+gameinfo:{x_csrf_token}+launchtime:{browserId}+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{browserId}%26placeId%3D{gameId}%26isPlayTogetherGame%3Dfalse+browsertrackerid:{browserId}+robloxLocale:en_us+gameLocale:en_us+channel:',shell=True)
        return 200
    except Exception as error:
        if showErrors:
            raise JoinGameFailed(f"During the command execution, an error has been accrued, Exception: {error} ")
        else:
            return

class RobloxProcOpen(object):
    def __init__(self,session):
        self.Session = session
    def JoinGame(self,GameId=int,showErrors=True):
        return JoinGameSession(session=self.Session,gameId=GameId,showErrors=showErrors)