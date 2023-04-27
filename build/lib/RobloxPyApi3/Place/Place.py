import xml.etree.ElementTree as ET
import random
import warnings
import RobloxPyApi3.Place.CallMethods as cm
import os
import time
from RobloxPyApi3.Errors import ValueNotSet,OpenProjectFail
class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_dict(self):
        return {"X": self.x, "Y": self.y, "Z": self.z}
class UDim2:
    def __init__(self,xScale = 0,xOffset = 0,YScale = 0,YOffSet = 0):
        self.xs = xScale
        self.xo = xOffset
        self.ys = YScale
        self.yo = YOffSet
    def to_dict(self):
        return {"XScale": self.xs,'XOffset':self.xo,'YScale':self.ys,'YOffset':self.yo}
class Vector2:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y

    def to_dict(self):
        return {"X": self.x, "Y": self.y}
class BrickColor:
    def __init__(self,FullBrickColor):
        self.bc = FullBrickColor
class Enum:
    def __init__(self, FullEnumItem):
        self.Enum = FullEnumItem

    def __str__(self):
        splt = ''
        for item in self.Enum:
            if item:
                if splt == "":
                    splt = f'{item}'
                else:
                    splt = f"{splt}.{item}"
        return splt


class Color3:
    def __init__(self, R, G, B):
        self.r = R
        self.g = G
        self.b = B

    def to_dict(self):
        return {"R": self.r, "G": self.g, "B": self.b}
class CFrame:
    def __init__(self,x, y, z, r00 = 0, r01 = 0, r02 = 0, r10 = 0, r11 = 0, r12 = 0, r20 = 0, r21 = 0, r22 = 0):
        self.X : int =  x
        self.Y : int  = y
        self.Z : int  = z
        self.r00 : int  = r00
        self.r01 : int  = r01
        self.r02 : int  = r02
        self.r10 : int  = r10
        self.r11 : int  = r11
        self.r12 : int  = r12
        self.r20 : int  = r20
        self.r21 : int  = r21
        self.r22 : int  = r22

    def to_dict(self):
        return {"X": self.X, "Y": self.Y, "Z": self.Z,'R00' : self.r00,'R01' : self.r01,'R02' : self.r02,'R10' : self.r10,'R11' : self.r11,'R12' : self.r12,'R20' : self.r20,'R21' : self.r21,'R22' : self.r22}

class Script:
    def __init__(self, parent, root, name):
        self.instance = 'Script'
        self.workspace = parent
        self.CreatedInstance = None
        self.Props = None
        self.Enabled = True
        self.root = root
        self.Name = name
        self.PropsTable = {}

    def CreateInstance(self):
        Disabled = None
        if self.Enabled == True:
            Disabled = 'true'
        elif self.Enabled == False:
            Disabled = 'false'
        else:
            Disabled = 'false'
        part = ET.SubElement(self.workspace, "Item")
        part.set("class", self.instance)
        part.set("referent", f"RBX{random.randint(100, 9999)}")
        self.CreatedInstance = part
        self.Props = ET.SubElement(part, "Properties")
        ET.SubElement(self.Props, "bool", name="Enabled").text = Disabled
        return self.root, self.workspace

    @property
    def GetParent(self):
        return self.workspace

    def CreatePropertiesSection(self):
        Disabled = None
        if self.Enabled == True:
            Disabled = 'true'
        elif self.Enabled == False:
            Disabled = 'false'
        else:
            Disabled = 'false'

        if not self.CreatedInstance:
            raise ValueError("CreateInstance method should be called first")
        self.Props = ET.SubElement(self.CreatedInstance, "Properties")

        ET.SubElement(self.Props, "bool", name="Enabled").text = Disabled
    def AddProperty(self, fullPropertyName, FullPropertyType, Value):
        FullVal = None
        if Value:
            if Value == True:
                FullVal = 'true'
            elif Value == False:
                FullVal = "false"
            elif Value == "":
                FullVal = ""
            elif Value == None:
                FullVal = ""
            else:
                FullVal = str(Value)
        else:
            raise ValueNotSet("Value was not set, please set the value")
        if FullPropertyType == cm.DefaultPropertyTypes.bool:
            ET.SubElement(self.Props, "bool", name=fullPropertyName).text = FullVal
        elif FullPropertyType == cm.DefaultPropertyTypes.string:
            ET.SubElement(self.Props, "string", name=fullPropertyName).text = FullVal
        elif FullPropertyType == cm.DefaultPropertyTypes.number:
            ET.SubElement(self.Props, "number", name=fullPropertyName).text = FullVal
        else:
            ET.SubElement(self.Props, FullPropertyType, name=fullPropertyName).text = FullVal
        self.PropsTable[fullPropertyName] = FullVal

    def AddCode(self, code):
        if not self.CreatedInstance:
            raise ValueError("CreateInstance method should be called first")
        else:
            ET.SubElement(self.Props, "string", name="Name").text = self.Name
            ET.SubElement(self.Props, "ProtectedString", name="Source").text = code
            self.PropsTable["Source"] = code
            self.PropsTable['Name'] = self.Name
        return self.root, self.workspace

    def GetInstance(self):
        return self.CreatedInstance
    @property
    def Parent(self):
        return self.workspace
    @property
    def Instance(self):
        return self.CreatedInstance

    @property
    def InstanceContent(self):
        return ET.tostring(self.CreatedInstance)

    @property
    def GetAllSetProperties(self):
        return self.PropsTable

    def GetProperty(self, PropertyNameSet):

        print("This feature is on beta mode.")
        print(
            "Note that this will only work with values you set. if you set the Name value, it will get Name and return it. It wont work with updating values like magnitude.")
        try:
            Prop = self.PropsTable[PropertyNameSet]
            if Prop:
                return Prop
        except:
            return

