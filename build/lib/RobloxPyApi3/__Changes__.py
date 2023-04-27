from RobloxPyApi3.Version import __PackageVersion__
__Version__ = __PackageVersion__
__Changes__ = f"""
---- CHANGES IN {__Version__} Date: // ----:
1.0.5 is the Release Version.
1. Added friends Api.
2. fixed bugs.
3. Added friends api inside the bot class.
4. Added friends api inside the Client class.
5. Added friends api inside the main python script.

"""
Version_1_0_6 = \
    """---- CHANGES IN 1.0.6 Date: 30/7/2022 ----:
1.0.5 is the Release Version.
1. Added new functions in the Avatar Api Module (RobloxPyApi3\\Avatar.py).
2. Added __Changes__.py inside the main package module init (RobloxPyApi3\\__init__.py).
3. Added __Changes__.py for viewing Changes log. to view, import RobloxPyApi3 and print(RobloxPyApi3.__Changes__.py).
4. Added Avatar Api Module functions to the client and bot class (class bot, class client).
5. Added new functions.
6. Added LeaveGame.py, JoinGame.py to RobloxPyApi3.
7. Added LeaveGame and JoinGame functions to the client and bot class (class bot, class client).
8. Fixed bugs."""
Version_2_0_6 = \
"""
---- MAJOR CHANGES IN 2.0.6 DATE: 27/4/2023 ----:
Some features might be repeated, and might not be used. 
In the main package, its still using cookies for authentication. 
UPDATES:
2.0.6 is a major update:
1. Added Multi Account handler, which supports proxies inside MultiAccount.py.
2. Added account creation system with CAPTCHA in auth.py.
3. Added Account Login system with CAPTCHA in auth.py
4. Added Module Place inside RobloxPyApi3, you can now create your own place in python!
5. Added Save and load inside Multi Account Handler (MAH).
6. Added NEW account information and Friends API, which now supports MAH system (Multi account handler).
7. You can now manage CAPTCHA, if you want to use Roblox captcha, you can now do that in Captcha.py.
8. Added Utilities script inside Utilities.py and SessionUtilities.py which used in MAH system.
9. Added Enums module, which can be used as parameters of some functions in the module.
10. Added 2 methods of captcha initialization, if SessionCaptcha.GetDetailsFromFieldData doesnt work, use GetDetailsFromFieldData2.
11. Added Captcha types inside Enums (Enums.py) Use CaptchaMetatable to get Keys from different captchas and use it in SessionCaptcha,
Not Captcha, to use CaptchaMetatable in Enums, it would be Enums.CaptchaMetatable.SignUp.Value (for example, SignUp Captcha Key)
12. Added Verification complete detection in Captcha.py.
13. Bug fixes.
"""