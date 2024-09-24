# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string 
magic = 'abracadabra'
# a. Retrieve the 5th character.
print(magic[4])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
print(magic.find("c"))

# Advanced Slicing:
# Given the string 
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[0:13:2])
# c. Reverse the entire string using slicing.
print(alphabet[::-1])

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the 
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy "
print(quote.find("John F. Kennedy "))
print(quote[83:-1])

# Manipulating Words:
# Given the string 
info = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
print(info.find(' subjective'))
print(info[36:46])
# b. Extract every third word.
#split tetx ubto words
words = info.split() #list
#extract every 3rd word
every_3rd_word=words[::3]
#join words inyo a string
result=' '.join(every_3rd_word)
print(result)
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
split_info=['python' , 'is' , 'fun']
print(split_info[::-1])

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: 
force="MAY THE FORCE BE WITH YOU."
print(force.lower())

# String Joining and Splitting:
# Given the list motto 
listone= ["Make", "haste", "slowly."]
# a. Convert the list into a single string.
together_listone=" ".join(listone)
print(together_listone)
# b. Now, split the string at every occurrence of the letter 'a'.
split_listone=together_listone.split("a")
print(split_listone)

# Replacing Words:
# Modify the sentence: 
life="Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
print(life.replace("busy" , "distracted"))
# b. Replace "plans" with "mistakes".
print(life.replace("plans" , "mistakes"))

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word 
rep="Iteration" 
rep="Iteration"*7
print(rep)

# Word Search:
# Check if the word "moonlight" appears in the quote: 
qoute2="With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
qoutemoon=False
print("The qoute has the word moonlight?"+str(qoutemoon))

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the 
phrase="Supercalifragilisticexpialidocious"
print(phrase.find("Supercalifragilisticexpialidocious"))

# b. Count the number of times the letter 'i' appears in the same word/phrase.
print(len(phrase))