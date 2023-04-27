from RobloxPyApi3.Errors import InvalidVariableUsage,FunctionValueFailure
import RobloxPyApi3.Place.CallMethods as CallMethods
gameobject = "game"
class ServiceValue:
    def __init__(self,Service:CallMethods.RobloxService):
        self.Service = Service
    @property
    def _ValueFull(self):
        return str(f"game:GetService('{self.Service.value}')")
    def __str__(self):
        return str(self._ValueFull)
class _Variable:
    def __init__(self,Var,Value):
        self.Name = Var
        self.Value = Value
    def __str__(self):
        if isinstance(self.Value,bool):
            if self.Value == True:
                self.Value = 'true'
            else:
                self.Value = 'false'
        elif isinstance(self.Value,str):
            self.Value = f"'{self.Value}'"
        return str(f"local {self.Name} = {self.Value}")
class _SetterVariable:
    def __init__(self,Var,Value):
        self.Name = Var
        self.Value = Value
    def __str__(self):
        if isinstance(self.Value,bool):
            if self.Value == True:
                self.Value = 'true'
            else:
                self.Value = 'false'
        elif isinstance(self.Value,str):
            self.Value = f"'{self.Value}'"
        return str(f"{self.Name} = {self.Value}")
class ModuleFunctionValue:

    def __init__(self,module_class,function_name,args):
        self.module_class = module_class
        self.function_name = function_name
        self.args = args
    def __str__(self):
        return _ModuleFunctionValue(module_class=self.module_class,function_name=self.function_name,args=self.args)

def _ModuleFunctionValue(module_class, function_name, args):
    try:
        if args == "":
            return f"{module_class}:{function_name}()"
        #module, class_name = str(module_class).split('.')
        arg_str = ','.join(
            f"'{arg.lower()}'" if isinstance(arg, str) else
            'true' if arg is True else
            'false' if arg is False else
            str(arg)
            for arg in args)
        return f"{module_class}:{function_name}({arg_str})"
    except Exception as error:
        raise FunctionValueFailure(f"Failed to compile into a string. Make sure all arguments are right. Got : {module_class} , {function_name}, {args}, Exception: {error}")
class FunctionValue:

    def __init__(self,function_name,args):
        self.function_name = function_name
        self.args = args
    def __str__(self):
        return _FunctionValue(function_name=self.function_name,args=self.args)
class ObjectValue:

    def __init__(self,*args):
        self.ag = args
    def __str__(self):
        result = ""
        for item in self.ag:
            if result == "":
                result = item
            else:
                result = f'{result}.{item}'
        return result
class CustomValue:
    def __init__(self,value):
        self.ag = value
    def __str__(self):
        return self.ag
def _FunctionValue(function_name, args):
    try:
        if args == "":
            return f"{function_name}()"
        #module, class_name = str(module_class).split('.')
        arg_str = ','.join(
            f"'{arg.lower()}'" if isinstance(arg, str) else
            'true' if arg is True else
            'false' if arg is False else
            str(arg)
            for arg in args)
        return f"{function_name}({arg_str})"
    except Exception as error:
        raise FunctionValueFailure(f"Failed to compile into a string. Make sure all arguments are right. Got :  '{function_name}', '{args}', Exception: {error}")
def GetServiceName(ServiceEnum):
    return ServiceEnum.value
