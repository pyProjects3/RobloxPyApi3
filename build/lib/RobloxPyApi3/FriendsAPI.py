from RobloxPyApi3.Utilities import Post_Request as __Post_Request__, \
    Get_Request as __Get_Request__
import requests
import RobloxPyApi3.Errors as Errors
from RobloxPyApi3.Enums import sortOrder
def Get_Friends_Metatable(session, targetUserId, showErrors=True) -> requests.Response:
    try:
        req = __Get_Request__(f"https://friends.roblox.com/v1/metadata?targetUserId={targetUserId}",
                              session=session)
        if req.status_code != 200:
            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")
        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))


def Get_Friends_Count(session, showErrors=True) -> requests.Response:
    try:
        req = __Get_Request__(f"https://friends.roblox.com/v1/my/friends/count",
                              session=session)
        if req.status_code != 200:
            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")
        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))


def Get_Friend_Requests(session, Limit, cursor, SortOrder:sortOrder, showErrors=True) -> requests.Response:
    try:
        req = __Get_Request__(
            f"https://friends.roblox.com/v1/my/friends/requests?limit={Limit}&cursor={cursor}&sortOrder={SortOrder.value}",
            session=session)
        if req.status_code != 200:
            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")
        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))


def Get_Friend_Request_Count(session, showErrors=True) -> requests.Response:
    try:
        req = __Get_Request__(f"https://friends.roblox.com/v1/user/friend-requests/count",
                              session=session)
        if req.status_code != 200:
            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")
        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))


def Get_User_Followers(session, targetUserId, Limit, cursor, SortOrder:sortOrder, showErrors=True) -> requests.Response:
    try:
        req = __Get_Request__(
            f"https://friends.roblox.com/v1/users/{targetUserId}/followers?limit={Limit}&cursor={cursor}&sortOrder={SortOrder.value}",
            session=session)
        if req.status_code != 200:
            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")
        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))


def Get_User_Followers_Count(session, targetUserId, showErrors=True) -> requests.Response:
    try:
        req = __Get_Request__(f"https://friends.roblox.com/v1/users/{targetUserId}/followers/count",
                              session=session)
        if req.status_code != 200:
            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")
        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))


def Get_User_Followings(session, targetUserId, Limit, cursor, SortOrder, showErrors=True) -> requests.Response:
    try:
        req = __Get_Request__(
            f"https://friends.roblox.com/v1/users/{targetUserId}/followings?limit={Limit}&cursor={cursor}&sortOrder={SortOrder.value}",
            session=session)
        if req.status_code != 200:
            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")
        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))


def Get_User_Friends(session, targetUserId, showErrors=True) -> requests.Response:
    try:
        req = __Get_Request__(f"https://friends.roblox.com/v1/users/{targetUserId}/friends",
                              session=session)
        if req.status_code != 200:
            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")
        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))


def Get_User_Friends_Count(session, targetUserId, showErrors=True) -> requests.Response:
    try:
        req = __Get_Request__(f"https://friends.roblox.com/v1/users/{targetUserId}/friends/count",
                              session=session)
        if req.status_code != 200:
            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")
        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))


def Get_User_Inactive_Friends(session, targetUserId, showErrors=True) -> requests.Response:
    try:
        req = __Get_Request__(f"https://friends.roblox.com/v1/users/{targetUserId}/friends/inactive",
                              session=session)
        if req.status_code != 200:
            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")
        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))


def Get_User_Online_Friends(session, targetUserId, showErrors=True) -> requests.Response:
    try:
        req = __Get_Request__(f"https://friends.roblox.com/v1/users/{targetUserId}/friends/online",
                              session=session)
        if req.status_code != 200:
            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")
        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))


def Get_User_InactiveFriends_Count(session, targetUserId, showErrors=True) -> requests.Response:
    try:
        req = __Get_Request__(f"https://friends.roblox.com/v1/users/{targetUserId}/friends/inactive/count",
                              session=session)
        if req.status_code != 200:
            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")
        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))


def Decline_All_Friend_Requests(session, showErrors=True) -> requests.Response:
    try:
        req = __Post_Request__(f"https://friends.roblox.com/v1/user/friend-requests/decline-all",
                               session=session,
                               data={

                               })
        if req.status_code != 200:
            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")
        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))


