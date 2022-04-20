##################################################
## Assignment 7: HAIKU GENERATOR
## Author: Jordan Chen
## Email: jordanchen50@gmail.com
## Class: MIS-515 Spring 2021
##################################################

# This program creates a haiku from a user input word

import requests, json

print('Hello, welcome to the predictive text Haiku generator!')

# While loop allows user to create as many haikus as they want
repeat = 'yes'
while repeat.lower() == 'yes':

# Try/Except block will catch any haikus that can't be generated 
  try:
    content = input('What would you like to see a Haiku about? ')

    # Word 0
    url = 'https://api.datamuse.com/words?md=s&rel_trg=' + content
    response = requests.get(url)
    data = json.loads(response.text)
    for i in data:
      if i['numSyllables'] == 3:
        word_0 = i['word']
        break

    # Word 1
    url = 'https://api.datamuse.com/words?md=s&lc=' + word_0
    response = requests.get(url)
    data = json.loads(response.text)
    for i in data:
      if i['numSyllables'] == 2:
        word_1 = i['word']
        break

    # word 2
    url = 'https://api.datamuse.com/words?md=s&lc=' + word_1
    response = requests.get(url)
    data = json.loads(response.text)
    for i in data:
      if i['numSyllables'] == 3:
        word_2 = i['word']
        break

    # word 3
    url = 'https://api.datamuse.com/words?md=s&lc=' + word_2
    response = requests.get(url)
    data = json.loads(response.text)
    for i in data:
      if i['numSyllables'] == 2:
        word_3 = i['word']
        break

    # word 4
    url = 'https://api.datamuse.com/words?md=s&lc=' + word_3 + '&rel_rhy=' + word_1
    response = requests.get(url)
    data = json.loads(response.text)
    for i in data:
      if i['numSyllables'] == 2:
        word_4 = i['word']
        break

    # word 5 
    url = 'https://api.datamuse.com/words?md=s&lc=' + word_4
    response = requests.get(url)
    data = json.loads(response.text)
    for i in data:
      if i['numSyllables'] == 3:
        word_5 = i['word']
        break

    # word 6
    url = 'https://api.datamuse.com/words?md=s&lc=' + word_5 + '&rel_rhy=' + word_1
    response = requests.get(url)
    data = json.loads(response.text)
    for i in data:
      if i['numSyllables'] == 2 and i['word'] != word_4:
        word_6 = i['word']
        break

    print('\n' + word_0, word_1 + '\n' + word_2, word_3, word_4 + '\n' + word_5, word_6 + '\n')
    
    # Delete variables so try/except block can work if haiku fails to generate 
    del word_0, word_1, word_2, word_3, word_4, word_5, word_6

  except:
    print("Sorry, a valid Haiku could not be generated. ")

  repeat = input('Would you like to see another Haiku? [yes/no] ')

print("\nThank you for using the predictive text Haiku Generator!")