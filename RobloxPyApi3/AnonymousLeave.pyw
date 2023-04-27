import subprocess

def Leave():
    try:
        subprocess.run("taskkill /im RobloxPlayerBeta.exe /f",shell=True)
        exit(0)
    except:
        exit(-1)
if __name__ == '__main__':
    Leave()