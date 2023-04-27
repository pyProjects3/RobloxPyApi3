# This package made by pyProjects3 for Roblox.
# Scroll till the end to see more information and QNA!
#import socket

from RobloxPyApi3.Version import *
from RobloxPyApi3.Avatar import * #list_bundles_from_assetId,Get_Bundle_Details,Get_BundleName_From_BundleId,Get_Items_From_Bundle,CheckIf_Item_In_Bundle,Find_Item_In_Bundle,Get_Bundle_Recommendation,Find_Bundle_in_Bundle_Recommendation,Get_Bundles_Names_owned_by_Player,Get_Bundles_Ids_owned_by_Player,CheckIf_Item_In_Bundle_IsOwned,Asset_To_Subcategory,Get_subcategories,Get_Categories,Get_asset_To_Category,Get_Asset_Favorites_Count,Unpack_Bundle,Favorite_Asset,Favorite_Bundle,Delete_Favorite_Asset,Delete_Favorite_Bundle,Get_Items_Details,Items_Details,Get_Bundle_Favorites_Count,Get_Favorite_Bundle,Get_Favorite_Asset,UnFavorite_Bundle,Create_Favorite_Asset,Create_Favorite_Bundle,UnFavorite_Asset
from RobloxPyApi3.Errors import * #Error,GetCategoriesFailed,APIConnectFailed,InvalidBundleId,ListBundlesFromAssetIdFailed,InvalidAssetId,NoItemFound,FindItemInBundleFailed,GetBundleDetailsFailed,GetBundleRecommendationFailed,InvalidUserId,GetPlayerBundlesFailed,NoContentError,UnpackBundleFailed,GetassetToCategoryFailed,GetassetToSubCategoryFailed
from RobloxPyApi3.Client import *
from RobloxPyApi3.__Changes__ import *
from RobloxPyApi3.friends import *
from RobloxPyApi3.JoinGame import *
from RobloxPyApi3.LeaveGame import *
import time
from RobloxPyApi3Update import *
from colorama import init,Fore
from RobloxPyApi3.Catalog import * #RigTypes,GetAvatarBodyColorsIds,GetAvatarDetails
init(convert=True)

__Author__= Version.__Author__
__PythonVersion__ = Version.__PythonVersion__
__ProgrammingLanguage__ = Version.__ProgrammingLanguage__
__FileName__ = "__init__.py"
__version__ = Version.__PackageVersion__
__Copyright__ = Version.__Copyright__
__Package__ = Version.__Package__
__GitHubUsername__ = Version.__GitHubUsername__
__GitHubPage__ = Version.__GitHubPage__
__GitHub__ = Version.__GitHub__
__moduleName__ = Version.__moduleName__
__RobloxUserName__ = Version.__RobloxUserName__
__RobloxProfile__ = Version.__RobloxUserId__
__RobloxUserId__ = Version.__RobloxUserName__
__RobloxPackages__ = ['RoPy','RobloxApi3','RobloxPyApi3','Pyblox','roblox.py']
class APIError(Exception):
    # raised when API request has errors and cant POST or GET.
    pass
class GetIdFailed(Exception):
    pass
class AuthenticationError(Exception):
    pass
class NoHeadersError(Exception):
    pass
class EmailVerificationFailed(Exception):
    pass
class ChangeDescriptionFailed(Exception):
    pass
class GetAllUserBadgesFailed(Exception):
    pass
class InvalidCookie(Exception):
    pass
class GetTokenException(Exception):
    pass
class SendMessageFailed(Exception):
    pass
class APIConnectFailed(Exception):

    pass
class APIPostError(Exception):
    pass
class FindUserBadgeFailed(Exception):
    pass
class TokenValidationFailed(Exception):
    pass
class InvalidCookieOrNoCookie(Exception):
    pass
class RobuxCheckFailed(Exception):
    pass
class CheckIsBannedFailed(Exception):
    pass
class GetMetadataFailed(Exception):
    pass
class AccountCheckError(Exception):
    pass
class UserNotFoundError(Exception):
    pass
class AuthTicketException(Exception):
    pass
class GetDisplayNameFailed(Exception):
    pass
class APIDeleteError(Exception):
    pass
class GetValidUsernameFailed(Exception):
    pass
class GetUserNameFailed(Exception):
    pass
class GetConversationError(Exception):
    pass
class RemoveStarCodeFailed(Exception):
    pass
class ReadSavedMessagesIdsFailed(Exception):
    pass
class CheckIfUserGotBadgeFailed(Exception):
    pass
class SendPrivateMessageFailed(Exception):
    pass
