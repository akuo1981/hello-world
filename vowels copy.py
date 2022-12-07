# Automation onboarding
# Write a program to find the number of vowels and consonants in a given string.
# Vowels: a, e, i, o, u
import re

def vowels(input):
    #print (input)
    # define a list to store all vowels and all consonants
    vowelList = []
    consonantList = []

    # remove any special characters and space
    input2 = re.sub('[^\w]+|_', '', input)


    for i in range(len(input2)):
        #print(input[i])
        character = input[i]
        if input2[i] == 'a' or input2[i] == 'e' or input2[i] == 'i' or input2[i] == 'o' or input2[i] == 'u':
            vowelList.append(input2[i])
        else:
            consonantList.append(input2[i])

    print ("Vowels:", vowelList)
    print ("Consonant:", consonantList)


vowels('This is a beautiful world!')
