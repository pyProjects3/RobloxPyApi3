from RobloxPyApi3.Version import *
import RobloxPyApi3
import socket
import requests
def Get_Robux2(cookie,showErrors = bool):
    #try:
        #req.urlopen('http://google.com')
    #except:
        #print("No internet connection, quiting.")
        #exit(-1)
    try:
        socket.create_connection(('google.com',80))
    except socket.gaierror:
        if showErrors == True:
            raise RobloxPyApi3.APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    try:
        a = requests.get(f"https://economy.roblox.com/v1/user/currency",headers={"Accept":"application/json","cookie":f".ROBLOSECURITY={cookie};"},cookies={".ROBLOSECURITY":f'{cookie}'})
        if 'errors' in a.json():
            if showErrors == True:
                raise RobloxPyApi3.APIError(f"{a.json()['errors'][0]['message']} Response: {a.status_code} fix: You must put your userId and not someone's else or login to your account first or check your cookie..")
            else:
                return
        else:
            return a.json()['robux']

    except Exception as RE:
        if showErrors == True:
            raise RobloxPyApi3.RobuxCheckFailed(f"Robux check process returned Exception: {RE}")
        else:
            return
 #AuthorName,Author,PythonVersion,ProgrammingLanguage,PVersion,Copyright,Package,GitHubUsername,GitHubPage,GitHub,moduleName