def Check_cookie(yourCookie,showErrors=bool):
    ##try:
        #req.urlopen('http://google.com')
    #except:
        #print("No internet connection, quiting.")
        #exit(-1)
    try:
        socket.create_connection(('google.com',80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    s = requests.Session()
    re = s.get("https://users.roblox.com/v1/users/authenticated",
               headers={"Accept": "application/json", "cookie": f".ROBLOSECURITY={yourCookie};"},
               cookies={".ROBLOSECURITY": f's.cookies[".ROBLOSECURITY"]'})
    try:
        if re.json()['name']:
            return True
        else:
            return False
    except:
        return False

def Get_Robux(cookie,showErrors = bool):
    #try:
        #req.urlopen('http://google.com')
    #except:
        #print("No internet connection, quiting.")
        #exit(-1)
    try:
        socket.create_connection(('google.com',80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    try:
        a = requests.get(f"https://economy.roblox.com/v1/user/currency",headers={"Accept":"application/json","cookie":f".ROBLOSECURITY={cookie};"},cookies={".ROBLOSECURITY":f'{cookie}'})
        if 'errors' in a.json():
            if showErrors == True:
                raise APIError(f"{a.json()['errors'][0]['message']} Response: {a.status_code} fix: You must put your userId and not someone's else or login to your account first or check your cookie..")
            else:
                return
        else:
            return a.json()['robux']

    except Exception as RE:
        if showErrors == True:
            raise RobuxCheckFailed(f"Robux check process returned Exception: {RE}")
        else:
            return
def init(Help=bool,cookie=str,showErrors = bool):
    print("This feature is coming soon, check the change log (__Changes__.py)")

    """
    try:
        socket.create_connection(('google.com',80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    if Help == True:
        print("Return: User Description from cookie, User Id from cookie, Username from cookie, Display name from cookie,\n")
        print("Isbanned from cookie, Robux value from cookie.\n")
        print(f
Usage: 
    init(Help=false,cookie=your .ROBLOSECURITY cookie)
    {Fore.YELLOW}IMPORTANT: Turn off 'Help' argument.
    {Fore.RED}Output:
        {Fore.BLUE}Description, User Id, Username, Display name, Is banned, robux:
        
        {Fore.LIGHTBLUE_EX}Hi, This is user description, 123456789, Username123, MyDisplayName, False, 0 {Fore.RESET}   

    elif Help is None:
        return
"""
def Get_Authentication_ticket(cookie,gameid,showErrors=bool):
    try:
        socket.create_connection(('google.com',80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    API = requests.post("https://auth.roblox.com/v1/authentication-ticket/",headers={"Accept": "application/json","x-csrf-token":Get_x_csrf_token(cookie=cookie,showErrors=showErrors),"referer":f"https://www.roblox.com/games/{gameid}","cookie":f".ROBLOSECURITY={cookie}"})
    if "rbx-authentication-ticket" in API.headers:
        return API.headers["rbx-authentication-ticket"]
    else:
        if showErrors == True:
            raise AuthTicketException("Failed to find 'rbx-authentication-ticket' in the headers.")
        else:
            return
def Check_User(UID,showErrors=bool):
    try:
        socket.create_connection(('google.com',80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    try:
        a = requests.get(f"https://users.roblox.com/v1/users/{UID}")
        if a.json()["description"] and a.json()["isBanned"] == False and a.json()["name"] and a.json()["displayName"] and a.json()["id"]:
            return True
        else:
            return False
    except:
        return False

def IsBanned(UID,showErrors=bool):
    try:
        socket.create_connection(('google.com',80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    try:

        a = requests.get(f"https://users.roblox.com/v1/users/{UID}")
        if "isBanned" in a.json():
            if a.json()['isBanned'] == False:
                return False
            elif a.json()['isBanned'] == True:
                return True
        else:
            return True
    except Exception as B:
        if showErrors == True:
            raise CheckIsBannedFailed("Check if banned process returned Exception: ",B)
        else:
            return
def Get_Authentication_Info(cookie,showErrors=bool):
    s = requests.Session() #Useless session....
    s.cookies['.ROBLOSECURITY'] = cookie
    #try:
        #req.urlopen('http://google.com')
    #except:
        #print("No internet connection, quiting.")
        #exit(-1)
    try:
        socket.create_connection(('google.com',80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    Auth = s.get("https://users.roblox.com/v1/users/authenticated",headers={"Accept":"application/json","cookie":f".ROBLOSECURITY={cookie};"},cookies={".ROBLOSECURITY":f'{cookie}'}).json()
    if 'errors' in Auth:
        if showErrors == True:
            raise AuthenticationError("The user is not authenticated. Check your cookie, the cookie must be the cookie that you're using.")
        else:
            return
    else:
        return Auth

def Get_x_csrf_token(cookie,showErrors=bool):
    try:
        try:
            socket.create_connection(('google.com', 80))
        except socket.gaierror:
            if showErrors == True:
                raise APIConnectFailed("No internet connection, check your internet connection and try again.")
            else:
                return
        #try:
            #req.urlopen('http://google.com')
        #except:
            #print("No internet connection, quiting.")
            #exit(-1)
        xsrfRequest = requests.post("https://auth.roblox.com/v2/logout",
                                    cookies={".ROBLOSECURITY": cookie})
        if xsrfRequest.headers:

            if xsrfRequest.headers.get("x-csrf-token") == None:
                if showErrors == True:
                    raise InvalidCookie("Invalid .ROBLOSECURITY cookie, are you sure you're using your current cookie ?")
                else:
                    return
            else:
                return xsrfRequest.headers["x-csrf-token"]
        else:
            if showErrors == True:
                raise NoHeadersError("The API didn't return any response headers. Check your internet connection.")
            else:
                return


            #else:
                #APIError("The request returned no result headers, Response: ",xsrfRequest.status_code)
            #print(xsrfRequest.headers["x-csrf-token"],xsrfRequest.headers)

    except Exception as e:
        raise GetTokenException(f"'Get x-csrf-token' process returned an Exception: {e}'")
def get_Auth_Metadata(cookie,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    try:
        API = requests.get('https://auth.roblox.com/v2/auth/metadata',
            headers=
            {
                "Accept":"application/json",
                "cookie":f"ROBLOSECURITY={cookie}"
            },
            cookies =
            {
                ".ROBLOSECURITY":cookie,

            },
            timeout=15
        )

        if 'errors' in API.json():
            if showErrors == True:
                raise GetMetadataFailed(f"Respond data returned an error, make sure the password is correct and the email is correct, error: {API.json()['errors'][0]['message']}")
            else:
                return
        else:
            return API.json()
    except Exception as error:
        if showErrors == True:
            raise APIError(f"'get_Auth_Metadata' process returned an exception: {error}")
        else:
            return
def SetEmail(cookie,email,password,x_csrf_token,Skipverification=bool,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    try:
        API = requests.post('https://accountsettings.roblox.com/v1/email',
            data=
            {
                'password': password,
                "emailAddress":email,
                "SkipVerificationEmail":Skipverification,
            },
            headers=
            {
                "Accept":"application/json",
                "x-csrf-token":x_csrf_token,
            },
            cookies =
            {
                ".ROBLOSECURITY":cookie,

            },
            timeout=15
        )

        if 'errors' in API.json():
            if showErrors == True:
                raise EmailVerificationFailed(f"Respond data returned an error, make sure that the email is correct, error: {API.json()['errors'][0]['message']}")
            else:
                return
        if Skipverification == False:
            #print(f"Email verification request sent to {email}")
            return API.status_code
        else:
            return API.status_code
    except Exception as error:
        if showErrors == True:
            raise APIPostError(f"'ChangeEmail' process returned an exception: {error}")
        else:
            return

def SendPrivateMessage(cookie,UserId,x_csrf_token,subject=str,body=str,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    try:
        API = requests.post('https://privatemessages.roblox.com/v1/messages/send',data={"userId":UserId,"subject":subject,"body":body,'recipientId':UserId,'includePreviousMessage':True},headers={"Accept": "application/json","x-csrf-token": x_csrf_token},cookies={".ROBLOSECURITY": cookie})
        if 'errors' in API.json():
            if showErrors == True:
                raise SendPrivateMessageFailed(f"{API.json()['errors'][0]['message']}")
            else:
                return
        elif 'success' in API.json():
            if API.json()['success'] == False:
                if showErrors == True:
                    raise SendPrivateMessageFailed(f'{API.json()["shortMessage"]}: {API.json()["message"]}')
                else:
                    return
            elif API.json()["success"] == True:
                return API.status_code
    except Exception as Error:
        if showErrors == True:
            raise APIPostError(f"'SendPrivateMessage' process returned an exception: {Error}")
        else:
            return

def VerifyEmail(cookie,email,password,x_csrf_token,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        elif showErrors == False:
            return
    try:
        API = requests.post('https://accountsettings.roblox.com/v1/email',
            data=
            {
                "emailAddress":email,
                'password':password,
                "SkipVerificationEmail":True,
            },
            headers=
            {
                "Accept":"application/json",
                "x-csrf-token":x_csrf_token,
            },
            cookies =
            {
                ".ROBLOSECURITY":cookie,

            },
            timeout=15
        )

        if 'errors' in API.json():
            if showErrors == True:
                 raise EmailVerificationFailed(f"Respond data returned an error, make sure the password is correct and the email is correct, error: {API.json()['errors'][0]['message']}")
            elif showErrors == False:
                return 
        if API.status_code == 200:
            #print(f"Email verification request sent to {email}")
            return API.status_code
    except Exception as error:
        raise APIPostError(f"'ChangeEmail' process returned an exception: {error}")

def GetUserId(cookie,showErrors=bool):
    Info = Get_Authentication_Info(cookie,showErrors=False)
    if Info:
        return Info['id']
    else:
        if showErrors == True:
            raise AccountCheckError("'GetUserId' process returned no user Id, check for authentication using Get_Authentication_Info(cookie) ")
        else:
            return

def GetUsername(cookie,showErrors=bool):
    Info = Get_Authentication_Info(cookie,showErrors=False)
    if Info:
        return Info['name']
    else:
        if showErrors == True:
            raise GetUserNameFailed("'GetUsername' process returned no username, check for authentication using Get_Authentication_Info(cookie) ")
        else:
            return

def GetDisplayName(cookie,showErrors=bool):
    Info = Get_Authentication_Info(cookie,showErrors=False)
    if Info:
        return Info['displayName']
    else:
        if showErrors == True:
            raise GetDisplayNameFailed("'GetDisplayName' process returned no user DisplayName, check for authentication using Get_Authentication_Info(cookie) ")
        else:
            return
def GetRandomUsername(cookie=None,Characters=list,CharWeight=int,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    try:

        randomUserTable = []
        if Characters is not None or Characters != None:
            randomUserTable = random.choices(Characters,k=CharWeight)
        else:
            randomUserTable = random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',k=CharWeight)
            print(randomUserTable)
        randomUser = ""
        for child in randomUserTable:
            randomUser += child
        print(randomUser)
        API = requests.get(f'https://api.roblox.com/users/get-by-username?username={randomUser}',
            headers=
            {
                "Accept":"application/json",
                "cookie":f"ROBLOSECURITY={cookie}"
            },
            cookies =
            {
                ".ROBLOSECURITY":cookie,

            },
            timeout=15
        )

        if 'errors' in API.json():
            randomUserTable2 = []
            if Characters is not None or Characters != None:
                randomUserTable2 = random.choices(Characters, k=CharWeight)
            else:
                randomUserTable2 = random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
                                                     k=CharWeight)
                print(randomUserTable2)
            randomUser2 = ""
            for child2 in randomUserTable:
                randomUser2 += child2
            return randomUser2
        else:
            return API.json()
    except Exception as error:
        if showErrors == True:
            raise APIError(f"'GetRandomUsername' process returned an exception: {error}")
        else:
            return
def Get_UserId_From_Username(cookie,Username,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    try:

        API = requests.get(f'https://api.roblox.com/users/get-by-username?username={Username.lower()}',
            headers=
            {
                "Accept":"application/json",
                "cookie":f"ROBLOSECURITY={cookie}"
            },
            cookies =
            {
                ".ROBLOSECURITY":cookie,

            },
            timeout=15
        )

        if 'errors' in API.json():
            if showErrors == True:

                raise APIError(f"An error while finding a username, make sure username {Username} is valid, Exception: {API.json()['errors'][0]['message']}")
            else:
                return
        else:

            return API.json()["Id"]
    except Exception as error:
        if showErrors == True:
            raise APIError(f"'GetUserIdFromUsername' process returned an exception: {error}")
        else:
            return

def Get_ConversationId(cookie,User,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    result = None
    guc = requests.get('https://chat.roblox.com/v2/get-user-conversations?pageNumber=1&pageSize=10',cookies={".ROBLOSECURITY":cookie})
    for i in range(200):
        try:
            a = guc.json()[i]
            if a:
                if 'title' in a:
                    if str(a['participants'][0]['name']).lower() == str(User).lower():
                         result = a['id']

        except IndexError:
            break
    if result != None:
        return result
    else:
        if showErrors == True:
            raise GetConversationError(f"Failed to get ConversationId, check if '{User}' is your friend in roblox.")
        else:
            return

def Send_Message(cookie,ConversationId,message,x_csrf_token,save_messageId_to_file,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    Post = requests.post("https://chat.roblox.com/v2/send-message",cookies={".ROBLOSECURITY":cookie},headers={"Accept":"application/json","x-csrf-token":x_csrf_token},data={'conversationId': ConversationId, 'message': message},timeout=15)
    if "messageId" in Post.json() and save_messageId_to_file == True:

        with open("SavedMessageId.txt",'a') as saved:
            saved.write(f"{Post.json()['messageId']} {Post.json()['content']} \n")
            return Post.json()["messageId"], Post.json()['content']
    elif "messageId" in Post.json() and save_messageId_to_file == False:
        return Post.json()["messageId"], Post.json()['content']
    elif "errors" in Post.json():
        if showErrors == True:
            raise SendMessageFailed("Send message failed, check if conversationId is valid. Error message: ",Post.json()['errors'][0]['message'])
        else:
            return
    else:
        if showErrors == True:
            raise APIPostError(f"Method Post has failed in API: {Post.url}. Response: {Post.status_code} Data returned: {Post.json()}")
        else:
            return

def Get_Saved_MessageId_By_Message(message,PathToFile,showErrors=bool):
    results = []
    try:
        with open(PathToFile,'r') as Saved:
            for line in Saved.readlines():
                if line.split()[1] == message:
                    results.append(line.split()[0])
                else:
                    continue
    except Exception as error:
        if showErrors == True:
            raise ReadSavedMessagesIdsFailed(f"The read process returned an Exception, check if '{PathToFile}' exist, error: {error}")
        else:
            return
    return results

def Get_All_User_Badges(AnyUserId,cookie,showErrors=bool):
    Results = []
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors== True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    try:
        API = requests.get(f'https://accountinformation.roblox.com/v1/users/{AnyUserId}/roblox-badges',headers={"Accept":"application/json"},cookies={".ROBLOSECURITY":cookie})
        if 'errors' in API:
            if showErrors == True:
                raise GetAllUserBadgesFailed(f"'Get All user Badges' process returned Exception, check if UserId: {AnyUserId} is vaild and not banned.")
            else:
                return
        for i in range(200):
            try:
                if API.json()[i]:
                    Results.append(API.json()[i]['name'])
                else:
                    continue
            except IndexError:
                break
        return Results
    except Exception as error:
        if showErrors == True:
            raise APIError(f"'Get All user Badges' process returned Exception, Error: {error}")
        else:
            return

def Find_User_Badge(AnyUserId,cookie,BadgeId=int,showErrors=bool):
    Results = None
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    API = requests.get(f'https://accountinformation.roblox.com/v1/users/{AnyUserId}/roblox-badges',headers={"Accept":"application/json"},cookies={".ROBLOSECURITY":cookie})
    if 'errors' in API:
        if showErrors == True:
            raise FindUserBadgeFailed(
                f"'Get All user Badges' process returned Exception, check if UserId: {AnyUserId} is vaild and not banned.")
        else:
            return
    try:
        for i in range(2003333):
            try:
                if API.json()[i] and API.json()[i]['id'] == BadgeId:
                    Results = API.json()[i]['name']
                    return Results
                else:
                    continue
            except IndexError:
                break
    except Exception as error:
        if showErrors ==True:
            raise APIError(f"'Find user Badge' process returned Exception, Error: {error}")
        else:
            return

def CheckIf_User_Has_badge(AnyUserId,cookie,BadgeId=int,showErrors=bool):
    Results = None
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    API = requests.get(f'https://accountinformation.roblox.com/v1/users/{AnyUserId}/roblox-badges',headers={"Accept":"application/json"},cookies={".ROBLOSECURITY":cookie})
    if 'errors' in API:
        if showErrors == True:
            raise CheckIfUserGotBadgeFailed(
                f"'Get All user Badges' process returned Exception, check if UserId: {AnyUserId} is vaild and not banned.")
        else:
            return
    try:
        for i in range(2003333):
            try:
                if API.json()[i] and API.json()[i]['id'] == BadgeId:

                    return True
                else:
                    continue
            except IndexError:
                return False
    except Exception as error:
        if showErrors == True:
            raise APIError(f"'Badge check' process returned Exception, Error: {error}")
        else:
            return

def Use_StarCode(cookie,x_csrf_token,starcode,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    try:
        API = requests.post("https://accountinformation.roblox.com/v1/star-code-affiliates",data={
            "code":starcode,
        },headers={
            "Accept": "application/json",
            'x-csrf-token': x_csrf_token,
        }, cookies={
            ".ROBLOSECURITY": cookie
        })
        if 'errors' in API.json() and API.json()['errors'][0]['message'] == "Token Validation Failed":
            if showErrors == True:
                raise TokenValidationFailed(
                    f"Invalid x-csrf-token: {x_csrf_token}, Use RobloxPyApi3.Remove_Starcode(your.ROBLOSECURITY,RobloxPyApi3.Get_x_csrf_token(your.ROBLOSECURITY)).")
            else:
                return
        elif 'errors' in API.json() and API.json()['errors'][0]['message'] != "Token Validation Failed":
            if showErrors == True:
                raise APIPostError(
                    f"Method Post has failed in API: {API.url}. Response: {API.status_code} reason: {API.json()['errors'][0]['message']}")
            else:
                return
        else:
            return API.status_code
    except Exception as error:
        raise RemoveStarCodeFailed(f"'Use_Starcode' process returned an Exception: {error}")


def Remove_Starcode(cookie,x_csrf_token,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    try:
        API = requests.delete("https://accountinformation.roblox.com/v1/star-code-affiliates",headers={
            "Accept":"application/json",
            'x-csrf-token':x_csrf_token
        },cookies={
            ".ROBLOSECURITY":cookie
        })
        if 'errors' in API.json() and API.json()['errors'][0]['message'] == "Token Validation Failed":
            if showErrors == True:

                raise TokenValidationFailed(f"Invalid x-csrf-token: {x_csrf_token}, Use RobloxPyApi3.Remove_Starcode(your.ROBLOSECURITY,RobloxPyApi3.Get_x_csrf_token(your.ROBLOSECURITY)).")
            else:
                return
        elif 'errors' in API.json() and API.json()['errors'][0]['message'] != "Token Validation Failed":
            if showErrors == True:
                raise APIDeleteError(f"Method Post has failed in API: {API.url}. Response: {API.status_code} reason: {API.json()['errors'][0]['message']}")
            else:
                return
        else:
            return API.status_code
    except Exception as error:
        if showErrors == True:
            raise RemoveStarCodeFailed(f"'Remove_Starcode' process returned an Exception: {error}")
        else:
            return

def Set_Description(cookie,x_csrf_token,Description,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    try:
        API = requests.post("https://accountinformation.roblox.com/v1/description", data={
            "description":Description,
        }, headers={
            "Accept": "application/json",
            'x-csrf-token': x_csrf_token,
        }, cookies={
            ".ROBLOSECURITY": cookie
        },timeout=15)

        if 'errors' in API.json() and API.json()['errors'][0]['message'] == "Token Validation Failed":
            if showErrors == True:
                raise TokenValidationFailed(
                    f"Invalid x-csrf-token: {x_csrf_token}, Use RobloxPyApi3.Remove_Starcode(your.ROBLOSECURITY,RobloxPyApi3.Get_x_csrf_token(your.ROBLOSECURITY)).")
            else:
                return
        elif 'errors' in API.json() and API.json()['errors'][0]['message'] != "Token Validation Failed":
            if showErrors == True:
                raise APIPostError(
                    f"Method Post has failed in API: {API.url}. Response: {API.status_code} reason: {API.json()['errors'][0]['message']}")
        else:
            return API.status_code
    except Exception as error:
        if showErrors == True:
            raise ChangeDescriptionFailed(f"'Set_Description' process returned an Exception: {error}")
        else:
            return

def Remove_Description(cookie,x_csrf_token,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        elif showErrors == False:
            return
    try:
        API = requests.post("https://accountinformation.roblox.com/v1/description", data={
            "description":"",
        }, headers={
            "Accept": "application/json",
            'x-csrf-token': x_csrf_token,
        }, cookies={
            ".ROBLOSECURITY": cookie
        })

        if 'errors' in API.json() and API.json()['errors'][0]['message'] == "Token Validation Failed":
            if showErrors == True:
                raise TokenValidationFailed(
                    f"Invalid x-csrf-token: {x_csrf_token}, Use RobloxPyApi3.Remove_Starcode(your.ROBLOSECURITY,RobloxPyApi3.Get_x_csrf_token(your.ROBLOSECURITY)).")
        elif 'errors' in API.json() and API.json()['errors'][0]['message'] != "Token Validation Failed":
            if showErrors == True:
                raise APIPostError(
                    f"Method Post has failed in API: {API.url}. Response: {API.status_code} reason: {API.json()['errors'][0]['message']}")

            elif showErrors == False:
                return
        else:
            return API.status_code
    except Exception as error:
        if showErrors == True:
            raise ChangeDescriptionFailed(f"'Set_Description' process returned an Exception: {error}")
        elif showErrors == False:
            return


class bot:


    def __init__(self,cookie,showErrors=bool):
        self.__Author__ = Version.__Author__

        self.__PythonVersion__ = Version.__PythonVersion__
        self.__ProgrammingLanguage__ = Version.__ProgrammingLanguage__
        self.__FileName__ = "__init__.py"
        self.__Version__ = Version.__PackageVersion__
        self. __Copyright__ = Version.__Copyright__
        self. __Package__ = Version.__Package__
        self.__GitHubUsername__ = Version.__GitHubUsername__
        self.__GitHubPage__ = Version.__GitHubPage__
        self.__GitHub__ = Version.__GitHub__
        self. __moduleName__ = Version.__moduleName__
        self. __RobloxUserName__ = Version.__RobloxUserName__
        self. __RobloxProfile__ = Version.__RobloxUserId__
        self. __RobloxUserId__ = Version.__RobloxUserName__
        self.__RobloxPackages__ = ['RoPy', 'RobloxApi3', 'RobloxPyApi3', 'Pyblox', 'roblox.py']
        self.ROBLOSECURITY = cookie
        self.Robux = Get_Robux(self.ROBLOSECURITY)
        self.Id = GetUserId(self.ROBLOSECURITY)
        self.UserId = GetUserId(self.ROBLOSECURITY)
        self.Name = GetUsername(cookie)
        self.Username = GetUsername(cookie)
        self.DisplayName = GetDisplayName(cookie)
        self.IsBanned = IsBanned(self.Id)
        self.x_csrf_token = Get_x_csrf_token(self.ROBLOSECURITY)
        self.showErrors = showErrors
    def Get_x_csrf_token(self):
        try:
            #try:
                #req.urlopen('google.com')
            #except:
                #print("No internet connection, quiting.")
                #exit(-1)
            try:
                socket.create_connection(('google.com', 80))
            except socket.gaierror:
                raise APIConnectFailed("No internet connection, check your internet connection and try again.")
            xsrfRequest = requests.post("https://auth.roblox.com/v2/logout",
                                        cookies={".ROBLOSECURITY": self.ROBLOSECURITY})
            if xsrfRequest.headers:

                if xsrfRequest.headers.get("x-csrf-token") == None:

                    raise InvalidCookie("Invalid .ROBLOSECURITY cookie, are you sure you're using your current cookie ?")
                else:
                    return xsrfRequest.headers["x-csrf-token"]
            else:

                raise NoHeadersError("The API didn't return any response headers. Check your internet connection.")



            #else:
                #APIError("The request returned no result headers, Response: ",xsrfRequest.status_code)
            #print(xsrfRequest.headers["x-csrf-token"],xsrfRequest.headers)

        except Exception as e:
            raise GetTokenException(f"'Get x-csrf-token' process returned an Exception: {e}'")
    def Check_cookie(self):
        return Check_cookie(self.ROBLOSECURITY,showErrors=self.showErrors)
    def Get_Robux(self):
        return Get_Robux(self.ROBLOSECURITY,showErrors=self.showErrors)
    def Check_User(self,UserId):
        return Check_User(UserId,showErrors=self.showErrors)
    def CheckIfIsBanned(self,UserId):
        return IsBanned(UID=UserId,showErrors=self.showErrors)
    def Get_Authentication_Info(self):
        return Get_Authentication_Info(self.ROBLOSECURITY, showErrors=self.showErrors)
    def get_Auth_Metadata(self):
        return get_Auth_Metadata(self.ROBLOSECURITY,showErrors=self.showErrors)
    def SetEmail(self,TargetEmail,BotPassword,skipverification=bool):
        return SetEmail(cookie=self.ROBLOSECURITY,email=TargetEmail,password=BotPassword,x_csrf_token=Get_x_csrf_token(self.ROBLOSECURITY,showErrors=self.showErrors),Skipverification=skipverification,showErrors=self.showErrors)
    def SendPrivateMessage(self,TargetUserId,subject=str,body=str):
        return SendPrivateMessage(self.ROBLOSECURITY,TargetUserId,Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),subject=subject,body=body,showErrors=self.showErrors)
    def VerifyEmail(self,TargetEmail,BotPassword):
        return VerifyEmail(self.ROBLOSECURITY,email=TargetEmail,password=BotPassword,x_csrf_token=Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),showErrors=self.showErrors)
    def Get_ConversationId(self,FriendUserName):
        return Get_ConversationId(cookie=self.ROBLOSECURITY,User=FriendUserName,showErrors=self.showErrors)
    def Send_Message(self,ConversationId,message,save_messageId_to_file):
        return Send_Message(cookie=self.ROBLOSECURITY,ConversationId=ConversationId,message=message,x_csrf_token=Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),save_messageId_to_file=save_messageId_to_file,showErrors=self.showErrors)
    def Get_Saved_MessageId_By_Message(self,message,PathToFile):
        return Get_Saved_MessageId_By_Message(message,PathToFile,showErrors=self.showErrors)
    def Get_All_User_Badges(self,AnyUserId):
        return Get_All_User_Badges(AnyUserId=AnyUserId,cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
    def Find_User_Badge(self,AnyUserId,BadgeId=int):
        return Find_User_Badge(AnyUserId,cookie=self.ROBLOSECURITY,BadgeId=BadgeId,showErrors=self.showErrors)
    def CheckIf_User_Has_badge(self,AnyUserId,BadgeId=int):
        return CheckIf_User_Has_badge(AnyUserId=AnyUserId,cookie=self.ROBLOSECURITY,BadgeId=BadgeId,showErrors=self.showErrors)
    def Use_StarCode(self,starcode):
        return Use_StarCode(cookie=self.ROBLOSECURITY, x_csrf_token=Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors), starcode=starcode, showErrors=self.showErrors)
    def Remove_Starcode(self):
        return Remove_Starcode(cookie=self.ROBLOSECURITY, x_csrf_token=Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors), showErrors=self.showErrors)
    def Set_Description(self,Description):
        return Set_Description(cookie=self.ROBLOSECURITY, x_csrf_token=Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors), Description=Description, showErrors=self.showErrors)
    def Remove_Description(self):
        return Remove_Description(cookie=self.ROBLOSECURITY,x_csrf_token=Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),showErrors=self.showErrors)
    def list_bundles_from_assetId(self,assetId):
        return list_bundles_from_assetId(cookie=self.ROBLOSECURITY,assetId=assetId,showErrors=self.showErrors)
    def Get_Bundle_Details(self,bundleId):
        return Get_Bundle_Details(cookie=self.ROBLOSECURITY, bundleId=bundleId, showErrors=self.showErrors)
    def Get_BundleName_From_BundleId(self,bundleId):
        return Get_BundleName_From_BundleId(cookie=self.ROBLOSECURITY, bundleId=bundleId, showErrors=self.showErrors)
    def Get_Items_From_Bundle(self,bundleId):
        return Get_Items_From_Bundle(cookie=self.ROBLOSECURITY, bundleId=bundleId, showErrors=self.showErrors)
    def Find_Item_In_Bundle(self,bundleId,AssetId):
        return Find_Item_In_Bundle(cookie=self.ROBLOSECURITY, bundleId=bundleId,AssetId=AssetId, showErrors=self.showErrors)
    def CheckIf_Item_In_Bundle_IsOwned(self,bundleId,AssetId):
        return CheckIf_Item_In_Bundle_IsOwned(cookie=self.ROBLOSECURITY, bundleId=bundleId,AssetId=AssetId, showErrors=self.showErrors)
    def CheckIf_Item_In_Bundle(self,bundleId,AssetId):
        return CheckIf_Item_In_Bundle(cookie=self.ROBLOSECURITY, bundleId=bundleId, AssetId=AssetId,showErrors=self.showErrors)
    def Get_Bundle_Recommendation(self,bundleId):
        return Get_Bundle_Recommendation(cookie=self.ROBLOSECURITY, bundleId=bundleId, showErrors=self.showErrors)
    def Find_Bundle_in_Bundle_Recommendation(self,bundleId,AssetId,TargetBundleId):
        return Find_Bundle_in_Bundle_Recommendation(cookie=self.ROBLOSECURITY, bundleId=bundleId,TargetBundleId=TargetBundleId,AssetId=AssetId,showErrors=self.showErrors)
    def Get_Bundles_Names_owned_by_Player(self,UserId):
        return Get_Bundles_Names_owned_by_Player(cookie=self.ROBLOSECURITY,UserId=UserId,showErrors=self.showErrors)
    def Get_Bundles_Ids_owned_by_Player(self,UserId):
        return Get_Bundles_Ids_owned_by_Player(cookie=self.ROBLOSECURITY, UserId=UserId, showErrors=self.showErrors)
    def Unpack_Bundle(self,bundleId):
        return Unpack_Bundle(cookie=self,x_csrf_token=Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),bundleId=bundleId,showErrors=self.showErrors)
    def Get_asset_To_Category(self):
        return Get_asset_To_Category(cookie=self.ROBLOSECURITY, showErrors=self.showErrors)
    def Asset_To_Subcategory(self):
        return Asset_To_Subcategory(cookie=self.ROBLOSECURITY, showErrors=self.showErrors)
    def Get_Categories(self):
        return Get_Categories(cookie=self.ROBLOSECURITY, showErrors=self.showErrors)
    def Get_subcategories(self):
        return Get_subcategories(cookie=self.ROBLOSECURITY, showErrors=self.showErrors)
    def Get_Asset_Favorites_Count(self,AssetId):
        return Get_Asset_Favorites_Count(cookie=self.ROBLOSECURITY,AssetId=AssetId,showErrors=self.showErrors)
    def Get_Bundle_Favorites_Count(self,bundleId):
        return Get_Bundle_Favorites_Count(cookie=self.ROBLOSECURITY,bundleId=bundleId,showErrors=self.showErrors)
    def Get_Favorite_Asset(self,AssetId,UserId):
        return Get_Favorite_Asset(cookie=self.ROBLOSECURITY,AssetId=AssetId,UserId=UserId,showErrors=self.showErrors)
    def Delete_Favorite_Asset(self,AssetId):
        return Delete_Favorite_Asset(cookie=self.ROBLOSECURITY,x_csrf_token=Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),AssetId=AssetId,YourUserId=self.UserId,showErrors=self.showErrors)
    def UnFavorite_Asset(self,AssetId):
        return UnFavorite_Asset(cookie=self.ROBLOSECURITY,x_csrf_token=Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),AssetId=AssetId,YourUserId=self.UserId,showErrors=self.showErrors)
    def Create_Favorite_Asset(self,AssetId):
        return Create_Favorite_Asset(cookie=self.ROBLOSECURITY,x_csrf_token=Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),AssetId=AssetId,YourUserId=self.UserId,showErrors=self.showErrors)
    def Favorite_Asset(self, AssetId):
        return Favorite_Asset(cookie=self.ROBLOSECURITY, x_csrf_token=Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),AssetId=AssetId, YourUserId=self.UserId, showErrors=self.showErrors)
    def Get_Favorite_Bundle(self, bundleId):
        return Get_Favorite_Bundle(cookie=self.ROBLOSECURITY, bundleId=bundleId, YourUserId=self.UserId, showErrors=self.showErrors)
    def Delete_Favorite_Bundle(self,bundleId):
        return Delete_Favorite_Bundle(cookie=self.ROBLOSECURITY,x_csrf_token=Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors), bundleId=bundleId, YourUserId=self.UserId, showErrors=self.showErrors)
    def UnFavorite_Bundle(self,bundleId):
        return UnFavorite_Bundle(cookie=self.ROBLOSECURITY,x_csrf_token=Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors), bundleId=bundleId, YourUserId=self.UserId, showErrors=self.showErrors)
    def Create_Favorite_Bundle(self,bundleId):
        return Create_Favorite_Bundle(cookie=self.ROBLOSECURITY,x_csrf_token=Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors), bundleId=bundleId, YourUserId=self.UserId, showErrors=self.showErrors)
    def Favorite_Bundle(self, bundleId):
        return Favorite_Bundle(cookie=self.ROBLOSECURITY,x_csrf_token=Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors), bundleId=bundleId,YourUserId=self.UserId, showErrors=self.showErrors)
    def Get_Items_Details(self,AssetId):
        return Get_Items_Details(cookie=self.ROBLOSECURITY,x_csrf_token=Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),AssetId=AssetId,showErrors=self.showErrors)
    def Items_Details(self,AssetId):
        return Items_Details(cookie=self.ROBLOSECURITY,x_csrf_token=Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),AssetId=AssetId,showErrors=self.showErrors)
    def JoinGame(self,gameid):
        return JoinGame(cookie=self.ROBLOSECURITY,gameId=gameid,showErrors=self.showErrors)
    def LeaveGame(self):
        return LeaveGame(showErrors=self.showErrors)
    def GetAvatarBodyColorsIds(self):
        return GetAvatarBodyColorsIds(cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
    def GetAvatarDetails(self):
        return GetAvatarDetails(cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
    def GetAvatarRigType(self):
        return GetAvatarRigType(cookie=self.ROBLOSECURITY, showErrors=self.showErrors)
    def GetAvatarRigTypeEnum(self):
        return GetAvatarRigTypeEnum(cookie=self.ROBLOSECURITY, showErrors=self.showErrors)
    def GetAvatarScales(self):
        return GetAvatarScales(cookie=self.ROBLOSECURITY, showErrors=self.showErrors)
    def GetAvatar(self):
        return GetAvatar(cookie=self.ROBLOSECURITY, showErrors=self.showErrors)
    def IsWearingDefaultPants(self):
        return IsWearingDefaultPants(cookie=self.ROBLOSECURITY, showErrors=self.showErrors)
    def IsWearingDefaultShirt(self):
        return IsWearingDefaultShirt(cookie=self.ROBLOSECURITY, showErrors=self.showErrors)
    def GetAvatarEmotes(self):
        return GetAvatarEmotes(cookie=self.ROBLOSECURITY, showErrors=self.showErrors)
    def GetAvatarAssets(self):
        return GetAvatarAssets(cookie=self.ROBLOSECURITY, showErrors=self.showErrors)
    def GetAvatarMetadata(self):
        return GetAvatarMetadata(cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
    def GetAvatarRules(self):
        return GetAvatarRules(cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
    def GetAvatarFromUser(self,UserId=int):
        return GetAvatarFromUser(cookie=self.ROBLOSECURITY,UserId=UserId,showErrors=self.showErrors)
    def GetAvatarAssetsFromUser(self,UserId):
        return GetAvatarAssetsFromUser(cookie=self.ROBLOSECURITY, UserId=UserId, showErrors=self.showErrors)
    def GetAvatarEmotesFromUser(self,UserId):
        return GetAvatarEmotesFromUser(cookie=self.ROBLOSECURITY, UserId=UserId, showErrors=self.showErrors)
    def GetAvatarScalesFromUser(self,UserId):
        return GetAvatarScalesFromUser(cookie=self.ROBLOSECURITY, UserId=UserId, showErrors=self.showErrors)
    def GetAvatarBodyColorsFromUser(self,UserId):
        return GetAvatarBodyColorsFromUser(cookie=self.ROBLOSECURITY, UserId=UserId,showErrors=self.showErrors)
    def GetAvatarRigTypeFromUser(self,UserId):
        return GetAvatarRigTypeFromUser(cookie=self.ROBLOSECURITY, UserId=UserId,showErrors=self.showErrors)
    def GetAvatarRigTypeEnumFromUser(self,UserId):
        return GetAvatarRigTypeEnumFromUser(cookie=self.ROBLOSECURITY, UserId=UserId,showErrors=self.showErrors)
    def Accept_Friend_Request(self,UserId):
        return Accept_Friend_Request(cookie=self.ROBLOSECURITY,UserId=UserId,showErrors=self.showErrors)
    def Decline_Friend_Request(self,UserId):
        return Decline_Friend_Request(cookie=self.ROBLOSECURITY,UserId=UserId,showErrors=self.showErrors)
    def Decline_All_Friend_Requests(self):
        return Decline_All_Friend_Requests(cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
