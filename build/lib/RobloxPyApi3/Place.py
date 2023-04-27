import xml.etree.ElementTree as ET
import random
class ValueNotSet(Exception):
    pass
class Vector3:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
class Instance:
    def __init__(self,fullName,Parent,root):
        self.instance = fullName
        self.workspace = Parent
        self.CreatedInstance = None
        self.Props = None
        self.root = root
    def CreateInstance(self):
        part = ET.SubElement(self.workspace, "Item")
        part.set("class", self.instance)
        part.set("referent", f"RBX{random.randint(100,9999)}")
        properties = ET.SubElement(part, "Properties")
        self.Props = properties
        if part:
            self.CreatedInstance = part
            print(self.CreatedInstance)
            properties = ET.SubElement(self.CreatedInstance, "Properties")
            self.Props = properties
        else:
            print("None")
        return self.root, self.workspace
    def CreatePropertiesSection(self):
        properties = ET.SubElement(self.CreatedInstance, "Properties")
        self.Props = properties
    def AddPropertyVector3(self,FullPropertyName,vector3:Vector3):
        if vector3:
            vector3_property = ET.SubElement(self.Props, "Vector3", name=FullPropertyName)
            ET.SubElement(vector3_property, "X").text = str(vector3.x)
            ET.SubElement(vector3_property, "Y").text = str(vector3.y)
            ET.SubElement(vector3_property, "Z").text = str(vector3.z)
        else:
            raise ValueNotSet("Value was not set, please set the vector3 value using Vector3(0,0,0) ")

        """
        ET.SubElement(self.Props, "string", name="Name").text = "MyPart"
        udim_position = ET.SubElement(self.Props, "UDim", name="Position")
        ET.SubElement(udim_position, "X").text = "0"
        ET.SubElement(udim_position, "Y").text = "0"
        udim_size = ET.SubElement(self.Props, "UDim", name="Size")
        ET.SubElement(udim_size, "X").text = "10"
        ET.SubElement(udim_size, "Y").text = "10"
        """
        return self.root, self.workspace
    def AddProperties(self,fullPropertyName,FullPropertyType,Value):
        # create the Part item
        FullVal = None
        if Value:
            if Value == True:
                FullVal = 'true'
            elif Value == False:
                FullVal = "false"
            else:
                FullVal = str(Value)

        else:
            raise ValueNotSet("Value was not set, please set the value")
        print(FullVal)
        # set the properties of the Part item

        ET.SubElement(self.Props, FullPropertyType, name=fullPropertyName).text = FullVal

        """
        ET.SubElement(self.Props, "string", name="Name").text = "MyPart"
        udim_position = ET.SubElement(self.Props, "UDim", name="Position")
        ET.SubElement(udim_position, "X").text = "0"
        ET.SubElement(udim_position, "Y").text = "0"
        udim_size = ET.SubElement(self.Props, "UDim", name="Size")
        ET.SubElement(udim_size, "X").text = "10"
        ET.SubElement(udim_size, "Y").text = "10"
        """
        return self.root, self.workspace
class Place:
    def __init__(self,Name):
        self.name = Name
        self.Num = 0
        self.Workspace = None
        self.root = None
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
        self.Num += 1
        self.root = root
        self.Workspace = workspace

    def AddInstance(self):
        inst = Instance("Part",self.Workspace,self.root)

        part,ws = inst.CreateInstance()
        inst.CreatePropertiesSection()
        inst.AddProperties("Anchored",'bool',True)
        inst.AddProperties("Name", 'string', "PyPartLolWorked")

        inst2 = Instance("Part", self.Workspace, self.root)
        part2, ws2 = inst.CreateInstance()
        inst2.CreatePropertiesSection()
        inst2.AddProperties("Anchored", 'bool', True)
        inst2.AddProperties("Name", 'string', "PyPartLolWorked22")
        print(ET.tostring(part2))
    def Tree_Write(self):
        tree = ET.ElementTree(self.root)
        tree.write(f"{self.name}.rbxl", encoding="UTF-8", xml_declaration=True)
    """
    def CreateInstance(self):
        # create the Part item
        part = ET.SubElement(self.Workspace, "Item")
        part.set("class", "Part")
        part.set("referent", "RBX1")

        # set the properties of the Part item
        properties = ET.SubElement(part, "Properties")
        ET.SubElement(properties, "bool", name="Anchored").text = "true"
        ET.SubElement(properties, "string", name="Name").text = "MyPart"
        udim_position = ET.SubElement(properties, "UDim", name="Position")
        ET.SubElement(udim_position, "X").text = "0"
        ET.SubElement(udim_position, "Y").text = "0"
        udim_size = ET.SubElement(properties, "UDim", name="Size")
        ET.SubElement(udim_size, "X").text = "10"
        ET.SubElement(udim_size, "Y").text = "10"
    """
place = Place("MyTestGame")
place.init()
place.AddInstance()