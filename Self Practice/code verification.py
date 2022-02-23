"""
This file is meant to test functions/code to make sure that they work as intended,
it will not be added upon, but rather constantly deleted and updated, do not push
"""

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 

print(myfamily)

myfamily["child3"]["name"] = "Robert"

print(myfamily)
