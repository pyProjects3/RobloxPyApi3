from enum import Enum
class Gender(Enum):
    male = 2
    female = 1
    Unknown = 0
    Random = 3
class Privacy(Enum):
    FRIENDS_FOLLOWING_AND_FOLLOWERS = "FriendsFollowingAndFollowers"
    NO_ONE = "NoOne"
    EVERYONE = "AllUsers"
    FRIENDS_AND_FOLLOWING = "FriendsAndFollowing"
    FRIENDS = "Friends"
class sortOrder(Enum):
    DESC = "Des"
    ASC = "Asc"
class Months(Enum):
    JANUARY = 'Jan'
    FEBRUARY = 'Feb'
    MARCH = 'Mar'
    APRIL = 'Apr'
    MAY = 'May'
    JUNE = 'Jun'
    JULY = 'Jul'
    AUGUST = 'Aug'
    SEPTEMBER = 'Sep'
    OCTOBER = 'Oct'
    NOVEMBER = 'Nov'
    DECEMBER = 'Dec'
class MonthsNum(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12
class CaptchaMetatable(Enum):
    SignUp = "A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F"
    AssetComment = "63E4117F-E727-42B4-6DAA-C8448E9B137F"
    ClothingAssetUpload = "63E4117F-E727-42B4-6DAA-C8448E9B137F"
    FollowUser = "63E4117F-E727-42B4-6DAA-C8448E9B137F"
    GenericChallenge = "CC30DB96-0C88-4DEB-86E5-6601927ACBB4"
    GroupJoin = "63E4117F-E727-42B4-6DAA-C8448E9B137F"
    GroupWallPost = "63E4117F-E727-42B4-6DAA-C8448E9B137F"
    SupportRequest = "63E4117F-E727-42B4-6DAA-C8448E9B137F"
    WebGamecardRedemption = "1B154715-ACB4-2706-19ED-0DC7E3F7D855"
    WebLogin = "476068BF-9607-4799-B53D-966BE98E2B81"
    WebResetPassword = "476068BF-9607-4799-B53D-966BE98E2B81"