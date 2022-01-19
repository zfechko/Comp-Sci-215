# practicing defining a function by making a simple add function
def add(x, y):
    print(x + y)

add(2.5, 3.8)

# practicing defining and accessing a list
practice_list = ["zach", "elliot", "josh"]
practice_list2 = ["fechko", "kimsey", "maloy"]


practice_list.append("noah") # funtions like a push_back for C++ vectors
practice_list2.append("frachon")

practice_list.extend(practice_list2) # concatenates two lists by appending practice_list2 to the end of practice_list

# practicing taking user input

name = input("What is your name? ")
print("Nice to meet you", name)

# taking multiple inputs
num_array = [int(x) for x in input("Enter some numbers").split()] #this formatting makes it so you don't have to use numerous lines to accomplish the same task
print(num_array)

#practicing making a function with an arbitrary amount of arguments
def arbitrary_add(*nums):
    sum = 0
    for x in range(len(nums)): # functions with arbitrary arguments use tuples as a list so use tuple syntax and not a list
        sum += nums[x]
    print(sum)

arbitrary_add(1, 2, 3)