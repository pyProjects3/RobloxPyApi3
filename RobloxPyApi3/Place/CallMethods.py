from enum import Enum
class Color3(Enum):
    new = 0
    fromRGB = 1
    fromHex = 2
    fromHSV = 3
class DefaultPropertyTypes(Enum):
    string = 0
    number = 1

    bool = 2
class BrickColor(Enum):
    new = 0

    Palette = 10
class UDim2(Enum):
    new = 0
    fromscale = 1
    fromoffset = 2
class BrickColor_Shorthanded(Enum):
    Random = 1
    Red = 2
    White = 3
    Gray = 4
    DarkGray = 5
    Black = 6
    Yellow = 7
    Green = 8
    Blue = 9
class RobloxService(Enum):
    ReplicatedFirst = "ReplicatedFirst"
    ReplicatedStorage = "ReplicatedStorage"
    ServerScriptService = "ServerScriptService"
    ServerStorage = "ServerStorage"
    Workspace = "Workspace"
    Lighting = "Lighting"
    Players = "Players"
    Teams = "Teams"
    Debris = "Debris"
    HttpService = "HttpService"
    RunService = "RunService"
    UserInputService = "UserInputService"
    InsertService = "InsertService"
    PathfindingService = "PathfindingService"
    Chat = "Chat"
    TeleportService = "TeleportService"
    BadgeService = "BadgeService"
    AssetService = "AssetService"
    GroupService = "GroupService"
    MarketplaceService = "MarketplaceService"
    PointsService = "PointsService"
    EconomyService = "EconomyService"
    SocialService = "SocialService"
    AnalyticsService = "AnalyticsService"
    LocalizationService = "LocalizationService"
    TextService = "TextService"
    VoiceChatService = "VoiceChatService"
    MessagingService = "MessagingService"
    NotificationService = "NotificationService"
    AvatarEditorService = "AvatarEditorService"
    ContentProvider = "ContentProvider"
    ContextActionService = "ContextActionService"
    GuiService = "GuiService"
    HapticService = "HapticService"
    PathService = "PathService"
    PhysicsService = "PhysicsService"
    SoundService = "SoundService"
    TestService = "TestService"
    ToolService = "ToolService"
