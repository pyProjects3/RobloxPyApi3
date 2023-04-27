
from RobloxPyApi3.AccountInformation import AccountInformationSession
from RobloxPyApi3.FriendsAPI import FriendsSession
from RobloxPyApi3.JoinGame import RobloxProcOpen
class SessionAPI(AccountInformationSession,FriendsSession,RobloxProcOpen):
    def __init__(self,session,Password):
        AccountInformationSession.__init__(self,session=session,password=Password)
        FriendsSession.__init__(self,session=session,password=Password)
        RobloxProcOpen.__init__(self,session=session)
