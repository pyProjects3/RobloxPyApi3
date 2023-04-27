import random
from Enums import Months
from Enums import Gender
from Enums import CaptchaMetatable
from Captcha import Captcha,SessionCaptcha
from Enums import MonthsNum
import string
import requests
class Date:
    def __init__(self,day,month,Year):
        self.d: int = day
        self.year: int = Year
        self.month = month.value
class NewDate:
    def __init__(self,Day,month: MonthsNum,year):
        self.y :int = year
        self.day: int = Day
        self.months :int = int(month.value)
class CaptchaType:
    def __init__(self,typeEnum):
        self.t:CaptchaMetatable = typeEnum.value
    def __str__(self) -> str:
        return str(self.t)
WaitForCaptchaNum = 4.5
_Outputting = True
_Debugging = True
def init(CaptchaDelay = 4.5,Output = True,Debug = True):
    global WaitForCaptchaNum
    global _Outputting
    global _Debugging
    WaitForCaptchaNum = CaptchaDelay
    _Outputting = Output
    _Debugging = Debug
def Output(str):
    global _Outputting
    if _Outputting:
        print(str)
def Debug(str):
    global _Debugging
    if _Debugging:
        print(str)
"""
def signup(Username,password,gender,birthday:Date,WaitAfterCaptcha = WaitForCaptchaNum):
    m = 0
    if gender == Gender.male:
        m = 'male'
    elif gender == Gender.female:
        m = "female"
    elif gender == Gender.Random:
        m = random.choice(["female",'male',0])
    elif gender == Gender.Unknown:
        m = 0
    else:
        m = gender
    JSONSignup = {
        "agreementIds": [
            "848d8d8f-0e33-4176-bcd9-aa4e22ae7905",
            "54d8a8f0-d9c8-4cf3-bd26-0cbf8af0bba3"
        ],

        "birthday": f"{birthday.d} {birthday.month} {birthday.year}",
        "context": "MultiverseSignupForm",
        "gender": m,
        "isTosAgreementBoxChecked": True,
        "password": password,
        "username": Username,
        "referralData": None,
        'abTestVariation': 0
    }
    c = Captcha("https://auth.roblox.com/v2/signup", data=JSONSignup,
                Headers={"Accept": "application/json", "x-csrf-token": requests.post(
                    'https://auth.roblox.com/v1/usernames/validate'
                ).headers['x-csrf-token']},WaitAfterComplete=WaitAfterCaptcha)

    def MakePost():
        post = requests.post("https://auth.roblox.com/v2/signup",
                             headers={"Accept": "application/json", "x-csrf-token": requests.post(
                                 'https://auth.roblox.com/v1/usernames/validate'
                             ).headers['x-csrf-token']}, json=JSONSignup)
        return post

    a = MakePost()
    b = a.json()['failureDetails'][0]['fieldData']
    if b:
        print("Captcha is required!")
        td = c.GetDetailsFromFieldData(b)
        f = c.StartSessionFromDetails(td['TokenID'], td['location'], td['id'], td['blob'])
    return f.json(),{"Username":Username,'Password':password}
    #details = c.GetDetails()
    #c.StartSession()
    #print(c.Token, c.ID)
"""

