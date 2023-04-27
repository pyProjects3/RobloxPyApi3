import random

import requests
from RobloxPyApi3.Utilities import Delete_Request as __Delete_Request__
from RobloxPyApi3.Utilities import Post_Request as __Post_Request__
from RobloxPyApi3.Utilities import Get_Request as __Get_Request__
from RobloxPyApi3.Enums import MonthsNum as Months
import RobloxPyApi3.Errors as Errors
from RobloxPyApi3.Auth import Gender
from RobloxPyApi3.Enums import Privacy
import warnings
from RobloxPyApi3.Auth import NewDate as Date
class PhoneNumber:
    def __init__(self,CountryCode,Perfix,phone):
        self.CCode: int = CountryCode
        self.perfix: int = Perfix
        self.Phone: int = phone


def SetDescription(session,description,showErrors = True) -> requests.Response:
    try:
        req = __Post_Request__("https://accountinformation.roblox.com/v1/description",
                               session=session,
                               data={
                                   "description":description
                               })
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def SetGender(session,gender:Gender,showErrors = True) -> requests.Response:
    try:
        m = None
        if gender == Gender.Random:
            m = str(random.choice(["male",'female','Unknown']))
        else:
            m = str(gender.value)
        req = __Post_Request__("https://accountinformation.roblox.com/v1/gender",
                               session=session,
                               data={
                                   "gender":m
                               })
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def GetBirthdate(session,showErrors = True) -> requests.Response:

    try:
        req = __Get_Request__("https://accountinformation.roblox.com/v1/birthdate",
                               session=session)
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def SetPhone(session,password,Phone:PhoneNumber,showErrors = True) -> requests.Response:

    try:
        req = __Post_Request__("https://accountinformation.roblox.com/v1/phone",
                               session=session,data=

                                    {
                                        "countryCode": str(Phone.CCode),
                                        "prefix": str(Phone.perfix),
                                        "phone": str(Phone.Phone),
                                        "password": str(password)
                                    }
                                )
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def DeletePhone(session,password,Phone:PhoneNumber,showErrors = True) -> requests.Response:

    try:
        req = __Post_Request__("https://accountinformation.roblox.com/v1/phone/delete",
                               session=session,data=

                                    {
                                        "countryCode": str(Phone.CCode),
                                        "prefix": str(Phone.perfix),
                                        "phone": str(Phone.Phone),
                                        "password": str(password)
                                    }
                                )
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def ResendPhone(session,showErrors = True) -> requests.Response:

    try:
        req = __Post_Request__("https://accountinformation.roblox.com/v1/phone/resend",
                               session=session,data={
                                })
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def VerifyPhone(session,code,showErrors = True) -> requests.Response:

    try:
        req = __Post_Request__("https://accountinformation.roblox.com/v1/phone/verify",
                               session=session,data={
                                    "code":code
                                })
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def Set_Promotion_Channels(session,promotionPrivacy:Privacy,FacebookProfileUrl = None,TwitterProfileUrl = None,YoutubeProfileUrl = None, TwitchProfileUrl = None,GuildedProfileUrl = None,showErrors = True) -> requests.Response:

    try:
        req = __Post_Request__("https://accountinformation.roblox.com/v1/promotion-channels",
                               session=session,data={
                                    "promotionChannelsVisibilityPrivacy":promotionPrivacy.value,
                                    'facebook': FacebookProfileUrl,
                                    'twitter': TwitterProfileUrl,
                                    'youtube': YoutubeProfileUrl,
                                    'twitch': TwitchProfileUrl,
                                    'guilded':GuildedProfileUrl
                                })
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def Get_Xbox_Consecutive_login_days(session,showErrors = True) -> requests.Response:

    try:
        req = __Get_Request__("https://accountinformation.roblox.com/v1/xbox-live/consecutive-login-days",
                               session=session)
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def Get_Metatable(session,showErrors = True) -> requests.Response:

    try:
        req = __Get_Request__("https://accountinformation.roblox.com/v1/metadata",
                               session=session)
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def Get_Verified_Phone(session,showErrors = True) -> requests.Response:

    try:
        req = __Get_Request__("https://accountinformation.roblox.com/v1/phone",
                               session=session)
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def Get_Promotion_Channels(session,showErrors = True) -> requests.Response:

    try:
        req = __Get_Request__("https://accountinformation.roblox.com/v1/promotion-channels",
                               session=session)
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def SetBirthdate(session,Password,NewDate = Date(23,Months.FEBRUARY,1992),showErrors = True) -> requests.Response:
    try:
        req = __Post_Request__("https://accountinformation.roblox.com/v1/birthdate",
                               session=session,
                               data={
                                    "birthMonth": int(NewDate.months),
                                    "birthDay": int(NewDate.day),
                                    "birthYear": int(NewDate.y),
                                    "password": str(Password)
                               })
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def Get_Users_Promotion_Channels(session,UserId,showErrors = True) -> requests.Response:

    try:
        req = __Get_Request__(f"https://accountinformation.roblox.com/v1/users/{UserId}/promotion-channels",
                               session=session)
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def Get_Current_Starcode(session,showErrors = True) -> requests.Response:

    try:
        req = __Get_Request__("https://accountinformation.roblox.com/v1/star-code-affiliates",
                               session=session)
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def Get_User_Badges(session,UserId,showErrors = True) -> requests.Response:

    try:
        req = __Get_Request__(f"https://accountinformation.roblox.com/v1/users/{UserId}/roblox-badges",
                               session=session)
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def GetGender(session,showErrors = True) -> requests.Response:

    try:
        req = __Get_Request__(f"https://accountinformation.roblox.com/v1/gender",
                               session=session)
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def Delete_Starcode(session,showErrors = True) -> requests.Response:

    try:
        req = __Delete_Request__("https://accountinformation.roblox.com/v1/star-code-affiliates",
                               session=session)
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                print(req.json())
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def SetStarcode(session,starcode,showErrors = True) -> requests.Response:
    try:
        req = __Post_Request__("https://accountinformation.roblox.com/v1/star-code-affiliates",
                               session=session,
                               data={
                                   "code":starcode
                               })
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def VerifyEmail(session,ticket,showErrors = True) -> requests.Response:
    try:
        req = __Post_Request__("https://accountinformation.roblox.com/v1/email/verify'",
                               session=session,
                               data={
                                   "ticket":ticket
                               })
        if req.status_code != 200:

            if 'errors' in req.json() and showErrors:
                raise Errors.APIError(f"(response:{req.status_code}) {req.json()['errors'][0]['message']}")

        return req
    except Exception as error:
        if showErrors:
            raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
