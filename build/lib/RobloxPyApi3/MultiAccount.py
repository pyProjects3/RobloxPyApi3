import RobloxPyApi3.Auth as Auth
import requests
import pickle
from RobloxPyApi3.Auth import Gender, Date, NewDate
from RobloxPyApi3.Enums import Months
from RobloxPyApi3.Enums import MonthsNum
from RobloxPyApi3.SessionUtilities import SessionAPI
import random
from typing import List
import string
import time

class Account(SessionAPI):

    def __init__(self,session,username,password,Birthdate,userId,Gender):
        super().__init__(session=session,Password=password)
        self.Username: str = username
        self.Password = password
        self.Birthdate = Birthdate
        self.UserId : int = userId
        self.Session:requests.Session = session
        self.Gender = Gender
    @property
    def session(self):
        return self.Session
    def SetProxy(self,ProxyServer,Protocol = "http"):
        prot = Protocol.lower()
        self.Session.proxies[prot] = str("{}://{}".format(prot,ProxyServer))
        print(self.Session.proxies)
    def RemoveProxies(self):
        self.Session.proxies.clear()
        #self.Session.proxies = None
    def SetProxies(self,dict):
        self.Session.proxies = dict
        print(self.Session.proxies)
    @property
    def Cookie(self):
        return self.Session.cookies.get(name=".ROBLOSECURITY")
    def to_dict(self) -> dict:
        return {'password':self.Password,'Birthdate': "{} {} {}".format(self.Birthdate.d,self.Birthdate.month,self.Birthdate.year),"UserId":self.UserId,"Gender":self.Gender}
class MultiAccountHandler:
    def __init__(self):
        self.AccountsDetails = {}
        self.Accounts: List[Account] = []
    def _AddAccountToList(self,Username,AccountDetails):
        self.AccountsDetails[Username] = AccountDetails
    def Auth_Config(self,CaptchaDelay = 4.5,Outputting = True,Debugging = True):
        Auth.init(CaptchaDelay=CaptchaDelay,Output=Outputting,Debug=Debugging)
    def SignUp(self,Username,password,gender = Gender.Random,birthday = Date(22,Months.JANUARY,1980),WaitAfterCaptcha = 2,retry = True) -> Account:
        Session,Info = Auth.signupSession(Username=Username,password=password,gender=gender,birthday=birthday,WaitAfterCaptcha=WaitAfterCaptcha,retry=retry)
        if 'UserId' in Info:
            acc = Account(Session,Username,password,birthday,Info["UserId"],Info["Gender"])
            self.AddAccount(acc)
            return acc
    def Login(self, Username, password, gender=Gender.Random, birthday=Date(22, Months.JANUARY, 1980),
               WaitAfterCaptcha=2, retry=True) -> Account:
        Session, Info = Auth.LoginSession(Username=Username, password=password,
                                           WaitAfterCaptcha=WaitAfterCaptcha, retry=retry)
        if 'UserId' in Info:
            acc = Account(Session, Username, password, birthday, Info["UserId"], Info["Gender"])
            self.AddAccount(acc)
            return acc

    def AddAccount(self, account: Account):
        if not self.AccountInClass(account.Username):
            self.Accounts.append(account)
            self.AccountsDetails[account.Username] = account.to_dict()
    def Save(self,Name = "SavedMultiHandler"):
        with open(f'{Name}.pkl', 'wb') as f:
            pickle.dump(self, f)
    def GetAccount(self,Name) -> Account:
        if self.Accounts != []:

            for account in self.Accounts:
                if account.Username.lower() == Name.lower():
                    return account
    def AccountInClass(self,Name) -> bool:
        if self.Accounts != []:

            for account in self.Accounts:
                if account.Username.lower() == Name.lower():
                    return True
        return False
    def RemoveAccount(self,AccountName):
        if self.AccountInClass(AccountName):
            account = self.GetAccount(AccountName)
            del self.AccountsDetails[account.Username]
            self.Accounts.remove(account)
    def RemoveAccountObject(self,Account:Account):
        del self.AccountsDetails[Account.Username]
        self.Accounts.remove(Account)
    def Load(self,Name="SavedMultiHandler"):
        try:
            with open(f'{Name}.pkl', 'rb') as f:
                Data: 'MultiAccountHandler' = pickle.load(f)
                self.Accounts = Data.Accounts
                self.AccountsDetails = Data.AccountsDetails
        except FileNotFoundError:
            raise FileNotFoundError(f"File 'SavedMultiHandler.pkl' was not found, Save the Multi-handler to fix it.")

    def UpdateAllAccounts(self):
        if self.Accounts:
            for acc in self.Accounts:
                # Get updated account info
                updated_account = Account(acc.Session, acc.Username, acc.Password, acc.Birthdate, acc.UserId,
                                          acc.Gender)
                updated_account_info = updated_account.to_dict()

                # Update the account details in the class dictionary
                self.AccountsDetails[acc.Username] = updated_account_info

                # Update the properties of the account instance
                acc.Password = updated_account.Password
                acc.Birthdate = updated_account.Birthdate
                acc.UserId = updated_account.UserId
                acc.Gender = updated_account.Gender
                acc.Session = updated_account.session