def _retsignupSession(session,Username, password, gender=Gender.Random, birthday=Date(22, Months.JANUARY, 1980),
                  WaitAfterCaptcha=4.5, retry=True):
    Output("Retrying")
    m = 0

    if gender == Gender.male:
        m = 'male'
    elif gender == Gender.female:
        m = "female"
    elif gender == Gender.Random:
        m = random.choice(["female", 'male', 0])
    elif gender == Gender.Unknown:
        m = "Unknown"
    else:
        m = gender
    JSONSignup = {
        "agreementIds": [
            "848d8d8f-0e33-4176-bcd9-aa4e22ae7905",
            "54d8a8f0-d9c8-4cf3-bd26-0cbf8af0bba3"
        ],

        "birthday": f"{birthday.d} {birthday.month} {birthday.year}",
        "context": "MultiverseSignupForm",
        "gender": m,
        "isTosAgreementBoxChecked": True,
        "password": password,
        "username": Username,
        "referralData": None,
        'abTestVariation': 0
    }
    c = SessionCaptcha("https://auth.roblox.com/v2/signup", data=JSONSignup,
                       Headers={"Accept": "application/json", "x-csrf-token": requests.post(
                           'https://auth.roblox.com/v1/usernames/validate'
                       ).headers['x-csrf-token']}, session=session, WaitAfterComplete=WaitAfterCaptcha)

    def MakePost():
        tok = session.post(
            'https://auth.roblox.com/v1/usernames/validate'
        ).headers['x-csrf-token']
        Debug(tok)
        post = session.post("https://auth.roblox.com/v2/signup",
                            headers={"Accept": "application/json", "x-csrf-token": tok}, json=JSONSignup)
        return post

    a = MakePost()
    b = a.json()['failureDetails'][0]['fieldData']
    if b:
        Output("Captcha is required!")
        td = c.GetDetailsFromFieldData(b)
        f = c.StartSessionFromDetails(td['TokenID'], td['location'])
        Debug(f.json())
        if "userId" in f.json():
            # make the authenticated request using the session of the current user
            """
            user_details = session.get(
                f"https://users.roblox.com/v1/users/authenticated/country-code").json()
            print(user_details)
            user_id = user_details['countryCode']
            print(f"New account created successfully. User ID: {user_id}")
            tok2 = session.post(
                'https://auth.roblox.com/v1/usernames/validate'
            ).headers['x-csrf-token']
            print(tok2)
            user_details = session.post(
                f"https://accountinformation.roblox.com/v1/description", data={
                    "description": "Hi, Im auto generated account!!"

                },headers={
                    "Accept":"application/json",
                    "x-csrf-token": tok2
                })
            print(user_details.json())
            print(
                f"Successfully set Account description! response = (Status:{user_details.status_code}) {user_details.json()}")
            """
            Output("Success")
            return session, {"Username": Username, 'Password': password, "UserId": f.json()["userId"],"Birthday":birthday,"Gender":m}
        else:
            if retry:
                s, info = _retsignupSession(session,Username,password,gender,birthday,WaitAfterCaptcha,retry)

                Debug(str('{} {}'.format(s,info)))
                if info["UserId"]:
                    Output("Successfully signed up")
                    return s, info
    # details = c.GetDetails()
    # c.StartSession()
    # print(c.Token, c.ID)
def signupSession(Username,password,gender = Gender.Random,birthday = Date(22,Months.JANUARY,1980),WaitAfterCaptcha = 1.4,retry = True):
    with requests.Session() as session:
        m = 0
        if gender == Gender.male:
            m = 'male'
        elif gender == Gender.female:
            m = "female"
        elif gender == Gender.Random:
            m = random.choice(["female",'male',0])
        elif gender == Gender.Unknown:
            m = "Unknown"
        else:
            m = gender
        JSONSignup = {
            "agreementIds": [
                "848d8d8f-0e33-4176-bcd9-aa4e22ae7905",
                "54d8a8f0-d9c8-4cf3-bd26-0cbf8af0bba3"
            ],

            "birthday": f"{birthday.d} {birthday.month} {birthday.year}",
            "context": "MultiverseSignupForm",
            "gender": m,
            "isTosAgreementBoxChecked": True,
            "password": password,
            "username": Username,
            "referralData": None,
            'abTestVariation': 0
        }
        c = SessionCaptcha("https://auth.roblox.com/v2/signup", data=JSONSignup,
                    Headers={"Accept": "application/json", "x-csrf-token": requests.post(
                        'https://auth.roblox.com/v1/usernames/validate'
                    ).headers['x-csrf-token']},session=session,WaitAfterComplete=WaitAfterCaptcha)

        def MakePost():
            tok =  session.post(
                                     'https://auth.roblox.com/v1/usernames/validate'
                                 ).headers['x-csrf-token']
            Debug(tok)
            post = session.post("https://auth.roblox.com/v2/signup",
                                 headers={"Accept": "application/json", "x-csrf-token":tok}, json=JSONSignup)
            return post

        a = MakePost()
        b = a.json()['failureDetails'][0]['fieldData']
        if b:
            Output("Captcha is required!")
            td = c.GetDetailsFromFieldData(b)
            f = c.StartSessionFromDetails(td['TokenID'], td['location'])
            Debug(f.json())
            if f:
                # make the authenticated request using the session of the current user
                # make the authenticated request using the session of the current user
                """
                user_details = session.get(
                    f"https://users.roblox.com/v1/users/authenticated/country-code").json()
                print(user_details)
                user_id = user_details['countryCode']
                print(f"New account created successfully. User ID: {user_id}")
                
                tok2 = session.post(
                    'https://auth.roblox.com/v1/usernames/validate'
                ).headers['x-csrf-token']
                Debug(tok2)
                user_details = session.post(
                    f"https://accountinformation.roblox.com/v1/description", data={
                        "description": "Hi, Im auto generated account!!"

                    }, headers={
                        "Accept": "application/json",
                        "x-csrf-token": tok2
                    })
                Debug(user_details.json())
                print(
                    f"Successfully set Account description! response = (Status:{user_details.status_code}) {user_details.json()}")
                """
                if "userId" in f.json():
                    Output("Success")
                    return session, {"Username": Username, 'Password': password, "UserId": f.json()["userId"],"Birthday":birthday,"Gender":m}
            else:
                if retry:

                    s, info = _retsignupSession(session,Username,password,gender,birthday,WaitAfterCaptcha,retry)
                    Debug(str('{} {}'.format(s,info)))
                    if info["UserId"]:
                        Output("Successfully signed up")
                        return s, info








