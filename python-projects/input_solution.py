# input() will read in string
# it can also display a prompt if given one
num=input("Enter a number")
print(num)

# if user does not enter a number an exception will be thrown. 
# use try/except
try:
    num=int(input("Enter a number: "))
    print(num)
    sum=num+2
except:
    print("you did not enter a number")

# Different ways to use print
name = "Jane"
greeting = "How are you?"
# use a comma to output each string separated by a space
print("Hello", name, greeting)
# use + to concatenate
print("Hello " + name + " " + greeting)
# embed variables and expressions in f-string
print(f"Hello {name}! {greeting}")
age = 14
print(f"{name} can vote in {18-age} years")

# use the end paramater to change what is printed after each statement
# a new line is the default
lst = [1,2,3,4,5]
for val in lst:
    print(val, end = " ")

# open file and store each line in a list called file
with open("movies.txt") as file:
    for line in file:
        # strip off the end line
        print(line.strip())

with open("heights.txt") as file:
    for line in file:
        # strip off end of line
        stripped_line=line.strip()
        # split each word separated by a space and store in the list tokens
        tokens = stripped_line.split()
        print(tokens)
        print(tokens[0], ' ', tokens[1], 'is', tokens[2], 'inches tall.')
        