class AccountInformationSession(object):
    def __init__(self,session,password):
        self.Session = session
        self.Password = password
    def SetDescription(self,Description,showErrors = True) -> requests.Response:
        return SetDescription(session=self.Session,description=Description,showErrors=showErrors)
    def SetGender(self,gender:Gender,showErrors = True) -> requests.Response:
        return SetGender(session=self.Session,gender=gender,showErrors=showErrors)
    def GetBirthDate(self,showErrors = True) -> requests.Response:
        return GetBirthdate(session=self.Session, showErrors=showErrors)
    def GetGender(self,showErrors = True):
        return GetGender(session=self.Session,showErrors = showErrors)
    def SetBirthdate(self,Date:Date,showErrors = True):
        warnings.warn("This function is deprecated. This feature now requires a Challange so it will probably break.")
        return SetBirthdate(session=self.Session,NewDate=Date,Password=self.Password,showErrors=showErrors)
    def Get_Xbox_Consecutive_login_days(self,showErrors = True):
        return Get_Xbox_Consecutive_login_days(session=self.Session,showErrors = showErrors)

    def Get_Metatable(self, showErrors=True):
        return Get_Metatable(session=self.Session,showErrors = showErrors)

    def Get_Verified_Phone(self,showErrors = True):
        return Get_Verified_Phone(session=self.Session,showErrors=showErrors)

    def SetPhone(self,Phone:PhoneNumber,showErrors = True):
        return SetPhone(session=self.Session,password=self.Password,Phone=Phone,showErrors = showErrors)

    def ResendPhone(self,showErrors = True):
        return ResendPhone(session=self.Session,showErrors = showErrors)
    def DeletePhone(self,Phone:PhoneNumber,showErrors=True):
        return DeletePhone(session=self.Session, password=self.Password, Phone=Phone, showErrors=showErrors)
    def VerifyPhone(self,code,showErrors = True):
        return VerifyPhone(session=self.Session, showErrors=showErrors,code=code)

    def Set_Promotion_Channels(self, promotionPrivacy: Privacy, FacebookProfileUrl = None, TwitterProfileUrl = None, YoutubeProfileUrl = None, TwitchProfileUrl = None, GuildedProfileUrl = None, showErrors = True):
        return Set_Promotion_Channels(session=self.Session,promotionPrivacy = promotionPrivacy,FacebookProfileUrl = FacebookProfileUrl,TwitterProfileUrl = TwitterProfileUrl,YoutubeProfileUrl = YoutubeProfileUrl, TwitchProfileUrl = TwitchProfileUrl,GuildedProfileUrl = GuildedProfileUrl,showErrors = showErrors)
    def Get_Promotion_Channels(self,showErrors = True):
        return Get_Promotion_Channels(self.Session,showErrors = showErrors)
    def Get_Users_Promotion_Channels(self,UserId:int,showErrors = True):
        return Get_Users_Promotion_Channels(session=self.Session,UserId=UserId,showErrors=showErrors)
    def Get_Current_Starcode(self,showErrors = True):
        return Get_Current_Starcode(session=self.Session,showErrors = showErrors)
    def SetStarcode(self,starcode,showErrors = True):
        return SetStarcode(session=self.Session, starcode=starcode, showErrors=showErrors)
    def Delete_Starcode(self,showErrors = True):
        return Delete_Starcode(session=self.Session,showErrors=showErrors)
    def Get_User_Badges(self,UserId,showErrors = True):
        return Get_User_Badges(session=self.Session,UserId=UserId,showErrors = showErrors)
    def VerifyEmail(self,ticket,showErrors = True):
        return VerifyEmail(session=self.Session, ticket=ticket, showErrors=showErrors)