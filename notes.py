myDictionary = {
  "name": "Ian",
  "health": 219,
  "strength": 199,
  "equipped": "Axe"
}

#it will only print the variables
# for i in myDictionary:
#   print(i)

# following will return variable also what data in it
# for i, x in myDictionary.items():
#   print(f"{i} : {x}")
"""
above is the way to use for loop in order to access every element with 
respect to it's value
first we write a for loop followed by creating two new variable and then
methening the dict veriable name and follwed by items function

then printring the both two valriable simultaneously
name : Ian
health : 219
strength : 199
equipped : Axe`
"""

#following will return data of the variable
myDictionary = {
  "name": "Ian",
  "health": 219,
  "strength": 199,
  "equipped": "Axe"
}

#to accesss the data in the variable of dict we have to use .values()
# for value in myDictionary.values():
# print(value)

myDictionary = {
  "name": "Ian",
  "health": 219,
  "strength": 199,
  "equipped": "Axe"
}

# for name,value in myDictionary.items():
#   print(f"{name}:{value}")

#   if (name == "strength"):
#     print("Whoa, SO STRONG!")

myDictionary = {
  "name": "David the Mildy Terrifying",
  "health": 186,
  "strength": 4,
  "equipped": "l33t haxx0r p0werz"
}

# for name, value in myDictionary.items():
#   print(f"{name}:{value}")

# if (name == "strength"):
#   if value > 100:
#     print("Whoa, SO STRONG")
#   else:  # it will print else becase in if condition check it's corresponding values
#     #when it come in dicts
#     print(
#         "Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!"
#     )

myDictionary = {
  "name": "Ian",
  "health": 219,
  "strength": 199,
  "equipped": "Axe"
}

# for name, x in myDictionary.items():
#   print(f"{name} {x}")
"""
to add both the values to our loop we have to creat two variable 
in for loop and after specifying the dict we have to use items fucntion to access 
evey element in dict

name Ian
health 219
strength 199
equipped Axe

"""

myDictionary = {
  "name": "David the Mildy Terrifying",
  "health": 186,
  "strength": 4,
  "equipped": "l33t haxx0r p0werz"
}

# for name, value in myDictionary.items():
#   print(f"{name}:{value}")
#   if (name == "strength"):
#     if value < 100:
#       print(
#           "Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!"
#       )
#     else:
#       print("whoa, so strong")

myDictionary = {
  "name": "David the Mildy Terrifying",
  "health": 186,
  "strength": 4,
  "equipped": "l33t haxx0r p0werz"
}

for name, x in myDictionary.items():
print(f"{name}:{x}")

if (name == "strength"):
  if x > 100:
    print("Whoa, SO STRONG")
  else:
    print(
        "Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!"
    )
