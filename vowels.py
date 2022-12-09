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
    input_result = re.sub('[^\w]+|_', '', input)


    for i in range(len(input_result)):
        #print(input[i])
        character = input[i]
        if input_result[i] == 'a' or input_result[i] == 'e' or input_result[i] == 'i' or input_result[i] == 'o' or input_result[i] == 'u':
            vowelList.append(input_result[i])
        else:
            consonantList.append(input_result[i])

    print ("Vowels:", vowelList)
    print ("Consonant:", consonantList)


vowels('This is a beautiful world!')