def _retloginSession(session, Username, password,
                      WaitAfterCaptcha=4.5, retry=True):
    Output("Retrying")
    JSONLogin = {
        "ctype": "Username",
        "cvalue": str(Username),
        "password": str(password),
    }
    c = SessionCaptcha("https://auth.roblox.com/v2/login", data=JSONLogin,
                       Headers={"Accept": "application/json", "x-csrf-token": requests.post(
                           'https://auth.roblox.com/v1/usernames/validate'
                       ).headers['x-csrf-token']}, session=session, WaitAfterComplete=WaitAfterCaptcha,Type=str(CaptchaType(CaptchaMetatable.WebLogin)))

    def MakePost():
        tok = session.post(
            'https://auth.roblox.com/v1/usernames/validate'
        ).headers['x-csrf-token']
        Debug(tok)
        post = session.post("https://auth.roblox.com/v2/login",
                            headers={"Accept": "application/json", "x-csrf-token": tok}, json=JSONLogin)
        return post

    a = MakePost()
    b = a.json()['errors'][0]['fieldData']
    if b:
        Output("Captcha is required!")
        td = c.GetDetailsFromFieldData2(b)
        f = c.StartSessionFromDetails(td['TokenID'], td['location'])
        Debug(f.json())
        if "user" in f.json():
            # make the authenticated request using the session of the current user
            Output("Success")
            return session, {"Username": Username, 'Password': password, "UserId": f.json()["user"]['id'],"displayName": f.json()["user"]['displayName']}
        else:
            if retry:
                s, info = _retloginSession(session, Username, password, WaitAfterCaptcha, retry)

                Debug(str('{} {}'.format(s, info)))
                if info["user"]:
                    Output("Successfully signed up")
                    return s, info
    # details = c.GetDetails()
    # c.StartSession()
    # print(c.Token, c.ID)


def LoginSession(Username, password,
                  WaitAfterCaptcha=1.4, retry=True):
    with requests.Session() as session:
        JSONLogin = {
            "ctype": "Username",
            "cvalue": str(Username),
            "password": str(password),
        }
        c = SessionCaptcha("https://auth.roblox.com/v2/login", data=JSONLogin,
                           Headers={"Accept": "application/json", "x-csrf-token": requests.post(
                               'https://auth.roblox.com/v1/usernames/validate'
                           ).headers['x-csrf-token']}, session=session, WaitAfterComplete=WaitAfterCaptcha,Type=str(CaptchaType(CaptchaMetatable.WebLogin)))

        def MakePost():
            tok = session.post(
                'https://auth.roblox.com/v1/usernames/validate'
            ).headers['x-csrf-token']
            Debug(tok)
            post = session.post("https://auth.roblox.com/v2/login",
                                headers={"Accept": "application/json", "x-csrf-token": tok}, json=JSONLogin)
            return post

        a = MakePost()
        b = a.json()['errors'][0]['fieldData']
        if b:
            Output("Captcha is required!")
            td = c.GetDetailsFromFieldData2(b)
            f = c.StartSessionFromDetails(td['TokenID'], td['location'])
            Debug(f.json())
            if f:
                # make the authenticated request using the session of the current user
                # make the authenticated request using the session of the current user
                if "user" in f.json():
                    # make the authenticated request using the session of the current user
                    Output("Success")
                    return session, {"Username": Username, 'Password': password, "UserId": f.json()["user"]['id'],
                                     "displayName": f.json()["user"]['displayName']}
            else:
                if retry:

                    s, info = _retloginSession(session, Username, password, WaitAfterCaptcha, retry)
                    Debug(str('{} {}'.format(s, info)))
                    if info["UserId"]:
                        Output("Successfully signed up")
                        return s, info

        #details = c.GetDetails()
        #c.StartSession()
        #print(c.Token, c.ID)
#signupSession("".join(random.choices(string.digits + string.ascii_uppercase + string.ascii_lowercase,k=10)),"markdarss")