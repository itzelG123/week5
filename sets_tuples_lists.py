# #colection=single "variable"used to store multiplr values
# #list =[] ordered and changeable. Duplicates OK
# #set ={}unordered and immutable, but add/remove OK NO duplicates
# #Tuple=()ordered and unchangeable Duplicates OK Faster

# fruits=["apple","orange", "banana", "coconut", "mango","kiwi","strawberry"]
# # print(fruits[0])   #0=apple
# # print(fruits[0:3]) 
# # print(len(fruits))#find lengths
# # print(fruits[::2])#every 2
# # print(fruits[::-1])#makes it backwards

# for fruit in fruits:
#     print(fruit)
#     #iteration
#     #DONT HAVE ONE LETTER VARIABLE
#     #fruit represent object to list 
#     #iteration is lopping thoughthe whole thing
# #will loop through each tine
#     #iteration 1-fruit=apple
#     #iteration 2-fruit=orange

#    # print(dir(fruits))
#     #gives all attributes for a list 

#     #print(help(fruits))
#     #gives manual of all the things you could do with lists,help with documentation

#     print(len(fruits)) #givews you length

#     print("apple"in fruits) #tells you if ot there
#     print("pineapple"in fruits)

#     fruits[1]="pineapple"
#     #changes the value of 0 in the list

#     fruits.append("watermelon")#adds things to the end of a list

#     fruits.remove("apple")#removes element

#     fruits.instert(0, "pineapple") #inserts varuable in the spot AND pushes the other variable

#     fruits.sort()#aplabethical order
#     fruits.reverse()#reverse

#     fruits.clear #all elemnts are gone/cleared
# print(fruits.index("apple")) #find the location/index


# cars=["ford","volvo","BMW","cadallic","chevy"]
# #add cars
# cars.append("honda")
# #print list in a f string
# print(f"The cars in the list are: {cars}")

# #replace last element in list
# cars[-1]="austin martin"

# #print out list of all cars in an f stirng 
# print(f"The cars in the list are: {cars}")
# #replace 3rd elemt with other car
# cars[2]="Genesis"
# print(f"The cars in the list are: {cars}")
# #remove 3rd in list 
# cars.remove("BMW")



# for car in cars:
#     requestCar=input("Enter a car:")


    #########SETS##########
    #sets are unordered and unindexed
    #thye are defined using curly brackets
    #they do not allow duplicates
    #{}sets
    #[]lists
# fruits={"apple","banana","mango","cherry","watermelon"}
# print(fruits)
# # print(dir(fruits))#methods/attrubiutes that can used with sets
# # print(help(fruits))#documentation/methods that can used with sets
# print(len(fruits))#number 9of elements in the set
# print("volvo"in fruits)#check if an element is in the set
# #add eleemnt to set
# print(fruits.add("orange"))
# print(fruits)
# print(fruits.add("kiwi"))
# print(fruits)

# #add mupltie things to set
# print(fruits.update(["organe","kiwi","pineapple"]))
# print(fruits)

# #remove element from set
# print(fruits.remove("banana"))
# print(fruits)
# print(fruits.pop())#removes last eleemnt in set
# print(fruits)
# print(fruits.clear())#clears set
#sets are useful when you want to store a collection of items that shouldnt be changed and you dont care about the order of item
#ex-a colection of uniuqe items

# social_security_number={123456789,987654321,123456789}
# #remvoe last element in set
# print(social_security_number.pop())
# print(social_security_number)
# #add nother ss number 
# print(social_security_number.add(246810))
# print(social_security_number)
# print(social_security_number.add(296698574))
# print(social_security_number)

#######tuples######
#tuples are immutable and are defined using parathesis
#create an extra tuple called mu_tuple with the values:
example_tuple=(1,2,3,4,5,6,7,8,9,10)
print(example_tuple)
print(example_tuple.count(2))#count the number of times
# #the vaule 2 appeaes in the tuple
# print(dir(example_tuple))#attributes that can be used with tuples
# print(help(example_tuple))#docuemntation/methods that can used in tuples
# print(len(example_tuple))#number of elemnts in tuplke
# print(2 in example_tuple)#check if elemnt is in tuple

#thye are useful when you wnat to store a collection of items that shoundt be changed such as days pf the week months of the year etc.If you wnat to find the index of a value in a tuple
# print(example_tuple.index(2))
# lymeric="ptetr pipe picked a peck of puckled peppers peppers"
# #convert string to a tuple
# #split it first
# lymeric_tuple=tuple(lymeric.split())
# print(lymeric_tuple)
# #find hoe many times the word peck appears in tuple
# print(lymeric_tuple.count("peppers"))


#loops with tupkes
# for item in example_tuple:
#     print(item)


    ########dictionarys#######
    #dictionares aee unordered,changeable,and indexed
    #they aew defined using curly brackets
    #they have keys and valyes
    #a collection of {key:value} pairs,no duplicates
    #keys are uniques
    #values can be of any data type
    capitals={"kenya":"Nairobi",
             "Uganda":"Kampala",
             "Tanzania":"Dodoma",
             "Rwanda":"Kingali",
             "China":"beijing",
             "USA":"DC"}
    print(capitals)
    # print(dir(capitals))#attributes used in dictprines
    # print(help(capitals))#documentation methods used in dictonaries
    # print(len(capitals))#number of items in a dictonary
    # #if tou want to check value of a key in the dictionary
    print(capitals["kenya"])
    print(capitals.get("kenya"))
    #add an item to the dictonairy # 2ways\
    capitals["south africa"]="Pretoria"
    print(capitals)
    capitals.update({ "Nigeria":"Abuja"})
    #add 3 more countires and thier captials 

capitals.update({ "Germany":"Berlin"})
print(capitals)

capitals.pop("china")#remove an item from the dictionary
print(capitals)
#clear dictonary
#capitals.clear()#donot run thsi
#loop through dictonary
for key in capitals:
    print(key)
    print(f"these are the{key}")

    #print values in dcitonary
for value in capitals.values():
    print(value)

    #print the key value pairs in the dictonary 
    items_all=capitals.items()#key vaules pairs
    for key, value in items_all:
        print(f"{key}is the capital of {value}")