class Client:
    def __init__(self,cookie,showErrors=bool):
        self.__Author__ = RobloxPyApi3.__Author__

        self.__PythonVersion__ = RobloxPyApi3.__PythonVersion__
        self.__ProgrammingLanguage__ = RobloxPyApi3.__ProgrammingLanguage__
        self.__FileName__ = "__init__.py"
        self.__Version__ = RobloxPyApi3.Version
        self.__Copyright__ = RobloxPyApi3.__Copyright__
        self.__Package__ = RobloxPyApi3.__Package__
        self.__GitHubUsername__ = RobloxPyApi3.__GitHubUsername__
        self.__GitHubPage__ = RobloxPyApi3.__GitHubPage__
        self.__GitHub__ = RobloxPyApi3.__GitHub__
        self.__moduleName__ = RobloxPyApi3.__moduleName__
        self.__RobloxUserName__ = RobloxPyApi3.__RobloxUserName__
        self.__RobloxProfile__ = RobloxPyApi3.__RobloxUserId__
        self.__RobloxUserId__ = RobloxPyApi3.__RobloxUserName__
        self.__RobloxPackages__ = ['RoPy', 'RobloxApi3', 'RobloxPyApi3', 'Pyblox', 'roblox.py']
        self.showErrors = showErrors
        self.ROBLOSECURITY = cookie
        self.Robux = Get_Robux2(cookie = self.ROBLOSECURITY,showErrors=self.showErrors)
        self.Id = RobloxPyApi3.GetUserId(self.ROBLOSECURITY,showErrors=self.showErrors)
        self.UserId = RobloxPyApi3.GetUserId(self.ROBLOSECURITY,showErrors=self.showErrors)
        self.Name = RobloxPyApi3.GetUsername(cookie,showErrors=self.showErrors)
        self.Username = RobloxPyApi3.GetUsername(cookie,showErrors=self.showErrors)
        self.DisplayName = RobloxPyApi3.GetDisplayName(cookie,showErrors=self.showErrors)
        self.IsBanned = RobloxPyApi3.IsBanned(self.Id,showErrors=self.showErrors)
        self.x_csrf_token = RobloxPyApi3.Get_x_csrf_token(self.ROBLOSECURITY,showErrors=self.showErrors)
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
                raise RobloxPyApi3.APIConnectFailed("No internet connection, check your internet connection and try again.")
            xsrfRequest = requests.post("https://auth.roblox.com/v2/logout",
                                        cookies={".ROBLOSECURITY": self.ROBLOSECURITY})
            if xsrfRequest.headers:

                if xsrfRequest.headers.get("x-csrf-token") == None:

                    raise RobloxPyApi3.InvalidCookie("Invalid .ROBLOSECURITY cookie, are you sure you're using your current cookie ?")
                else:
                    return xsrfRequest.headers["x-csrf-token"]
            else:

                raise RobloxPyApi3.NoHeadersError("The API didn't return any response headers. Check your internet connection.")



            #else:
                #APIError("The request returned no result headers, Response: ",xsrfRequest.status_code)
            #print(xsrfRequest.headers["x-csrf-token"],xsrfRequest.headers)

        except Exception as e:
            raise RobloxPyApi3.GetTokenException(f"'Get x-csrf-token' process returned an Exception: {e}'")
    def Check_cookie(self):
        return RobloxPyApi3.Check_cookie(self.ROBLOSECURITY,showErrors=self.showErrors)
    def Get_Robux(self):
        return self.Robux
    def Check_User(self,UserId):
        return RobloxPyApi3.Check_User(UserId,showErrors=self.showErrors)
    def CheckIfIsBanned(self,UserId):
        return RobloxPyApi3.IsBanned(UID=UserId,showErrors=self.showErrors)
    def Get_Authentication_Info(self):
        return RobloxPyApi3.Get_Authentication_Info(self.ROBLOSECURITY, showErrors=self.showErrors)
    def get_Auth_Metadata(self):
        return RobloxPyApi3.get_Auth_Metadata(self.ROBLOSECURITY,showErrors=self.showErrors)
    def SetEmail(self,TargetEmail,BotPassword,skipverification=bool):
        return RobloxPyApi3.SetEmail(cookie=self.ROBLOSECURITY,email=TargetEmail,password=BotPassword,x_csrf_token=RobloxPyApi3.Get_x_csrf_token(self.ROBLOSECURITY,showErrors=self.showErrors),Skipverification=skipverification,showErrors=self.showErrors)
    def SendPrivateMessage(self,TargetUserId,subject=str,body=str):
        return RobloxPyApi3.SendPrivateMessage(self.ROBLOSECURITY,TargetUserId,RobloxPyApi3.Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),subject=subject,body=body,showErrors=self.showErrors)
    def VerifyEmail(self,TargetEmail,BotPassword):
        return RobloxPyApi3.VerifyEmail(self.ROBLOSECURITY,email=TargetEmail,password=BotPassword,x_csrf_token=RobloxPyApi3.Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),showErrors=self.showErrors)
    def Get_ConversationId(self,FriendUserName):
        return RobloxPyApi3.Get_ConversationId(cookie=self.ROBLOSECURITY,User=FriendUserName,showErrors=self.showErrors)
    def Send_Message(self,ConversationId,message,save_messageId_to_file):
        return RobloxPyApi3.Send_Message(cookie=self.ROBLOSECURITY,ConversationId=ConversationId,message=message,x_csrf_token=RobloxPyApi3.Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),save_messageId_to_file=save_messageId_to_file,showErrors=self.showErrors)
    def Get_Saved_MessageId_By_Message(self,message,PathToFile):
        return RobloxPyApi3.Get_Saved_MessageId_By_Message(message,PathToFile,showErrors=self.showErrors)
    def Get_All_User_Badges(self,AnyUserId):
        return RobloxPyApi3.Get_All_User_Badges(AnyUserId=AnyUserId,cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
    def Find_User_Badge(self,AnyUserId,BadgeId=int):
        return RobloxPyApi3.Find_User_Badge(AnyUserId,cookie=self.ROBLOSECURITY,BadgeId=BadgeId,showErrors=self.showErrors)
    def CheckIf_User_Has_badge(self,AnyUserId,BadgeId=int):
        return RobloxPyApi3.CheckIf_User_Has_badge(AnyUserId=AnyUserId,cookie=self.ROBLOSECURITY,BadgeId=BadgeId,showErrors=self.showErrors)
    def Use_StarCode(self,starcode):
        return RobloxPyApi3.Use_StarCode(cookie=self.ROBLOSECURITY, x_csrf_token=RobloxPyApi3.Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors), starcode=starcode, showErrors=self.showErrors)
    def Remove_Starcode(self):
        return RobloxPyApi3.Remove_Starcode(cookie=self.ROBLOSECURITY, x_csrf_token=RobloxPyApi3.Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors), showErrors=self.showErrors)
    def Set_Description(self,Description):
        return RobloxPyApi3.Set_Description(cookie=self.ROBLOSECURITY, x_csrf_token=RobloxPyApi3.Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors), Description=Description, showErrors=self.showErrors)
    def Remove_Description(self):
        return RobloxPyApi3.Remove_Description(cookie=self.ROBLOSECURITY,x_csrf_token=RobloxPyApi3.Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),showErrors=self.showErrors)
    def list_bundles_from_assetId(self,assetId):
        return RobloxPyApi3.list_bundles_from_assetId(cookie=self.ROBLOSECURITY,assetId=assetId,showErrors=self.showErrors)
    def Get_Bundle_Details(self,bundleId):
        return RobloxPyApi3.Get_Bundle_Details(cookie=self.ROBLOSECURITY, bundleId=bundleId, showErrors=self.showErrors)
    def Get_BundleName_From_BundleId(self,bundleId):
        return RobloxPyApi3.Get_BundleName_From_BundleId(cookie=self.ROBLOSECURITY, bundleId=bundleId, showErrors=self.showErrors)
    def Get_Items_From_Bundle(self,bundleId):
        return RobloxPyApi3.Get_Items_From_Bundle(cookie=self.ROBLOSECURITY, bundleId=bundleId, showErrors=self.showErrors)
    def Find_Item_In_Bundle(self,bundleId,AssetId):
        return RobloxPyApi3.Find_Item_In_Bundle(cookie=self.ROBLOSECURITY, bundleId=bundleId,AssetId=AssetId, showErrors=self.showErrors)
    def CheckIf_Item_In_Bundle_IsOwned(self,bundleId,AssetId):
        return RobloxPyApi3.CheckIf_Item_In_Bundle_IsOwned(cookie=self.ROBLOSECURITY, bundleId=bundleId,AssetId=AssetId, showErrors=self.showErrors)
    def CheckIf_Item_In_Bundle(self,bundleId,AssetId):
        return RobloxPyApi3.CheckIf_Item_In_Bundle(cookie=self.ROBLOSECURITY, bundleId=bundleId, AssetId=AssetId,showErrors=self.showErrors)
    def Get_Bundle_Recommendation(self,bundleId):
        return RobloxPyApi3.Get_Bundle_Recommendation(cookie=self.ROBLOSECURITY, bundleId=bundleId, showErrors=self.showErrors)
    def Find_Bundle_in_Bundle_Recommendation(self,bundleId,AssetId,TargetBundleId):
        return RobloxPyApi3.Find_Bundle_in_Bundle_Recommendation(cookie=self.ROBLOSECURITY, bundleId=bundleId,TargetBundleId=TargetBundleId,AssetId=AssetId,showErrors=self.showErrors)
    def Get_Bundles_Names_owned_by_Player(self,UserId):
        return RobloxPyApi3.Get_Bundles_Names_owned_by_Player(cookie=self.ROBLOSECURITY,UserId=UserId,showErrors=self.showErrors)
    def Get_Bundles_Ids_owned_by_Player(self,UserId):
        return RobloxPyApi3.Get_Bundles_Ids_owned_by_Player(cookie=self.ROBLOSECURITY, UserId=UserId, showErrors=self.showErrors)
    def Unpack_Bundle(self,bundleId):
        return RobloxPyApi3.Unpack_Bundle(cookie=self,x_csrf_token=RobloxPyApi3.Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),bundleId=bundleId,showErrors=self.showErrors)
    def Get_asset_To_Category(self):
        return RobloxPyApi3.Get_asset_To_Category(cookie=self.ROBLOSECURITY, showErrors=self.showErrors)
    def Asset_To_Subcategory(self):
        return RobloxPyApi3.Asset_To_Subcategory(cookie=self.ROBLOSECURITY, showErrors=self.showErrors)
    def Get_Categories(self):
        return RobloxPyApi3.Get_Categories(cookie=self.ROBLOSECURITY, showErrors=self.showErrors)
    def Get_subcategories(self):
        return RobloxPyApi3.Get_subcategories(cookie=self.ROBLOSECURITY, showErrors=self.showErrors)
    def Get_Asset_Favorites_Count(self,AssetId):
        return RobloxPyApi3.Get_Asset_Favorites_Count(cookie=self.ROBLOSECURITY,AssetId=AssetId,showErrors=self.showErrors)
    def Get_Bundle_Favorites_Count(self,bundleId):
        return RobloxPyApi3.Get_Bundle_Favorites_Count(cookie=self.ROBLOSECURITY,bundleId=bundleId,showErrors=self.showErrors)
    def Get_Favorite_Asset(self,AssetId,UserId):
        return RobloxPyApi3.Get_Favorite_Asset(cookie=self.ROBLOSECURITY,AssetId=AssetId,UserId=UserId,showErrors=self.showErrors)
    def Delete_Favorite_Asset(self,AssetId):
        return RobloxPyApi3.Delete_Favorite_Asset(cookie=self.ROBLOSECURITY,x_csrf_token=RobloxPyApi3.Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),AssetId=AssetId,YourUserId=self.UserId,showErrors=self.showErrors)
    def UnFavorite_Asset(self,AssetId):
        return RobloxPyApi3.UnFavorite_Asset(cookie=self.ROBLOSECURITY,x_csrf_token=RobloxPyApi3.Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),AssetId=AssetId,YourUserId=self.UserId,showErrors=self.showErrors)
    def Create_Favorite_Asset(self,AssetId):
        return RobloxPyApi3.Create_Favorite_Asset(cookie=self.ROBLOSECURITY,x_csrf_token=RobloxPyApi3.Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),AssetId=AssetId,YourUserId=self.UserId,showErrors=self.showErrors)
    def Favorite_Asset(self, AssetId):
        return RobloxPyApi3.Favorite_Asset(cookie=self.ROBLOSECURITY, x_csrf_token=RobloxPyApi3.Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),AssetId=AssetId, YourUserId=self.UserId, showErrors=self.showErrors)
    def Get_Favorite_Bundle(self, bundleId):
        return RobloxPyApi3.Get_Favorite_Bundle(cookie=self.ROBLOSECURITY, bundleId=bundleId, YourUserId=self.UserId, showErrors=self.showErrors)
    def Delete_Favorite_Bundle(self,bundleId):
        return RobloxPyApi3.Delete_Favorite_Bundle(cookie=self.ROBLOSECURITY,x_csrf_token=RobloxPyApi3.Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors), bundleId=bundleId, YourUserId=self.UserId, showErrors=self.showErrors)
    def UnFavorite_Bundle(self,bundleId):
        return RobloxPyApi3.UnFavorite_Bundle(cookie=self.ROBLOSECURITY,x_csrf_token=RobloxPyApi3.Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors), bundleId=bundleId, YourUserId=self.UserId, showErrors=self.showErrors)
    def Create_Favorite_Bundle(self,bundleId):
        return RobloxPyApi3.Create_Favorite_Bundle(cookie=self.ROBLOSECURITY,x_csrf_token=RobloxPyApi3.Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors), bundleId=bundleId, YourUserId=self.UserId, showErrors=self.showErrors)
    def Favorite_Bundle(self, bundleId):
        return RobloxPyApi3.Favorite_Bundle(cookie=self.ROBLOSECURITY,x_csrf_token=RobloxPyApi3.Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors), bundleId=bundleId,YourUserId=self.UserId, showErrors=self.showErrors)
    def Get_Items_Details(self,AssetId):
        return RobloxPyApi3.Get_Items_Details(cookie=self.ROBLOSECURITY,x_csrf_token=RobloxPyApi3.Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),AssetId=AssetId,showErrors=self.showErrors)
    def Items_Details(self,AssetId):
        return RobloxPyApi3.Items_Details(cookie=self.ROBLOSECURITY,x_csrf_token=RobloxPyApi3.Get_x_csrf_token(cookie=self.ROBLOSECURITY,showErrors=self.showErrors),AssetId=AssetId,showErrors=self.showErrors)
    def JoinGame(self,gameid):
        return RobloxPyApi3.JoinGame(cookie=self.ROBLOSECURITY,gameId=gameid,showErrors=self.showErrors)
    def LeaveGame(self):
        return RobloxPyApi3.LeaveGame(showErrors=self.showErrors)
    def GetAvatarBodyColorsIds(self):
        return RobloxPyApi3.GetAvatarBodyColorsIds(cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
    def GetAvatarDetails(self):
        return RobloxPyApi3.GetAvatarDetails(cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
    def GetAvatarRigType(self):
        return RobloxPyApi3.GetAvatarRigType(cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
    def GetAvatarRigTypeEnum(self):
        return RobloxPyApi3.GetAvatarRigTypeEnum(cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
    def GetAvatarScales(self):
        return RobloxPyApi3.GetAvatarScales(cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
    def GetAvatar(self):
        return RobloxPyApi3.GetAvatar(cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
    def IsWearingDefaultPants(self):
        return RobloxPyApi3.IsWearingDefaultPants(cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
    def IsWearingDefaultShirt(self):
        return RobloxPyApi3.IsWearingDefaultShirt(cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
    def GetAvatarEmotes(self):
        return RobloxPyApi3.GetAvatarEmotes(cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
    def GetAvatarAssets(self):
        return RobloxPyApi3.GetAvatarAssets(cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
    def GetAvatarMetadata(self):
        return RobloxPyApi3.GetAvatarMetadata(cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
    def GetAvatarRules(self):
        return RobloxPyApi3.GetAvatarRules(cookie=self.ROBLOSECURITY,showErrors=self.showErrors)
    def GetAvatarFromUser(self,UserId=int):
        return RobloxPyApi3.GetAvatarFromUser(cookie=self.ROBLOSECURITY,UserId=UserId,showErrors=self.showErrors)
    def GetAvatarAssetsFromUser(self,UserId):
        return RobloxPyApi3.GetAvatarAssetsFromUser(cookie=self.ROBLOSECURITY, UserId=UserId, showErrors=self.showErrors)
    def GetAvatarEmotesFromUser(self,UserId):
        return RobloxPyApi3.GetAvatarEmotesFromUser(cookie=self.ROBLOSECURITY, UserId=UserId, showErrors=self.showErrors)
    def GetAvatarScalesFromUser(self,UserId):
        return RobloxPyApi3.GetAvatarScalesFromUser(cookie=self.ROBLOSECURITY, UserId=UserId, showErrors=self.showErrors)
    def GetAvatarBodyColorsFromUser(self,UserId):
        return RobloxPyApi3.GetAvatarBodyColorsFromUser(cookie=self.ROBLOSECURITY, UserId=UserId,showErrors=self.showErrors)
    def GetAvatarRigTypeFromUser(self,UserId):
        return RobloxPyApi3.GetAvatarRigTypeFromUser(cookie=self.ROBLOSECURITY, UserId=UserId,showErrors=self.showErrors)
    def GetAvatarRigTypeEnumFromUser(self,UserId):
        return RobloxPyApi3.GetAvatarRigTypeEnumFromUser(cookie=self.ROBLOSECURITY, UserId=UserId,showErrors=self.showErrors)
    def Accept_Friend_Request(self,UserId):
        return RobloxPyApi3.Accept_Friend_Request(cookie=self.ROBLOSECURITY,UserId=UserId,showErrors=self.showErrors)
    def Decline_Friend_Request(self,UserId):
        return RobloxPyApi3.Decline_Friend_Request(cookie=self.ROBLOSECURITY,UserId=UserId,showErrors=self.showErrors)
    def Decline_All_Friend_Requests(self):
        return RobloxPyApi3.Decline_All_Friend_Requests(cookie=self.ROBLOSECURITY,showErrors=self.showErrors)