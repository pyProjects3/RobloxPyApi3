import requests
from RobloxPyApi3 import Errors
def GetToken(s = None):
    if s != None:
        tok = s.post(
            'https://auth.roblox.com/v1/usernames/validate'
        ).headers['x-csrf-token']
    else:
        tok = requests.post(
            'https://auth.roblox.com/v1/usernames/validate'
        ).headers['x-csrf-token']
    return tok
def Post_Request(url, session = None, data=None) -> requests.Response:
    try:
        if session == None:
            req = requests.post(url=url, data=data, headers={"accept": "application/json",
                                                             "x-csrf-token": GetToken(),
                                                             })
            return req
        else:
            req = session.post(url=url, data=data, headers={"accept": "application/json",
                                                            "x-csrf-token": GetToken(session),
                                                            })
            return req
    except Exception as error:
        raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def Delete_Request(url, session = None) -> requests.Response:
    try:
        if url:
            if not session:
                req = requests.delete(url=url,headers={"accept":"application/json",
                                                         "x-csrf-token": GetToken(),
                                                        'Content-Type': 'application/json'})
                return req
            else:
                req = session.delete(url=url,headers={"accept":"application/json",
                                                         "x-csrf-token": GetToken(session),
                                                        'Content-Type': 'application/json'
                                                              })
                return req
        else:
            raise Errors.UrlNotSpecified("You must specify the url before getting the request.")
    except Exception as error:
        raise Errors.MakeRequestFailed("An error occurred: {}".format(error))
def Get_Request(url, session = None) -> requests.Response:
    try:
        if url:
            if not session:
                req = requests.get(url=url,headers={'Content-Type': "application/json" })
                return req
            else:
                req = session.get(url=url,headers={"content-type": "application/json"})
                return req
        else:
            raise Errors.UrlNotSpecified("You must specify the url before getting the request.")
    except Exception as error:

        raise Errors.MakeRequestFailed("An error occurred: {}".format(error))