class LocalScript:
    def __init__(self, parent, root, name):
        self.instance = 'LocalScript'
        self.workspace = parent
        self.CreatedInstance = None
        self.Props = None
        self.Disabled = False
        self.root = root
        self.Name = name
        self.PropsTable = {}

    def CreateInstance(self):
        Disabled = None
        if self.Disabled == True:
            Disabled = 'true'
        elif self.Disabled == False:
            Disabled = 'false'
        else:
            Disabled = 'false'
        part = ET.SubElement(self.workspace, "Item")
        part.set("class", self.instance)
        part.set("referent", f"RBX{random.randint(100, 9999)}")
        self.CreatedInstance = part
        self.Props = ET.SubElement(part, "Properties")
        ET.SubElement(self.Props, "bool", name="Disabled").text = Disabled
        return self.root, self.workspace

    @property
    def GetParent(self):
        return self.workspace

    def CreatePropertiesSection(self):
        Disabled = None
        if self.Disabled == True:
            Disabled = 'true'
        elif self.Disabled == False:
            Disabled = 'false'
        else:
            Disabled = 'false'

        if not self.CreatedInstance:
            raise ValueError("CreateInstance method should be called first")
        self.Props = ET.SubElement(self.CreatedInstance, "Properties")

        ET.SubElement(self.Props, "bool", name="Disabled").text = Disabled
    def AddProperty(self, fullPropertyName, FullPropertyType, Value):
        FullVal = None
        if Value:
            if Value == True:
                FullVal = 'true'
            elif Value == False:
                FullVal = "false"
            elif Value == "":
                FullVal = ""
            elif Value == None:
                FullVal = ""
            else:
                FullVal = str(Value)
        else:
            raise ValueNotSet("Value was not set, please set the value")
        if FullPropertyType == cm.DefaultPropertyTypes.bool:
            ET.SubElement(self.Props, "bool", name=fullPropertyName).text = FullVal
        elif FullPropertyType == cm.DefaultPropertyTypes.string:
            ET.SubElement(self.Props, "string", name=fullPropertyName).text = FullVal
        elif FullPropertyType == cm.DefaultPropertyTypes.number:
            ET.SubElement(self.Props, "number", name=fullPropertyName).text = FullVal
        else:
            ET.SubElement(self.Props, FullPropertyType, name=fullPropertyName).text = FullVal
        self.PropsTable[fullPropertyName] = FullVal

    def AddCode(self, code):
        if not self.CreatedInstance:
            raise ValueError("CreateInstance method should be called first")
        else:
            ET.SubElement(self.Props, "string", name="Name").text = self.Name
            ET.SubElement(self.Props, "ProtectedString", name="Source").text = code
            self.PropsTable["Source"] = code
            self.PropsTable['Name'] = self.Name
        return self.root, self.workspace

    def GetInstance(self):
        return self.CreatedInstance
    @property
    def Parent(self):
        return self.workspace
    @property
    def Instance(self):
        return self.CreatedInstance

    @property
    def InstanceContent(self):
        return ET.tostring(self.CreatedInstance)

    @property
    def GetAllSetProperties(self):
        return self.PropsTable

    def GetProperty(self, PropertyNameSet):

        print("This feature is on beta mode.")
        print(
            "Note that this will only work with values you set. if you set the Name value, it will get Name and return it. It wont work with updating values like magnitude.")
        try:
            Prop = self.PropsTable[PropertyNameSet]
            if Prop:
                return Prop
        except:
            return


