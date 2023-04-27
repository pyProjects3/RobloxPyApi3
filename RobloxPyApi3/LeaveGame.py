import subprocess
from RobloxPyApi3.Errors import NoRobloxProcessFound

def LeaveGame(showErrors=bool):
    try:
        #os.system("start AnonymousLeave.pyw")
        subprocess.run("taskkill /im RobloxPlayerBeta.exe /f")
    except Exception as Error:
        if showErrors == True:
            raise NoRobloxProcessFound("Failed to end Roblox process (RobloxPlayerBeta.exe), make sure that roblox is running.")
        else:
            return

