import requests
from RobloxPyApi3.Errors import APIConnectFailed,APIError,GetAvatarMetadataFailed,GetAvatarRulesFailed,InvalidUserId
import socket
class RigTypes:
    R6 = "R6"
    R15 = "R15"
    def __init__(self):
        self.R15 = "R15"
        self.R6 = "R6"
def GetAvatarDetails(cookie, showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:

            raise APIError(
                f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()

def GetAvatarScales(cookie, showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:

            raise APIError(
                f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()['scales']
def GetAvatarRigTypeEnum(cookie, showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:

            raise APIError(
                f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        if a.json()['playerAvatarType'] == "R6":
            return RigTypes.R6
        elif a.json()['playerAvatarType'] == "R15":
            return RigTypes.R15
def GetAvatarType(cookie, showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:

            raise APIError(
                f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()['playerAvatarType']
def GetAvatarRigType(cookie, showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:

            raise APIError(
                f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()['playerAvatarType']
def GetAvatarAssets(cookie, showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:

            raise APIError(
                f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()['assets']
def GetAvatarEmotes(cookie, showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:

            raise APIError(
                f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()['emotes']
def IsWearingDefaultShirt(cookie, showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:

            raise APIError(
                f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()['defaultShirtApplied']
def IsWearingDefaultPants(cookie, showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:

            raise APIError(
                f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()['defaultPantsApplied']
def GetAvatar(cookie, showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:

            raise APIError(
                f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def GetAvatarMetadata(cookie, showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/avatar/metadata",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:

            raise GetAvatarMetadataFailed(
                f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def GetAvatarRules(cookie, showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/avatar-rules",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:

            raise GetAvatarRulesFailed(
                f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def GetAvatarFromUser(cookie, UserId=int,showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/users/{UserId}/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['Message'] == "The specified user does not exist.":
                raise InvalidUserId(f"{a.json()['errors'][0]['Message']}")
            else:
                raise APIError(
                    f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def GetAvatarBodyColorsFromUser(cookie, UserId=int,showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/users/{UserId}/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['Message'] == "The specified user does not exist.":
                raise InvalidUserId(f"{a.json()['errors'][0]['Message']}")
            else:
                raise APIError(
                    f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()['bodyColors']
def GetAvatarScalesFromUser(cookie, UserId=int,showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/users/{UserId}/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['Message'] == "The specified user does not exist.":
                raise InvalidUserId(f"{a.json()['errors'][0]['Message']}")
            else:
                raise APIError(
                    f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()['scales']
def GetAvatarEmotesFromUser(cookie, UserId=int,showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/users/{UserId}/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['Message'] == "The specified user does not exist.":
                raise InvalidUserId(f"{a.json()['errors'][0]['Message']}")
            else:
                raise APIError(
                    f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()['emotes']
def GetAvatarAssetsFromUser(cookie, UserId=int,showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/users/{UserId}/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['Message'] == "The specified user does not exist.":
                raise InvalidUserId(f"{a.json()['errors'][0]['Message']}")
            else:
                raise APIError(
                    f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()['assets']
def GetAvatarRigTypeEnumFromUser(cookie, UserId=int,showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/users/{UserId}/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['Message'] == "The specified user does not exist.":
                raise InvalidUserId(f"{a.json()['errors'][0]['Message']}")
            else:
                raise APIError(
                    f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        if a.json()['playerAvatarType'] == "R15":
            return RigTypes.R15
        elif a.json()['playerAvatarType'] == "R6":
            return RigTypes.R6
        else:
            return
def GetAvatarRigTypeFromUser(cookie, UserId=int,showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/users/{UserId}/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['Message'] == "The specified user does not exist.":
                raise InvalidUserId(f"{a.json()['errors'][0]['Message']}")
            else:
                raise APIError(
                    f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()['playerAvatarType']
def CheckIfUserAvatarDefaultPantsApplied(cookie, UserId=int,showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/users/{UserId}/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['Message'] == "The specified user does not exist.":
                raise InvalidUserId(f"{a.json()['errors'][0]['Message']}")
            else:
                raise APIError(
                    f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()['defaultPantsApplied']
def CheckIfUserAvatarDefaultShirtApplied(cookie, UserId=int,showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/users/{UserId}/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['Message'] == "The specified user does not exist.":
                raise InvalidUserId(f"{a.json()['errors'][0]['Message']}")
            else:
                raise APIError(
                    f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()['defaultShirtApplied']
    
def GetAvatarBodyColorsIds(cookie, showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://avatar.roblox.com/v1/avatar",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:

            raise APIError(
                f"A process returned exception, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()['bodyColors']