class Instance:
    def __init__(self, fullName, parent, root):
        self.instance = fullName
        self.workspace = parent
        self.CreatedInstance = None
        self.Props = None

        self.root = root
        self.PropsTable = {}

    def GetProperty(self, PropertyNameSet):

        print("This feature is on beta mode.")
        print(
            "Note that this will only work with values you set. if you set the Name value, it will get Name and return it. It wont work with updating values like magnitude.")
        try:
            Prop = self.PropsTable[PropertyNameSet]
            if Prop:
                return Prop
        except:
            return

    def CreateInstance(self):
        part = ET.SubElement(self.workspace, "Item")
        part.set("class", self.instance)
        part.set("referent", f"RBX{random.randint(100, 9999)}")
        self.CreatedInstance = part
        self.Props = ET.SubElement(part, "Properties")
        return self.root, self.workspace

    def CreatePropertiesSection(self):
        if not self.CreatedInstance:
            raise ValueError("CreateInstance method should be called first")
        self.Props = ET.SubElement(self.CreatedInstance, "Properties")

    def AddProperty(self, fullPropertyName, FullPropertyType, Value):
        FullVal = None
        if Value:
            if Value == True:
                FullVal = 'true'
            elif Value == False:
                FullVal = "false"
            elif Value == None:
                FullVal = ''
            elif Value == "":
                FullVal = ''
            else:
                FullVal = str(Value)
        else:
            warnings.warn("Warning: Value was not set, please set the value")
        self.PropsTable[fullPropertyName] = FullVal
        if FullPropertyType == cm.DefaultPropertyTypes.bool:
            ET.SubElement(self.Props, "bool", name=fullPropertyName).text = FullVal
        elif FullPropertyType == cm.DefaultPropertyTypes.string:
            ET.SubElement(self.Props, "string", name=fullPropertyName).text = FullVal
        elif FullPropertyType == cm.DefaultPropertyTypes.number:
            ET.SubElement(self.Props, "number", name=fullPropertyName).text = FullVal
        else:
            ET.SubElement(self.Props, FullPropertyType, name=fullPropertyName).text = FullVal
    def AddPropertyMultipleValues(self, fullPropertyName, LuaValues:str):
        script = Script(self.GetInstance(), self.root, f"CustomProperty_{fullPropertyName}")
        script.CreateInstance()
        script.CreatePropertiesSection()
        script.AddCode(f"""
script.Parent.{fullPropertyName} = {LuaValues}
                            """)

    def AddPropertyEnum(self, fullPropertyName, EnumValue: Enum):
        script = Script(self.GetInstance(), self.root, f"EnumItem_{fullPropertyName}")
        script.CreateInstance()
        script.CreatePropertiesSection()

        script.AddCode(f"""
script.Parent.{fullPropertyName} = {EnumValue}
                            """)
    def AddPropertyColor3(self, FullPropertyName,CallMethod, color3: Color3):
        if color3:

            r, g, b = color3.r, color3.g, color3.b
            script = Script(self.GetInstance(), self.root, f"Color3_{FullPropertyName}")
            script.CreateInstance()
            script.CreatePropertiesSection()
            if CallMethod == cm.Color3.new:
                script.AddCode(f"""
script.Parent.{FullPropertyName} = Color3.new({r},{g},{b})
                        """)
            elif CallMethod == cm.Color3.fromRGB:
                script.AddCode(f"""
script.Parent.{FullPropertyName} = Color3.fromRGB({r},{g},{b})
                                        """)
            elif CallMethod == cm.Color3.fromHSV:
                script.AddCode(f"""
script.Parent.{FullPropertyName} = Color3.fromHSV({r},{g},{b})
                                        """)

        self.PropsTable.setdefault(FullPropertyName, {})["Color3"] = color3.to_dict()
        return self.root, self.workspace

    def AddPropertyBrickColor(self, FullPropertyName ,CallMethod ,Brickcolor: BrickColor):
        if Brickcolor:

            Brc = Brickcolor.bc
            script = Script(self.GetInstance(), self.root, f"BrickColor_{FullPropertyName}")
            script.CreateInstance()
            script.CreatePropertiesSection()
            if CallMethod == cm.BrickColor.new:
                script.AddCode(f"""
script.Parent.{FullPropertyName} = BrickColor.new('{Brc}')
                                        """)
            elif CallMethod == cm.BrickColor.Palette:
                    script.AddCode(f"""
script.Parent.{FullPropertyName} = BrickColor.palette({Brc})
                                                    """)
            self.PropsTable.setdefault(FullPropertyName, {})["BrickColor"] = Brc
            return self.root, self.workspace

    def AddPropertyUDim2(self, FullPropertyName, CallMethod,udim2:UDim2):
        if CallMethod:
            script = Script(self.GetInstance(), self.root, f"UDim2_{FullPropertyName}")
            script.CreateInstance()
            script.CreatePropertiesSection()
            XScale, XOffset, YScale, YOffset = udim2.xs,udim2.xo,udim2.ys,udim2.yo
            if CallMethod == cm.UDim2.new:
                script.AddCode(f"""
script.Parent.{FullPropertyName} = UDim2.new({XScale},{XOffset},{YScale},{YOffset})
""")
            elif CallMethod == cm.UDim2.fromscale:
                script.AddCode(f"""
script.Parent.{FullPropertyName} = UDim2.fromScale({XScale},{YScale})
                """)
            elif CallMethod == cm.UDim2.fromoffset:
                script.AddCode(f"""
script.Parent.{FullPropertyName} = UDim2.fromOffset({XOffset},{YOffset})
                            """)

            self.PropsTable.setdefault(FullPropertyName, {})["UDim2"] = udim2.to_dict()
            return self.root, self.workspace
    def AddPropertyBrickColor_shorthand(self, FullPropertyName, CallMethod):
        if CallMethod:
            script = Script(self.GetInstance(), self.root, f"BrickColor_{FullPropertyName}")
            script.CreateInstance()
            script.CreatePropertiesSection()
            if CallMethod == cm.BrickColor_Shorthanded.Red:
                script.AddCode(f"""
script.Parent.{FullPropertyName} = BrickColor.Red()
                """)
            elif CallMethod == cm.BrickColor_Shorthanded.White:
                script.AddCode(f"""
script.Parent.{FullPropertyName} = BrickColor.White()
                """)
            elif CallMethod == cm.BrickColor_Shorthanded.Gray:
                script.AddCode(f"""
script.Parent.{FullPropertyName} = BrickColor.Gray()
                """)
            elif CallMethod == cm.BrickColor_Shorthanded.DarkGray:
                script.AddCode(f"""
script.Parent.{FullPropertyName} = BrickColor.DarkGray()
                """)
            elif CallMethod == cm.BrickColor_Shorthanded.Black:
                script.AddCode(f"""
script.Parent.{FullPropertyName} = BrickColor.Black()
                """)
            elif CallMethod == cm.BrickColor_Shorthanded.Yellow:
                script.AddCode(f"""
script.Parent.{FullPropertyName} = BrickColor.Yellow()
                """)
            elif CallMethod == cm.BrickColor_Shorthanded.Green:
                script.AddCode(f"""
script.Parent.{FullPropertyName} = BrickColor.Green()
                """)
            elif CallMethod == cm.BrickColor_Shorthanded.Blue:
                script.AddCode(f"""
script.Parent.{FullPropertyName} = BrickColor.Blue()
                """)
            elif CallMethod == cm.BrickColor_Shorthanded.Random:
                script.AddCode(f"""
script.Parent.{FullPropertyName} = BrickColor.Random()
                                """)
            self.PropsTable.setdefault(FullPropertyName, {})["BrickColor"] = CallMethod
            return self.root, self.workspace

    def AddHexPropertyColor3(self, FullPropertyName, hexValue):
        if hexValue:

            script = Script(self.GetInstance(), self.root, f"Color3_{FullPropertyName}")
            script.CreateInstance()
            script.CreatePropertiesSection()
            r,g,b = int(hexValue[0:2], 16), int(hexValue[2:4], 16), int(hexValue[4:6], 16)
            script.AddCode(f"""
script.Parent.{FullPropertyName} = Color3.fromRGB({r},{g},{b})
            
            """)
    @property
    def GetAllSetProperties(self):
        return self.PropsTable

    @property
    def Instance(self):
        return self.CreatedInstance

    @property
    def Parent(self):
        return self.workspace
    @property

    def InstanceContent(self):
        return ET.tostring(self.CreatedInstance)

    def AddPropertyVector3(self, FullPropertyName, vector3: Vector3):
        if vector3:
            x, y, z = vector3.x, vector3.y, vector3.z
            script = Script(self.GetInstance(), self.root, f"Vector3_{FullPropertyName}")
            script.CreateInstance()
            script.CreatePropertiesSection()
            script.AddCode(f"""
script.Parent.{FullPropertyName} = Vector3.new({x},{y},{z})
            """)
            self.PropsTable.setdefault(FullPropertyName, {})["Vector3"] = vector3.to_dict()
        return self.root, self.workspace

    def AddPropertyCFrame(self, FullPropertyName, cFrame: CFrame):
        if cFrame:
            x, y, z, r00, r01, r02, r10, r11, r12, r20, r21, r22 = cFrame.X, cFrame.Y, cFrame.Z,cFrame.r00,cFrame.r01,cFrame.r02,cFrame.r10,cFrame.r11,cFrame.r12,cFrame.r20,cFrame.r21,cFrame.r22
            script = Script(self.GetInstance(), self.root, f"CFrame_{FullPropertyName}")
            script.CreateInstance()
            script.CreatePropertiesSection()
            script.AddCode(f"""
script.Parent.{FullPropertyName} = CFrame.new({x, y, z, r00, r01, r02, r10, r11, r12, r20, r21, r22})
            """)
            self.PropsTable.setdefault(FullPropertyName, {})["CFrame"] = cFrame.to_dict()
        return self.root, self.workspace

    def AddPropertyVector2(self, FullPropertyName, vector2: Vector2):
        if vector2:
            x, y = vector2.x, vector2.y
            script = Script(self.GetInstance(), self.root, f"Vector3_{FullPropertyName}")
            script.CreateInstance()
            script.CreatePropertiesSection()
            script.AddCode(f"""
script.Parent.{FullPropertyName} = Vector2.new({x},{y})
            """)
            self.PropsTable.setdefault(FullPropertyName, {})["Vector3"] = vector2.to_dict()
        return self.root, self.workspace

    def GetInstance(self):
        return self.CreatedInstance


