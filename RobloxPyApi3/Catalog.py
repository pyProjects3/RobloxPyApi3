import socket
import requests
from RobloxPyApi3.Errors import Error,GetCategoriesFailed,APIConnectFailed,InvalidBundleId,ListBundlesFromAssetIdFailed,InvalidAssetId,NoItemFound,FindItemInBundleFailed,GetBundleDetailsFailed,GetBundleRecommendationFailed,InvalidUserId,GetPlayerBundlesFailed,NoContentError,UnpackBundleFailed,GetassetToCategoryFailed,GetassetToSubCategoryFailed
def list_bundles_from_assetId(cookie,assetId,showErrors=bool):
    try:
        socket.create_connection(('google.com',80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/assets/{assetId}/bundles",headers={"Accept":"application/json","cookie":f".ROBLOSECURITY={cookie}"},cookies={".ROBLOSECURITY":cookie})

    if 'errors' in a.json():
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid assetId":
                raise InvalidAssetId(f"AssetId: {assetId} is invalid.")
            raise ListBundlesFromAssetIdFailed(
                f"A process returned exception, make sure the AssetId:{assetId} is Valid, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def Get_Bundle_Details(cookie,bundleId,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/bundles/{bundleId}/details",
                     headers={"Accept": "application/json", "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})

    if 'errors' in a.json():
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid bundle":
                raise InvalidBundleId(f"BundleId: {bundleId} is invalid.")
            raise GetBundleDetailsFailed(
                f"A process returned exception, make sure the BundleId:{bundleId} is Valid, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()

def Get_BundleName_From_BundleId(cookie,bundleId,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/bundles/{bundleId}/details",
                     headers={"Accept": "application/json", "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})

    if 'errors' in a.json():
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid bundle":
                raise InvalidBundleId(f"BundleId: {bundleId} is invalid.")
            raise GetBundleDetailsFailed(
                f"A process returned exception, make sure the BundleId:{bundleId} is Valid, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()["name"]
def Get_Items_From_Bundle(cookie,bundleId,showErrors=bool):
    results = []
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/bundles/{bundleId}/details",
                     headers={"Accept": "application/json", "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})

    if 'errors' in a.json():
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid bundle":
                raise InvalidBundleId(f"BundleId: {bundleId} is invalid.")
            raise GetBundleDetailsFailed(
                f"A process returned exception, make sure the BundleId:{bundleId} is Valid, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:

        for i in range(124204):
            try:
                if a.json()['items'][i]['name']:

                    results.append(a.json()['items'][i]['name'])
                else:
                    continue
            except IndexError:
                break
        return results
def Find_Item_In_Bundle(cookie,bundleId,AssetId,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/bundles/{bundleId}/details",
                     headers={"Accept": "application/json", "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})

    if 'errors' in a.json():
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid bundle":
                raise InvalidBundleId(f"BundleId: {bundleId} is invalid.")
            elif a.json()['errors'][0]['message'] == "Invalid assetId":
                raise NoItemFound(f"Invalid assetId: {AssetId}")
            raise GetBundleDetailsFailed(
                f"A process returned exception, make sure the BundleId: {bundleId} is Valid, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:

        for i in range(124204):
            try:
                if a.json()['items'][i]['id'] == AssetId:
                    return a.json()['items'][i]['name']
                else:
                    continue
            except IndexError:
                break
def CheckIf_Item_In_Bundle_IsOwned(cookie,bundleId,AssetId,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/bundles/{bundleId}/details",
                     headers={"Accept": "application/json", "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})

    if 'errors' in a.json():
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid bundle":
                raise InvalidBundleId(f"BundleId: {bundleId} is invalid.")
            elif a.json()['errors'][0]['message'] == "Invalid assetId":
                raise NoItemFound(f"Invalid assetId: {AssetId}")
            raise FindItemInBundleFailed(
                f"A process returned exception, make sure the BundleId: {bundleId} is Valid, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:

        for i in range(124204):
            try:
                if a.json()['items'][i]['id'] == AssetId:
                    if a.json()['items'][i]['owned'] == True:
                        return True
                    else:
                        return False
                else:
                    continue
            except IndexError:
                return False
def CheckIf_Item_In_Bundle(cookie,bundleId,AssetId,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/bundles/{bundleId}/details",
                     headers={"Accept": "application/json", "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})

    if 'errors' in a.json():
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid bundle":
                raise InvalidBundleId(f"BundleId: {bundleId} is invalid.")
            elif a.json()['errors'][0]['message'] == "Invalid assetId":
                raise NoItemFound(f"Invalid assetId: {AssetId}")
            raise FindItemInBundleFailed(
                f"A process returned exception, make sure the BundleId: {bundleId} is Valid, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:

        for i in range(124204):
            try:
                if a.json()['items'][i]['id'] == AssetId:
                    return True
                else:
                    continue
            except IndexError:
                return False
def Get_Bundle_Recommendation(cookie,bundleId,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/bundles/{bundleId}/recommendations",
                     headers={"Accept": "application/json", "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})

    if 'errors' in a.json():
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid bundle":
                raise InvalidBundleId(f"BundleId: {bundleId} is invalid.")
            raise GetBundleRecommendationFailed(
                f"A process returned exception, make sure the BundleId:{bundleId} is Valid, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def Find_Bundle_in_Bundle_Recommendation(cookie,bundleId,AssetId,TargetBundleId,showErrors=bool):
    result = []
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/bundles/{bundleId}/recommendations",
                     headers={"Accept": "application/json", "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})

    if 'errors' in a.json():
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid bundle":
                raise InvalidBundleId(f"BundleId: {bundleId} is invalid.")
            elif a.json()['errors'][0]['message'] == "Invalid assetId":
                raise NoItemFound(f"Invalid assetId: {AssetId}")
            raise GetBundleRecommendationFailed(
                f"A process returned exception, make sure the BundleId: {bundleId} is Valid, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        for i in range(323404):
            try:
                if a.json()['data'][i]["id"] == TargetBundleId:
                    result.append(a.json()['data'][i]["id"])
                else:
                    continue
            except IndexError:
                break
    return result
def Get_Bundles_Names_owned_by_Player(cookie,UserId,showErrors=bool):
    result = []
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/users/{UserId}/bundles",
                     headers={"Accept": "application/json", "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})

    if 'errors' in a.json():
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid user Id.":
                raise InvalidUserId(f"Invalid UserId: {UserId}")
            raise GetPlayerBundlesFailed(
                f"A process returned exception, make sure the UserId:{UserId} is Valid, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        for i in range(323404):
            try:
                if a.json()['data'][i]["name"]:
                    result.append(a.json()['data'][i]["name"])
                else:
                    continue
            except IndexError:
                break
    return result

def Get_Bundles_Ids_owned_by_Player(cookie,UserId,showErrors=bool):
    result = []
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/users/{UserId}/bundles",
                     headers={"Accept": "application/json", "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})

    if 'errors' in a.json():
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid user Id.":
                raise InvalidUserId(f"Invalid UserId: {UserId}")
            raise GetPlayerBundlesFailed(
                f"A process returned exception, make sure the UserId:{UserId} is Valid, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        for i in range(323404):
            try:
                if a.json()['data'][i]["id"]:
                    result.append(a.json()['data'][i]["id"])
                else:
                    continue
            except IndexError:
                break
    return result
def Unpack_Bundle(cookie,x_csrf_token,bundleId,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.post(f"https://catalog.roblox.com/v1/bundles/{bundleId}/unpack",
                     data={},
                     headers={"Accept": "application/json",'x-csrf-token':x_csrf_token, "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})
    if 'errors' in a.json():
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid bundle":
                raise InvalidBundleId(f"BundleId: {bundleId} is invalid.")
            raise UnpackBundleFailed(
                f"A process returned exception, make sure the bundleId: {bundleId} is Valid, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        if a.status_code == 204:
            if showErrors == True:
                raise NoContentError("No content.")
            else:
                return
    return a.status_code
def Get_asset_To_Category(cookie,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/asset-to-category",
                     headers={"Accept": "application/json", "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})
    if 'errors' in a.json():
        if showErrors == True:
            raise GetassetToCategoryFailed(
                f"A process returned Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def Asset_To_Subcategory(cookie,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/asset-to-subcategory",
                     headers={"Accept": "application/json", "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})
    if 'errors' in a.json():
        if showErrors == True:
            raise GetassetToSubCategoryFailed(
                f"A process returned Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def Get_Categories(cookie,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/categories",
                     headers={"Accept": "application/json", "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})
    if 'errors' in a.json():
        if showErrors == True:
            raise GetCategoriesFailed(
                f"A process returned Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def Get_subcategories(cookie,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/subcategories",
                     headers={"Accept": "application/json", "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})
    if 'errors' in a.json():
        if showErrors == True:
            raise GetCategoriesFailed(
                f"A process returned Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def Get_Asset_Favorites_Count(cookie,AssetId,showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/favorites/assets/{AssetId}/count",
                     headers={"Accept": "application/json", "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid assetId":
                raise NoItemFound(f"Invalid assetId: {AssetId}")
            raise Error(
                f"A process returned exception, make sure the AssetId:{AssetId} is Valid, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def Get_Bundle_Favorites_Count(cookie,bundleId,showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/favorites/bundles/{bundleId}/count",
                     headers={"Accept": "application/json", "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid bundle":
                raise InvalidBundleId(f"BundleId: {bundleId} is invalid.")
            raise Error(
                f"A process returned exception, make sure the BundleId: {bundleId} is Valid, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def Get_Favorite_Asset(cookie,AssetId,UserId,showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/favorites/users/{UserId}/assets/{AssetId}/favorite",
                     headers={"Accept": "application/json", "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid assetId":
                raise NoItemFound(f"Invalid assetId: {AssetId}")
            elif a.json()['errors'][0]['message'] == "Invalid user Id.":
                raise InvalidUserId(f"Invalid UserId: {UserId}")
            raise Error(
                f"A process returned exception, make sure the AssetId:{AssetId} is Valid, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def Delete_Favorite_Asset(cookie,x_csrf_token,AssetId,YourUserId,showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.delete(f"https://catalog.roblox.com/v1/favorites/users/{YourUserId}/assets/{AssetId}/favorite",
                     headers={"Accept": "application/json",'x-csrf-token':x_csrf_token, "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid assetId":
                raise NoItemFound(f"Invalid assetId: {AssetId}")
            elif a.json()['errors'][0]['message'] == "Invalid user Id.":
                raise InvalidUserId(f"Invalid UserId: {YourUserId}")
            raise Error(
                f"A process returned exception, make sure the AssetId:{AssetId} is Valid and UserId:{YourUserId} is your userId, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def UnFavorite_Asset(cookie,x_csrf_token,AssetId,YourUserId,showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.delete(f"https://catalog.roblox.com/v1/favorites/users/{YourUserId}/assets/{AssetId}/favorite",
                     headers={"Accept": "application/json",'x-csrf-token':x_csrf_token, "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid assetId":
                raise NoItemFound(f"Invalid assetId: {AssetId}")
            elif a.json()['errors'][0]['message'] == "Invalid user Id.":
                raise InvalidUserId(f"Invalid UserId: {YourUserId}")
            raise Error(
                f"A process returned exception, make sure the AssetId:{AssetId} is Valid and UserId:{YourUserId} is your userId, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def Create_Favorite_Asset(cookie,x_csrf_token,AssetId,YourUserId,showErrors=bool):

    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.post(f"https://catalog.roblox.com/v1/favorites/users/{YourUserId}/assets/{AssetId}/favorite",
                     headers={"Accept": "application/json",'x-csrf-token':x_csrf_token, "cookie": f".ROBLOSECURITY={cookie}"},
                     cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid assetId":
                raise NoItemFound(f"Invalid assetId: {AssetId}")
            elif a.json()['errors'][0]['message'] == "Invalid user Id.":
                raise InvalidUserId(f"Invalid UserId: {YourUserId}")
            raise Error(
                f"A process returned exception, make sure the AssetId:{AssetId} is Valid and UserId:{YourUserId} is your userId, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()


def Favorite_Asset(cookie, x_csrf_token, AssetId, YourUserId, showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.post(f"https://catalog.roblox.com/v1/favorites/users/{YourUserId}/assets/{AssetId}/favorite",
                      headers={"Accept": "application/json", 'x-csrf-token': x_csrf_token,
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid assetId":
                raise NoItemFound(f"Invalid assetId: {AssetId}")
            elif a.json()['errors'][0]['message'] == "Invalid user Id.":
                raise InvalidUserId(f"Invalid UserId: {YourUserId}")
            raise Error(
                f"A process returned exception, make sure the AssetId:{AssetId} is Valid and UserId:{YourUserId} is your userId, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def Get_Favorite_Bundle(cookie, bundleId, YourUserId, showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.get(f"https://catalog.roblox.com/v1/favorites/users/{YourUserId}/bundles/{bundleId}/favorite",
                      headers={"Accept": "application/json",
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid bundle":
                raise InvalidBundleId(f"BundleId: {bundleId} is invalid.")
            elif a.json()['errors'][0]['message'] == "Invalid user Id.":
                raise InvalidUserId(f"Invalid UserId: {YourUserId}")
            raise Error(
                f"A process returned exception, make sure the BundleId:{bundleId} is Valid and UserId:{YourUserId} is your userId, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def Delete_Favorite_Bundle(cookie,x_csrf_token, bundleId, YourUserId, showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.delete(f"https://catalog.roblox.com/v1/favorites/users/{YourUserId}/bundles/{bundleId}/favorite",
                      headers={"Accept": "application/json",'x-csrf-token':x_csrf_token,
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid bundle":
                raise InvalidBundleId(f"BundleId: {bundleId} is invalid.")
            elif a.json()['errors'][0]['message'] == "Invalid user Id.":
                raise InvalidUserId(f"Invalid UserId: {YourUserId}")
            raise Error(
                f"A process returned exception, make sure the BundleId:{bundleId} is Valid and UserId:{YourUserId} is your userId, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def UnFavorite_Bundle(cookie,x_csrf_token, bundleId, YourUserId, showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.delete(f"https://catalog.roblox.com/v1/favorites/users/{YourUserId}/bundles/{bundleId}/favorite",
                      headers={"Accept": "application/json",'x-csrf-token':x_csrf_token,
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid bundle":
                raise InvalidBundleId(f"BundleId: {bundleId} is invalid.")
            elif a.json()['errors'][0]['message'] == "Invalid user Id.":
                raise InvalidUserId(f"Invalid UserId: {YourUserId}")
            raise Error(
                f"A process returned exception, make sure the BundleId:{bundleId} is Valid and UserId:{YourUserId} is your userId, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def Create_Favorite_Bundle(cookie,x_csrf_token, bundleId, YourUserId, showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.post(f"https://catalog.roblox.com/v1/favorites/users/{YourUserId}/bundles/{bundleId}/favorite",
                      headers={"Accept": "application/json",'x-csrf-token':x_csrf_token,
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid bundle":
                raise InvalidBundleId(f"BundleId: {bundleId} is invalid.")
            elif a.json()['errors'][0]['message'] == "Invalid user Id.":
                raise InvalidUserId(f"Invalid UserId: {YourUserId}")
            raise Error(
                f"A process returned exception, make sure the BundleId:{bundleId} is Valid and UserId:{YourUserId} is your userId, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def Favorite_Bundle(cookie,x_csrf_token, bundleId, YourUserId, showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.post(f"https://catalog.roblox.com/v1/favorites/users/{YourUserId}/bundles/{bundleId}/favorite",
                      headers={"Accept": "application/json",'x-csrf-token':x_csrf_token,
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if a.status_code != 200:
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid bundle":
                raise InvalidBundleId(f"BundleId: {bundleId} is invalid.")
            elif a.json()['errors'][0]['message'] == "Invalid user Id.":
                raise InvalidUserId(f"Invalid UserId: {YourUserId}")
            raise Error(
                f"A process returned exception, make sure the BundleId:{bundleId} is Valid and UserId:{YourUserId} is your userId, Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def Get_Items_Details(cookie,x_csrf_token,AssetId,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.post(f"https://catalog.roblox.com/v1/catalog/items/details",
                      data={"items":[{'itemType':"Asset",'id':AssetId}]},
                      headers={"Accept": "application/json",'x-csrf-token':x_csrf_token,
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if 'errors' in a.json():
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid assetId":
                raise NoItemFound(f"Invalid assetId: {AssetId}")
            raise Error(
                f"A process returned Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()
def Items_Details(cookie,x_csrf_token,AssetId,showErrors=bool):
    try:
        socket.create_connection(('google.com', 80))
    except socket.gaierror:
        if showErrors == True:
            raise APIConnectFailed("No internet connection, check your internet connection and try again.")
        else:
            return
    a = requests.post(f"https://catalog.roblox.com/v1/catalog/items/details",
                      data={"items":[{'itemType':"Asset",'id':AssetId}]},
                      headers={"Accept": "application/json",'x-csrf-token':x_csrf_token,
                               "cookie": f".ROBLOSECURITY={cookie}"},
                      cookies={".ROBLOSECURITY": cookie})

    if 'errors' in a.json():
        if showErrors == True:
            if a.json()['errors'][0]['message'] == "Invalid assetId":
                raise NoItemFound(f"Invalid assetId: {AssetId}")
            raise Error(
                f"A process returned Exception: {a.json()['errors'][0]['message']} Response: {a.status_code} ")
        else:
            return
    else:
        return a.json()