class LuaScript:
    def __init__(self):
        self.fullScript = ""
        self.Variables = {}
    def Variable(self,Varname:str,Value):
        if ' ' in Varname:
            raise InvalidVariableUsage(f"Variable '{Varname}' cannot contain spaces.")
        else:
            Var = _Variable(Varname,Value)
            if Var:
                if not isinstance(Value,bool):
                    if not str(Value).isdigit():
                        if isinstance(Value,ServiceValue):

                            self.Variables[Varname] = str(Value)
                        elif isinstance(Value,ModuleFunctionValue):

                            self.Variables[Varname] = str(Value)
                        elif isinstance(Value,CustomValue):

                            self.Variables[Varname] = str(Value)
                        elif isinstance(Value,FunctionValue):

                            self.Variables[Varname] = str(Value)
                        elif isinstance(Value,ObjectValue):

                            self.Variables[Varname] = str(Value)
                        else:
                            self.Variables[Varname] = str(f"'{Value}'")

                    else:
                        self.Variables[Varname] = int(Value)
                else:
                    """
                    if Value == True:
                        self.Variables[Varname] = 'true'
                    else:
                        self.Variables[Varname] = 'false'
                    """
                    self.Variables[Varname] = bool(Value)
            self.fullScript = f"{self.fullScript}\n{Var}"
            return Varname
    def SetterVariable(self,Varname:str,Value):
        if ' ' in Varname:
            raise InvalidVariableUsage(f"Variable '{Varname}' cannot contain spaces.")
        else:
            Var = _SetterVariable(Varname,Value)
            if Var:
                try:
                    if self.Variables[Varname]:
                        #print("Exists")
                        if not isinstance(Value,bool):
                            if not str(Value).isdigit():
                                if isinstance(Value,ServiceValue):

                                    self.Variables[Varname] = str(Value)
                                elif isinstance(Value,ModuleFunctionValue):

                                    self.Variables[Varname] = str(Value)
                                elif isinstance(Value,CustomValue):

                                    self.Variables[Varname] = str(Value)
                                elif isinstance(Value,FunctionValue):

                                    self.Variables[Varname] = str(Value)
                                elif isinstance(Value,ObjectValue):

                                    self.Variables[Varname] = str(Value)
                                else:
                                    self.Variables[Varname] = str(f"'{Value}'")

                            else:
                                self.Variables[Varname] = int(Value)
                        else:
                            """
                            if Value == True:
                                self.Variables[Varname] = 'true'
                            else:
                                self.Variables[Varname] = 'false'
                            """
                            self.Variables[Varname] = bool(Value)
                    self.fullScript = f"{self.fullScript}\n{Var}"
                    return Varname
                except Exception as error:
                    #print(error)
                    return
    def Connect(self, Object:ObjectValue, event: str, connectargs = "",callback = None):
        if connectargs == "" or connectargs == None:
            script = f"{Object}.{event}:Connect(function()\n"
            script += f'{callback}\n'
            script += "end)\n"
            self.fullScript = f"{self.fullScript}\n{script}"
        else:
            arg_str = ','.join(
                f"'{arg.lower()}'" if isinstance(arg, str) else
                'true' if arg is True else
                'false' if arg is False else
                str(arg)
                for arg in connectargs)
            script = f"{Object}.{event}:Connect(function({arg_str})\n"
            script += f'{callback}\n'
            script += "end)\n"
            self.fullScript = f"{self.fullScript}\n{script}"
    def AddToScript(self,script):
        self.fullScript = f'{self.fullScript}\n{script}'
    def ConnectVoidFunction(self, Object:ObjectValue, event: str,functionName = ""):
        script = f"{Object}.{event}:Connect({functionName})"
        self.fullScript = f"{self.fullScript}\n{script}"
    def GetVariableName(self,Name):
        result = None
        Table = self.Variables
        #print(f"Items : {Table.items()}")
        for key,_ in Table.items():
            if key == Name:
                result = key
        return result
    def CallFunction(self, FunctionName, *Value):
        arg_str = ','.join(
            f"'{arg}'" if isinstance(arg, str) else
            str(arg).lower() if isinstance(arg, bool) else
            str(arg)
            for arg in Value)
        script = f"{FunctionName}({arg_str})"
        self.fullScript = f"{self.fullScript}\n{script}"
    def CallModuleFunction(self,module_class ,FunctionName, *Value):
        arg_str = ','.join(
            f"'{arg}'" if isinstance(arg, str) else
            str(arg).lower() if isinstance(arg, bool) else
            str(arg)
            for arg in Value)
        script = f"{module_class}:{FunctionName}({arg_str})"
        self.fullScript = f"{self.fullScript}\n{script}"
    @property
    def GetFullScript(self):
        return self.fullScript
    def __str__(self):
        return self.fullScript
