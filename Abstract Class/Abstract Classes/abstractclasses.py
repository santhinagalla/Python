from abc import ABC, abstractmethod, abstractproperty

class Movable(ABC):
	@abstractmethod
	def move(self): 
	    pass
		
class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Part(Displayable):
    def __init__(self,partNo,price):
        self.__partNo = partNo
        self.__price = price  

    @property
    def partNo(self):
        return self.__partNo
    
    @partNo.setter
    def partNo(self):
        self.__partNo = partNo

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self):
        self.__price = price
    
    def display(self):
        print("partno = ",self.partNo,"\nprice=",self.__price)

    def __str__(self):
        return "partno = {partno}\nprice = {price}".format(partno = self.__partNo,price = self.__price)

class MovablePart(Part,Movable):
    def __init__(self,partNo,price,type):
        self.__type = type
        Part.__init__(self,partNo,price)
        
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self):
        self.__type = type
    
    def display(self):
        Part.display(self)
        print("type = ",self.__type)

    def __str__(self):
        return "type= {type}".format(type=self.__type)

    def move(self):
        print("PartNo:",self.partNo,"is moving fast!")
    
class JetFighter(Displayable,Flyable):
    def __init__(self,model,speed):
        self.__model = model
        self.__speed = speed
    
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self):
        self.__model = model

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self):
        self.__speed = speed
        
    def fly(self):
        print("model =", self.__model,"\nspeed =",self.__speed)

    def __str__(self):
        return "model = {model}\nspeed = {speeed}".format(model= self.__model,speed=self.__speed)

class Machine(Displayable):
    def __init__(self,machineName):
        self.__machineName = machineName
        self.__parts = []

    @property
    def machineName(self):
        return self.__machineName

    @machineName.setter
    def machineName(self):
        self.__machineName = machineName

    @abstractmethod
    def dowork(self):
        pass

    @abstractmethod
    def addPart(self,part):
        pass

    @abstractmethod
    def removePart(self,partNo):
        pass

    def findDuplicatedPart(self):
        dict = {}
        for part in self.__parts:
            if part.partNo not in dict.keys():
                dict[part.partNo] = 1
            else:
                dict[part.partNo] += 1
        
        for key in list(dict):
            if dict[key] <= 1:
                dict.pop(key)
                #del dict[key]
        return dict    
            
    def display(self):
        print("machine name =",self.__machineName)
        print("The machine has these parts:")
        for part in self.__parts:
            part.display()
            print()
        
class Robot(Machine,JetFighter):
    def __init__(self, machineName,cpu, model, speed):
        self.__cpu = cpu
        Machine.__init__(self,machineName)
        JetFighter.__init__(self,model,speed)

    @property
    def cpu(self):
        return self.__cpu
    
    @cpu.setter
    def cpu(self):
        self.__cpu = cpu

    def addPart(self,part):
        self._Machine__parts.append(part)

    def getExpensiveParts(self,priceLimit):
        temp_list = []
        for part in self._Machine__parts:
            if part.price >= priceLimit:
                temp_list.append(part)
        return temp_list
   
    def getMovableParts(self):
        temp_list = []
        for movablepart in self._Machine__parts:
            if type(movablepart) is MovablePart:
                temp_list.append(movablepart)
        return temp_list

    def getMovablePartsByType(self):
        dict = {}
        for part in self._Machine__parts:
            if type(part) is MovablePart:
                if part.type not in dict:
                    dict[part.type] = []
                dict[part.type].append(part)
        return dict    
           
    def fly(self):
        print("The JetFigher",self.model,"is flying over the ocean!")
        print("The Robot",self.machineName, "is flying over the ocean!")

    def dowork(self):
        print("The Robot", self.machineName,"is assembling a big truck.")
    
    def removePart(self,partNo):
        print("Remove element")
        temp_list = [part for part in self._Machine__parts if part.partNo != partNo]
        self._Machine__parts = temp_list

    def display(self):
        print("cpu =",self.__cpu)
        Machine.display(self)
        JetFighter.fly(self)

def main():
    
    robo = Robot('MTX', 'M1X', 'F-16', 10000)
    robo.addPart(Part(111, 100))
    robo.addPart(Part(222, 200))
    robo.addPart(Part(333, 300))
    robo.addPart(Part(222, 300))
    robo.addPart(MovablePart(555, 300, "TypeA"))
    robo.addPart(Part(111, 100))
    robo.addPart(Part(111, 100))
    robo.addPart(MovablePart(777, 300, "TypeB")) 
    robo.display()
    print()
    
    print("\nRobot test flight----")
    robo.fly()

    print("\nDuplicated part list----")
    partFreq = robo.findDuplicatedPart()
    for partNo in partFreq.keys():
        print(partNo,'=>',partFreq[partNo], 'times')

    print("\nExpensive part list----")
    expensiveParts = robo.getExpensiveParts(200)
    for part in expensiveParts:
        part.display()

   
    print("\nMovable part list----")
    movableParts = robo.getMovablePartsByType()
    for type, parts in movableParts.items():
        print("type =", type)
        for part in parts:
            part.display()
        print()

    print("\nAsk movable to move----")
    movableParts = robo.getMovableParts()
    for part in movableParts:
        part.move()

main()