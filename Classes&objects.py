class robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    
    def introduce(self):
        print("Hi! My name is "+self.name)

class person:
    def __init__(self, pname, attitude, sitdown):
        self.pname = pname
        self.attitude = attitude
        self.sitdown = sitdown
    
    def is_sitting(self):
        if self.sitdown == True:
            print(self.pname+"! Please Stand up")
        else:
            print(self.pname+"! Please Sit down")

r1 = robot("tom", "blue", 40)
r1.introduce()
p1 = person("alice", "aggressive", False)
p1.is_sitting()

p1.ownRobot = r1
p1.ownRobot.introduce()