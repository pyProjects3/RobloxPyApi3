import requests
import socket

import RobloxPyApi3
from RobloxPyApi3.Errors import APIConnectFailed,AcceptFriendRequestFailed,DeclineFriendRequestFailed,DeclineAllFriendsRequest
def Accept_Friend_Request(cookie,UserId, showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    api = requests.post(f'https://friends.roblox.com/v1/users/{UserId}/accept-friend-request',headers={"Accept":"application/json",'cookies':f".ROBLOSECURITY={cookie};","x-csrf-token":RobloxPyApi3.Get_x_csrf_token(cookie=cookie,showErrors=showErrors)},cookies={".ROBLOSECURITY":cookie})
    if api.status_code == 200:
        return 200
    elif 'errors' in api.json():
        if showErrors == True:
            raise AcceptFriendRequestFailed(f"Failed to accept request, make sure the requested user sent friend request. Error: {api.json()['errors'][0]['message']}")
        else:
            return
def Decline_Friend_Request(cookie,UserId, showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    api = requests.post(f'https://friends.roblox.com/v1/users/{UserId}/decline-friend-request',headers={"Accept":"application/json",'cookies':f".ROBLOSECURITY={cookie};","x-csrf-token":RobloxPyApi3.Get_x_csrf_token(cookie=cookie,showErrors=showErrors)},cookies={".ROBLOSECURITY":cookie})
    if api.status_code == 200:
        return 200
    elif 'errors' in api.json():
        if showErrors == True:
            raise DeclineFriendRequestFailed(f"Failed to decline request, make sure the requested user sent friend request. Error: {api.json()['errors'][0]['message']}")
        else:
            return

def Decline_All_Friend_Requests(cookie, showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    api = requests.post(f'https://friends.roblox.com/v1/user/friend-requests/decline-all',cookies={".ROBLOSECURITY":cookie},headers={"Accept":"application/json","x-csrf-token":RobloxPyApi3.Get_x_csrf_token(cookie=cookie,showErrors=showErrors)})
    if api.status_code == 200:
        return 200
    elif 'errors' in api.json():
        if showErrors == True:
            raise DeclineAllFriendsRequest(f"Failed to accept request, make sure the requested user sent friend request. Error: {api.json()['errors'][0]['message']}")
        else:
            return

def Get_Friend_Metadata(cookie,UserId, showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    api = requests.get(f'https://friends.roblox.com/v1/metadata?targetUserId={UserId}',headers={"Accept":"application/json",'cookies':f".ROBLOSECURITY={cookie};"},cookies={".ROBLOSECURITY":cookie})
    if api.status_code == 200:
        return 200
    elif 'errors' in api.json():
        if showErrors == True:
            raise AcceptFriendRequestFailed(f"Failed to accept request, make sure the requested user sent friend request. Error: {api.json()['errors'][0]['message']}")
        else:
            return
def Get_Friends_Count(cookie, showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    api = requests.get(f'https://friends.roblox.com/v1/my/friends/count',headers={"Accept":"application/json",'cookies':f".ROBLOSECURITY={cookie};"},cookies={".ROBLOSECURITY":cookie})
    if api.status_code == 200:
        return 200
    elif 'errors' in api.json():
        if showErrors == True:
            raise AcceptFriendRequestFailed(f"Failed to accept request, make sure the requested user sent friend request. Error: {api.json()['errors'][0]['message']}")
        else:
            return
