import dog

dogfile = open("dogs.txt")

##line = dogfile.readline()
##splitline = line.split()
##print(splitline[0])

doglist = {}

testdog = dog("1", "2", "2", True)

s = dogfile.readline().split()
d1 = dog(s[0],s[1],s[2],s[3])
s = dogfile.readline().split()
doglist[1] = dog(s[0],s[1],s[2],s[3])
s = dogfile.readline().split()
doglist[2] = dog(s[0],s[1],s[2],s[3])
s = dogfile.readline().split()
doglist[3] = dog(s[0],s[1],s[2],s[3])
s = dogfile.readline().split()
doglist[4] = dog(s[0],s[1],s[2],s[3])


print(doglist)

