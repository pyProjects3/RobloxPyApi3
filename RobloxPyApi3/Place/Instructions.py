from RobloxPyApi3.Place import * # Importing the base module and everything inside. It can also be "import Place" or "import Place as rbxplace" its up to you.
import RobloxPyApi3.Place.CallMethods as CallMethods # Importing the constants of the module.
MyPlace = Place("MyPlaceName")
# Creates the main Place class 'MyPlace'.
MyPlace.init()
# Creating Workspace and some Services that will be accessable.
# Note that only Workspace, StarterCharacter and all inside StarterCharacter. Aka StarterCharacterScripts and StarterPlayerScripts.
# All other Services need to be created to access them.
print(MyPlace.PlaceContent)
# Printing out the generated Roblox place file formatted in XML. RBXL in roblox.
print(MyPlace.WorkspaceContent)
# Printing out the Workspace XML item of the place. It will print every part in Workspace. all formatted in XML.
MyPart = MyPlace.AddInstance('Part',MyPlace.Workspace)
# Creating a part inside the workspace.
# Note that an Instance Name, aka the first argument should be a full name. Not 'part', "pARt" etc.
MyPart.AddProperty("Name",CallMethods.DefaultPropertyTypes.string,"MyBeautifulPart")
# Setting a string property 'Name' and setting its value to 'MyBeautifulPart'.
# Note that the CallMethod depends on a property. If its a string, its going to be 'CallMethods.DefaultPropertyTypes.string'
# Number value is going to be 'CallMethods.DefaultPropertyTypes.number', it can be double, float, int.
# A boolean value is going to be 'CallMethods.DefaultPropertyTypes.bool'.
MyPart.AddPropertyUDim2("Size",CallMethods.UDim2.new,UDim2(1,0,1,0)) # ->
MyPart.AddPropertyUDim2("Size",CallMethods.UDim2.fromscale,UDim2(1,1))
# Adding a UDim2 property. Both of these are right. Its the same thing. They are only setting the XScale and YScale.
MyPart.AddPropertyUDim2("Size",CallMethods.UDim2.new,UDim2(0,200,0,200)) # ->
MyPart.AddPropertyUDim2("Size",CallMethods.UDim2.fromoffset,UDim2(200,200))
# They are only setting the XOffset and YOffset.
MyPart.AddPropertyEnum("Material",Enum(["Enum",'Material','Grass']))
# Setting the Enum Material to 'Enum(["Enum",'Material','Grass'])' -> Enum.Material.Grass
inst = MyPart.GetInstance()
# Storing the full instance inside the inst variable,
# This will allow you to create another instance, and its parent is going to be : 'MyPart.GetInstance()' aka this part.
MyPart.AddPropertyCFrame("CFrame",CFrame(1,2,3)) # Setting the CFrame value 'CFrame' to 1,2,3. Aka 'CFrame.new(1,2,3)'
MyPart.AddPropertyVector3("Position",Vector3(32,0,32)) # Setting the Vector3 property 'Position' to 'Vector3.new(32,0,32)'
MyPart.AddPropertyBrickColor("Color",CallMethods.BrickColor.new,BrickColor("Pastel Blue")) # This one is special. It sets the brickcolor property to BrickColor.new("Pastel Blue")
# But, it got another way of using it:
MyPart.AddPropertyBrickColor_shorthand("Color",CallMethods.BrickColor_Shorthanded.Red)
# It 'AddPropertyBrickColor_shorthand' Uses shorthanded functions, aka void functions. You dont need to pass arguments in void functions.
MyPart.AddHexPropertyColor3("Color",0x3a8dcb) # Sets Color3 value 'Color' to a hex color value.
MyPart.AddPropertyColor3("Color",CallMethods.Color3.new,Color3(0,0,0)) # Sets Color3 value 'Color' to 0,0,0 aka 'Color3.new(0,0,0)' It got multiple CallMethod.