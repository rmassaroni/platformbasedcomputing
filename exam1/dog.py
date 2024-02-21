class dog:

    def __init__(self, name, trick, breed, hungry=True):
        self.name = name
        self.trick = trick
        self.breed = breed
        self.hungry = hungry

    def __str__(self):
        return name + ":" + breed

    def speak(self):
        print("Woof")

    def feed(self):
        self.hungry = false

    def change_trick(self, newtrick):
        self.trick = newtrick

    def get_name(self):
        return self.name

    def get_breed(self):
        return self.breed

    def get_trick(self):
        return self.trick

    def isHungry(self):
        return self.hungry


dogfile = open("dogs.txt")
doglist = {}
s = dogfile.readline().split()
doglist[0] = dog(s[0],s[1],s[2],s[3])
##print(doglist[0])
s = dogfile.readline().split()
doglist[1] = dog(s[0],s[1],s[2],s[3])
##print(doglist[1])
s = dogfile.readline().split()
doglist[2] = dog(s[0],s[1],s[2],s[3])
##print(doglist[2])
s = dogfile.readline().split()
doglist[3] = dog(s[0],s[1],s[2],s[3])
##print(doglist[3])
s = dogfile.readline().split()
doglist[4] = dog(s[0],s[1],s[2],s[3])
##print(doglist[4])
