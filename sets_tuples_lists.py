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


cars=["ford","volvo","BMW","cadallic","chevy"]
#add cars
cars.append("honda")
#print list in a f string
print(f"The cars in the list are: {cars}")

#replace last element in list
cars[-1]="austin martin"

#print out list of all cars in an f stirng 
print(f"The cars in the list are: {cars}")
#replace 3rd elemt with other car
cars[2]="Genesis"
print(f"The cars in the list are: {cars}")
#remove 3rd in list 
cars.remove("BMW")



for car in cars:
    requestCar=input("Enter a car:")