class Service:

    def __init__(self, FullName, root):
        self.name = FullName
        self.root = root
        self.Num: int = 0
        self.__Service__ = None

    def CreateService(self):
        self.Num = random.randint(93293, 4289823)
        service = ET.SubElement(self.root, "Item")
        service.set("class", self.name)
        service.set("referent", f"RBX{self.Num}")
        properties = ET.SubElement(service, "Properties")
        ET.SubElement(properties, "string", name="Name").text = self.name
        self.__Service__ = service
        return self.root, service

    def GetService(self):
        return self.__Service__

    @property
    def ServiceContent(self):
        return ET.tostring(self.__Service__)

    @property
    def Service(self):
        return self.__Service__


class Place:
    def __init__(self, Name):
        self.name = Name
        self.Num = 0
        self.Workspace = None
        self.root = None
        self.StarterPlayer = None
        self.StarterCharacterScripts = None
        self.StarterPlayerScripts = None
    def init(self):
        # create the root element
        root = ET.Element("roblox")
        root.set("version", "4")
        # create the Workspace item
        workspace = ET.SubElement(root, "Item")
        workspace.set("class", "Workspace")
        workspace.set("referent", f"RBX{self.Num}")
        properties = ET.SubElement(workspace, "Properties")
        ET.SubElement(properties, "string", name="Name").text = "Workspace"
        # create the StarterPlayer item
        starter_player = ET.SubElement(root, "Item")
        starter_player.set("class", "StarterPlayer")
        starter_player.set("referent", f"RBX{self.Num + 1}")
        properties = ET.SubElement(starter_player, "Properties")
        ET.SubElement(properties, "string", name="Name").text = "StarterPlayer"

        # create the StarterCharacterScripts item
        starter_character_scripts = ET.SubElement(starter_player, "Item")
        starter_character_scripts.set("class", "StarterCharacterScripts")
        starter_character_scripts.set("referent", f"RBX{self.Num + 2}")
        ET.SubElement(starter_character_scripts, "Properties")

        # create the StarterPlayerScripts item
        starter_player_scripts = ET.SubElement(starter_player, "Item")
        starter_player_scripts.set("class", "StarterPlayerScripts")
        starter_player_scripts.set("referent", f"RBX{self.Num + 3}")
        ET.SubElement(starter_player_scripts, "Properties")
        self.StarterPlayer = starter_player
        self.StarterPlayerScripts = starter_player_scripts
        self.StarterCharacterScripts = starter_character_scripts
        self.Num += 4
        self.root = root
        self.Workspace = workspace
        self.Num += 1
        self.root = root
        self.Workspace = workspace

    def AddInstance(self, InstanceFullName, Parent):
        inst = Instance(InstanceFullName, Parent, self.root)
        inst.CreateInstance()
        inst.CreatePropertiesSection()
        self.root = inst.root
        return inst

    def AddScript(self, Parent, Name, code):
        inst = Script(Parent, self.root, Name)
        inst.CreateInstance()
        inst.CreatePropertiesSection()
        inst.AddCode(code)
        self.root = inst.root
        return inst
    def AddLocalScript(self, Parent, Name, code):
        inst = LocalScript(Parent, self.root, Name)
        inst.CreateInstance()
        inst.CreatePropertiesSection()
        inst.AddCode(code)
        self.root = inst.root
        return inst

    def AddService(self, Name):
        serv = Service(Name, self.root)
        serv.CreateService()
        return serv

    def exec(self, code):
        script = self.AddInstance("Script", self.Workspace)
        script.AddProperty("Disabled", "bool", False)
        script.AddProperty("LinkedSource", "Token", "")
        script.AddProperty("Name", "string", random.randint(24, 23493248947))
        script.AddProperty("Source", "ProtectedString", code)
        return script

    @property
    def PlaceContent(self):
        return ET.tostring(self.root)

    @property
    def PlaceRoot(self):
        return self.root

    @property
    def WorkspaceContent(self):
        return ET.tostring(self.Workspace)

    def Tree_Write(self):
        tree = ET.ElementTree(self.root)
        tree.write(f"{self.name}.rbxl", encoding="UTF-8", xml_declaration=True)
    def Open_In_Studio(self):
        try:
            os.system("taskkill /im RobloxStudioBeta.exe /f")
            time.sleep(1)
            os.system(f'{self.name}.rbxl')
        except Exception as error:
            raise OpenProjectFail(error)
'''
# Docs: Usage
place = Place("wreer")  # Creates a rbxl place XML file with the name "Test"
place.init()  # Initializes the place file, setting up some settings and creating workspace.
ServerScriptService = place.AddService("ServerScriptService")
print(ServerScriptService.ServiceContent)
script = place.AddScript(ServerScriptService.GetService(), "ServerScript", """
print('Hello From ServerScriptService '..script.Parent.Name..'!!')
wait(1)
print("LOL")
""")

print(script.InstanceContent)
print(place.PlaceContent)  # Prints the generated XML file.
place.Tree_Write()  # writes the place XML to the file.
'''