def AcceptFriendRequest(session, requesterUserId, showErrors=True) -> requests.Response:
    try:
        req = __Post_Request__(f"https://friends.roblox.com/v1/users/{requesterUserId}/accept-friend-request",
                               session=session,
                               data={

                               })
        if req.status_code != 200:
            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")
        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))


def DeclineFriendRequest(session, requesterUserId, showErrors=True) -> requests.Response:
    try:
        req = __Post_Request__(f"https://friends.roblox.com/v1/users/{requesterUserId}/decline-friend-request",
                               session=session,
                               data={

                               })
        if req.status_code != 200:
            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")
        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))


def SendFriendRequest(session, targetUserId, showErrors=True) -> requests.Response:
    try:
        print(session)
        req = __Post_Request__(f"https://friends.roblox.com/v1/users/{targetUserId}/request-friendship",
                               session=session,
                               data={

                               })
        print(req)
        if req.status_code != 200:
            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")
        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))

def Unfriend(session, targetUserId, showErrors=True) -> requests.Response:
    try:
        print(session)
        req = __Post_Request__(f"https://friends.roblox.com/v1/users/{targetUserId}/unfriend",
                               session=session,
                               data={

                               })
        print(req)
        if req.status_code != 200:
            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")
        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))

class FriendsSession(object):
    def __init__(self, session, password):
        self.Session = session
        self.Password = password

    def Get_Friends_Metatable(self, targetUserId, showErrors=True):
        return Get_Friends_Metatable(self.Session, targetUserId, showErrors=showErrors)

    def Get_Friends_Count(self, showErrors=True):
        return Get_Friends_Count(self.Session, showErrors=showErrors)

    def Get_Friend_Requests(self, Limit, cursor, sortOrder, showErrors=True):
        return Get_Friend_Requests(self.Session, Limit, cursor, sortOrder, showErrors=showErrors)

    def Get_Friend_Request_Count(self, showErrors=True):
        return Get_Friend_Request_Count(self.Session, showErrors=showErrors)

    def Get_User_Followers(self, targetUserId, Limit, cursor, sortOrder, showErrors=True):
        return Get_User_Followers(self.Session, targetUserId, Limit, cursor, sortOrder, showErrors=showErrors)

    def Get_User_Followers_Count(self, targetUserId, showErrors=True):
        return Get_User_Followers_Count(self.Session, targetUserId, showErrors=showErrors)

    def Get_User_Followings(self, targetUserId, Limit, cursor, sortOrder, showErrors=True):
        return Get_User_Followings(self.Session, targetUserId, Limit, cursor, sortOrder, showErrors=showErrors)

    def Get_User_Friends(self, targetUserId, showErrors=True):
        return Get_User_Friends(self.Session, targetUserId, showErrors=showErrors)

    def Get_User_Friends_Count(self, targetUserId, showErrors=True):
        return Get_User_Friends_Count(self.Session, targetUserId, showErrors=showErrors)

    def Get_User_Inactive_Friends(self, targetUserId, showErrors=True):
        return Get_User_Inactive_Friends(self.Session, targetUserId, showErrors=showErrors)

    def Get_User_Online_Friends(self, targetUserId, showErrors=True):
        return Get_User_Online_Friends(self.Session, targetUserId, showErrors=showErrors)

    def Get_User_InactiveFriends_Count(self, targetUserId, showErrors=True):
        return Get_User_InactiveFriends_Count(self.Session, targetUserId, showErrors=showErrors)

    def Decline_All_Friend_Requests(self, showErrors=True):
        return Decline_All_Friend_Requests(self.Session, showErrors=showErrors)

    def AcceptFriendRequest(self, requesterUserId, showErrors=True):
        return AcceptFriendRequest(self.Session, requesterUserId, showErrors=showErrors)

    def DeclineFriendRequest(self, requesterUserId, showErrors=True):
        return DeclineFriendRequest(self.Session, requesterUserId, showErrors=showErrors)

    def SendFriendRequest(self, targetUserId, showErrors=True):
        return SendFriendRequest(session=self.Session, targetUserId=targetUserId, showErrors=showErrors)
    def Unfriend(self, targetUserId, showErrors=True):
        return Unfriend(self.Session, targetUserId, showErrors=showErrors)