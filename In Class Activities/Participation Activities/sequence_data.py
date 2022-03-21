"""
Zach Fechko
Participation Activity #2
"""

# list_1 with 10 unique elements in the range (1 - 10), i.e. 1, 2, 3, 4,  5, 6, 7, 8, 19, 10 .
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_2 with 10 random elements between 5 and 20.
list_2 = [6, 10, 15, 8, 13, 12, 16, 5, 14, 9]

#create a list with elements combined from list_1 & list_2 using concatenation or append operations
combined_list = list_1 + list_2

print("Combined List: ", combined_list)

#create a dictionary object that mps each element of list_1 with corresponding element of list_2
dict_obj = {}

for x in range(len(list_1)):
    dict_obj[list_1[x]] = list_2[x]

print("Dictionary: ", dict_obj)

#create a tuple object with elements combined from list_1 & list_2
tuple_obj = ()
for x in combined_list:
    y = (combined_list[x],)
    tuple_obj += y

print("Tuple: ", tuple_obj)

#create a set object with all unique values of list_1 and list_2
set_obj = set(combined_list)
print("Set: ", set_obj)