def Load_Handler(Name = "SavedMultiHandler") -> MultiAccountHandler:
    try:
        with open(f'{Name}.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return
def Get_Handler(Name = "SavedMultiHandler"):
    try:
        with open(f'{Name}.pkl', 'rb') as f:
            return f
    except FileNotFoundError:
        return
"""
MAH = Load_Handler()
print(MAH.AccountsDetails)
try:
    print()
    #for i in range(2):
     #   MAH.SignUp("".join(random.choices(string.digits + string.ascii_uppercase + string.ascii_lowercase,k=10)),"markdarss")
    #    MAH.Save()
    #for acc in MAH.Accounts:
    #    rand = "".join(random.choices(string.hexdigits + string.whitespace + string.octdigits + string.punctuation + string.printable,k=200))
    #    print(acc.Username)
    #    continue
    # List of adjectives to use in the username
    adjectives = ['Gamer', 'Cool', 'nice', 'green', 'red', 'Fearless', 'Dark', 'Bright', 'White', 'Shiny',"Good"]

    # List of nouns to use in the username
    nouns = ['Wolf', 'Dragon', 'Knight', 'Warrior', 'Hero', 'Pirate', 'Ninja', 'Samurai', 'Wizard', 'Viking',
             "Emily", "Liam", "Ava", "Noah", "Olivia", "Ethan", "Emma", "Lucas", "Isabella", "Mason", "Sophia", "Logan",
             "Mia", "Jackson", "Charlotte", "Jacob", "Amelia", "Caden", "Harper", "William", "Evelyn", "Oliver",
             "Abigail", "Elijah", "Ella", "Grayson", "Madison", "Michael", "Scarlett", "Benjamin", "Avery", "Carter",
             "Lily", "Luke", "Chloe", "Daniel", "Aria", "Gabriel", "Ellie", "Matthew", "Nora", "Jayden", "Hazel",
             "James", "Zoe", "Lincoln", "Luna", "Jackson", "Grace", "Owen", "Violet", "Levi", "Riley", "Alexander",
             "Aurora", "Sebastian", "Aaliyah", "Isaac", "Stella", "Wyatt", "Nova", "Hunter", "Emilia", "Christian",
             "Everly", "Jonathan", "Valentina", "Ezra", "Adalyn", "Jaxon", "Brooklyn", "Nicholas", "Bella", "Jace",
             "Genesis", "Nathan", "Savannah", "Caleb", "Skylar", "Landon", "Paisley", "John", "Victoria", "David",
             "Eleanor", "Adam", "Leah", "Grayson", "Hannah", "Ian", "Audrey", "Cooper", "Aubrey", "Isaiah", "Claire",
             "Carson", "Penelope", "Charles", "Natalie", "Max", "Addison", "Joseph", "Mila", "Mateo", "Liliana",
             "Antonio", "Rosalie","User"]
    #proxies = {
    #    'http': [
    #        "103.82.157.146:8080"
    #        "102.165.51.172:3128"
    #    ]
    #}
    proxies = {
        'http': [
            '182.18.208.59:3128',
            '103.127.1.130:80',
            '121.199.78.228:8888',
            '35.247.242.101:3129',
            '120.197.40.219:9002',
            '71.19.248.67:8001',
            '182.48.204.35:8080',
            '35.247.243.231:3129',
            '167.172.238.15:9991',
            '106.75.18.223:80',
            '113.57.84.39:9091',
            '35.247.255.188:3129',
            '209.38.252.159:8080',
            '65.108.230.239:40657',
            '35.247.198.196:3129',
            '161.35.70.249:8080',
            '61.160.212.98:8111',
            '146.59.199.12:80',
            '200.35.49.57:42541',
            '51.77.194.204:80',
            '128.199.202.122:8080',
            '65.108.69.40:10048',
            '179.63.149.4:999',
            '114.255.132.60:3128',
            '197.246.212.70:3030'
        ]
    }

    # Generate a random number to add to the end of the username
    number = random.randint(1000, 9999)

    # Combine a random adjective, noun, and number to create the username
    username = random.choice(adjectives) + random.choice(nouns) + str(number)
    print(username)
    # Print the generated username
    print(username)
    print(MAH.Accounts)
    r = "".join(random.choices(string.digits + string.ascii_uppercase + string.ascii_lowercase,k=10))
    MAH.UpdateAllAccounts()
    for acc in MAH.Accounts:
        acc.Session.proxies = {}
        print(acc.Session.proxies)
        prox = random.choice(proxies["http"])
        print(prox)
        acc.SetProxy(prox)

        print(acc.Session.proxies)
        #acc.SetProxy(Protocol=prot,ProxyServer=procserv)
        acc.SetDescription(f"Im a bot that uses Proxy: {prox}")
    #for i in range(5):
        #account = MAH.SignUp(username,"markdarss")
        #if account:
            #print(account.session)
            #print(account.to_dict())

except Exception as err:
    print(err)
"""