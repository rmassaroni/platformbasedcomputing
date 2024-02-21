print("hello world")


# LOOPS
nums = [10,20,30,40,50]

for i in range(len(nums)):
    print(nums[i])

for val in nums:
    val += 5
    print(val)
print(nums)

for i, val in enumerate(nums):
    print("i is", i, "and val is",val)

dogs = ["boomer","rocky","daisy"]

nums = [1,2,3,4,5]
sum_nums=0
for num in nums:
    sum_nums += num
print("sum of nums is", sum_nums)
print(f"the sum of nums is {sum_nums}")


# FUNCTIONS
def hello(name = "friend"):
    print("hello!", name)

hello("Bob")
hello()     




# STRINGS
name = 'Robert Massaroni'
print("She's a great dancer.")
#print('She's a great dancer.') #does not work

subtotal = 14.75
subtotle_statement = 'The subtotal is ' + str(subtotal) #cast to string

#name = 'Robert' + ' ' + 'Massaroni'

firstChar = name[0]
lastChar = name[-1]

print('Python' * 7)
hashtags = 15 * '#'
print(hashtags)

if name == 'Robert Massaroni':
    print("yes")
if name != 'Robert Massaroni':
    print("no")

name_in_uppercase = name.upper()
print(name_in_uppercase)

fullname = "Robert Massaroni"
firstname = fullname[0:6]
lastname = fullname[7:-1] #? wont work
print(lastname)
lastname = fullname[7:16]
print(lastname)




nums = [0,3,8,5,4]
temp = nums[2]
nums[2] = nums[-1]
nums[-1] = temp
print(nums)
