##################################################
## Assignment 9: TWITTER LINGUISTICS
## Author: Jordan Chen
## Email: jordanchen50@gmail.com
## Class: MIS-515 Spring 2021
##################################################

# This code will take company customer service tweets and generate data from it. 
# %pip install syllables

import textblob, json, nltk, amath, re
import matplotlib.pyplot as plt
import syllables

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

amazon = []
apple = []
spectrum = []
play_station = []
comcast = []
hulu = []
spotify = []
sprint = []
tmobile = []
uber = []
ups = []
xbox = []

with open("/content/customer_service_tweets_full", "r") as file:
  reader = file.read()
  data = json.loads(reader)

count = 0
for line in data:
  count += 1
  if line["Company"] == "@AmazonHelp":
    amazon.append(line["Text"])
  elif line["Company"] == "@AppleSupport":
    apple.append(line["Text"])
  elif line["Company"] == "@Ask_Spectrum":
    spectrum.append(line["Text"])
  elif line["Company"] == "@AskPlayStation":
    play_station.append(line["Text"])
  elif line["Company"] == "@comcastcares":
    comcast.append(line["Text"])
  elif line["Company"] == "@hulu_support":
    hulu.append(line["Text"])
  elif line["Company"] == "@SpotifyCares":
    spotify.append(line["Text"])
  elif line["Company"] == "@sprintcare":
    sprint.append(line["Text"])
  elif line["Company"] == "@TMobileHelp":
    tmobile.append(line["Text"])
  elif line["Company"] == "@Uber_Support":
    uber.append(line["Text"])
  elif line["Company"] == "@UPSHelp":
    ups.append(line["Text"])
  elif line["Company"] == "@XboxSupport":
    xbox.append(line["Text"])

# Sprint calculations
sprint_polarity_list = []
sprint_subjectivity_list = []

sprint_words = 0
sprint_sentences = 0
sprint_syllables = 0
sprint_pollysyllables = 0

f = 0
c = 0 

for tweet in sprint:
  tweet_blob = textblob.TextBlob(tweet)

  polarity_data = tweet_blob.polarity
  sprint_polarity_list.append(polarity_data)

  subjectivity_data = tweet_blob.subjectivity
  sprint_subjectivity_list.append(subjectivity_data)

  words = tweet_blob.words
  sentences = tweet_blob.sentences

  sprint_words += len(words)
  sprint_sentences += len(sentences)
  sprint_syllables += syllables.estimate(tweet)

  for word in words:
    if syllables.estimate(word) >= 3:
      sprint_pollysyllables += 1

  tags = tweet_blob.tags

  for word, tag in tags:
    noun = re.search("NN\w*", tag)
    adjective = re.search("JJ\w*", tag)
    preposition = re.search("IN\w*", tag)
    determiner = re.search("DT\w*", tag)
    pronoun = re.search("PR\w*", tag)
    verb = re.search("VB\w*", tag)
    adverb = re.search("RB\w*", tag)
    interjection = re.search("UH\w*", tag)

    if noun or adjective or preposition or determiner:
      f += 1
    elif pronoun or verb or adverb or interjection:
      c += 1

sprint_polarity = sum(sprint_polarity_list) / len(sprint)
sprint_subjectivity = sum(sprint_subjectivity_list) / len(sprint)

sprint_fkgl = 0.39 * (sprint_words / sprint_sentences) + 11.8 * (sprint_syllables / sprint_words) - 15.59
sprint_smog = 1.043 * math.sqrt(sprint_pollysyllables * (30 / sprint_sentences)) + 3.1291

sprint_formality = 50 * ((f - c) / (f + c) + 1)

# Spectrum calculations
spectrum_polarity_list = []
spectrum_subjectivity_list = []

spectrum_words = 0
spectrum_sentences = 0
spectrum_syllables = 0
spectrum_pollysyllables = 0

f = 0
c = 0 

for tweet in spectrum:
  tweet_blob = textblob.TextBlob(tweet)

  polarity_data = tweet_blob.polarity
  spectrum_polarity_list.append(polarity_data)

  subjectivity_data = tweet_blob.subjectivity
  spectrum_subjectivity_list.append(subjectivity_data)

  words = tweet_blob.words
  sentences = tweet_blob.sentences

  spectrum_words += len(words)
  spectrum_sentences += len(sentences)
  spectrum_syllables += syllables.estimate(tweet)

  for word in words:
    if syllables.estimate(word) >= 3:
      spectrum_pollysyllables += 1

  tags = tweet_blob.tags

  for word, tag in tags:
    noun = re.search("NN\w*", tag)
    adjective = re.search("JJ\w*", tag)
    preposition = re.search("IN\w*", tag)
    determiner = re.search("DT\w*", tag)
    pronoun = re.search("PR\w*", tag)
    verb = re.search("VB\w*", tag)
    adverb = re.search("RB\w*", tag)
    interjection = re.search("UH\w*", tag)

    if noun or adjective or preposition or determiner:
      f += 1
    elif pronoun or verb or adverb or interjection:
      c += 1

spectrum_polarity = sum(spectrum_polarity_list) / len(spectrum)
spectrum_subjectivity = sum(spectrum_subjectivity_list) / len(spectrum)

spectrum_fkgl = 0.39 * (spectrum_words / spectrum_sentences) + 11.8 * (spectrum_syllables / spectrum_words) - 15.59
spectrum_smog = 1.043 * math.sqrt(spectrum_pollysyllables * (30 / spectrum_sentences)) + 3.1291

spectrum_formality = 50 * ((f - c) / (f + c) + 1)

# Play Station calculations
play_station_polarity_list = []
play_station_subjectivity_list = []

play_station_words = 0
play_station_sentences = 0
play_station_syllables = 0
play_station_pollysyllables = 0

f = 0
c = 0 

for tweet in play_station:
  tweet_blob = textblob.TextBlob(tweet)

  polarity_data = tweet_blob.polarity
  play_station_polarity_list.append(polarity_data)

  subjectivity_data = tweet_blob.subjectivity
  play_station_subjectivity_list.append(subjectivity_data)

  play_station_words += len(words)
  play_station_sentences += len(sentences)
  play_station_syllables += syllables.estimate(tweet)

  for word in words:
    if syllables.estimate(word) >= 3:
      play_station_pollysyllables += 1

  tags = tweet_blob.tags

  for word, tag in tags:
    noun = re.search("NN\w*", tag)
    adjective = re.search("JJ\w*", tag)
    preposition = re.search("IN\w*", tag)
    determiner = re.search("DT\w*", tag)
    pronoun = re.search("PR\w*", tag)
    verb = re.search("VB\w*", tag)
    adverb = re.search("RB\w*", tag)
    interjection = re.search("UH\w*", tag)

    if noun or adjective or preposition or determiner:
      f += 1
    elif pronoun or verb or adverb or interjection:
      c += 1

play_station_polarity = sum(play_station_polarity_list) / len(play_station)
play_station_subjectivity = sum(play_station_subjectivity_list) / len(play_station)

play_station_fkgl = 0.39 * (play_station_words / play_station_sentences) + 11.8 * (play_station_syllables / play_station_words) - 15.59
play_station_smog = 1.043 * math.sqrt(play_station_pollysyllables * (30 / play_station_sentences)) + 3.1291

play_station_formality = 50 * ((f - c) / (f + c) + 1)

# Xbox calculations
xbox_polarity_list = []
xbox_subjectivity_list = []

xbox_words = 0
xbox_sentences = 0
xbox_syllables = 0
xbox_pollysyllables = 0

f = 0
c = 0 

for tweet in xbox:
  tweet_blob = textblob.TextBlob(tweet)

  polarity_data = tweet_blob.polarity
  xbox_polarity_list.append(polarity_data)

  subjectivity_data = tweet_blob.subjectivity
  xbox_subjectivity_list.append(subjectivity_data)

  words = tweet_blob.words
  sentences = tweet_blob.sentences

  xbox_words += len(words)
  xbox_sentences += len(sentences)
  xbox_syllables += syllables.estimate(tweet)

  for word in words:
    if syllables.estimate(word) >= 3:
      xbox_pollysyllables += 1

  tags = tweet_blob.tags

  for word, tag in tags:
    noun = re.search("NN\w*", tag)
    adjective = re.search("JJ\w*", tag)
    preposition = re.search("IN\w*", tag)
    determiner = re.search("DT\w*", tag)
    pronoun = re.search("PR\w*", tag)
    verb = re.search("VB\w*", tag)
    adverb = re.search("RB\w*", tag)
    interjection = re.search("UH\w*", tag)

    if noun or adjective or preposition or determiner:
      f += 1
    elif pronoun or verb or adverb or interjection:
      c += 1
      
xbox_polarity = sum(xbox_polarity_list) / len(xbox)
xbox_subjectivity = sum(xbox_subjectivity_list) / len(xbox)

xbox_fkgl = (0.39 * (xbox_words / xbox_sentences)) + (11.8 * (xbox_syllables / xbox_words)) - 15.59
xbox_smog = 1.043 * math.sqrt(xbox_pollysyllables * (30 / xbox_sentences)) + 3.1291

xbox_formality = 50 * ((f - c) / (f + c) + 1)

# UPS calculations
ups_polarity_list = []
ups_subjectivity_list = []

ups_words = 0
ups_sentences = 0
ups_syllables = 0
ups_pollysyllables = 0

f = 0
c = 0 

for tweet in ups:
  tweet_blob = textblob.TextBlob(tweet)

  polarity_data = tweet_blob.polarity
  ups_polarity_list.append(polarity_data)

  subjectivity_data = tweet_blob.subjectivity
  ups_subjectivity_list.append(subjectivity_data)

  words = tweet_blob.words
  sentences = tweet_blob.sentences

  ups_words += len(words)
  ups_sentences += len(sentences)
  ups_syllables += syllables.estimate(tweet)

  for word in words:
    if syllables.estimate(word) >= 3:
      ups_pollysyllables += 1

  tags = tweet_blob.tags

  for word, tag in tags:
    noun = re.search("NN\w*", tag)
    adjective = re.search("JJ\w*", tag)
    preposition = re.search("IN\w*", tag)
    determiner = re.search("DT\w*", tag)
    pronoun = re.search("PR\w*", tag)
    verb = re.search("VB\w*", tag)
    adverb = re.search("RB\w*", tag)
    interjection = re.search("UH\w*", tag)

    if noun or adjective or preposition or determiner:
      f += 1
    elif pronoun or verb or adverb or interjection:
      c += 1

ups_polarity = sum(ups_polarity_list) / len(ups)
ups_subjectivity = sum(ups_subjectivity_list) / len(ups)

ups_fkgl = (0.39 * (ups_words / ups_sentences)) + (11.8 * (ups_syllables / ups_words)) - 15.59
ups_smog = 1.043 * math.sqrt(ups_pollysyllables * (30 / ups_sentences)) + 3.1291

ups_formality = 50 * ((f - c) / (f + c) + 1)

# Amazon calculations
amazon_polarity_list = []
amazon_subjectivity_list = []

amazon_words = 0
amazon_sentences = 0
amazon_syllables = 0
amazon_pollysyllables = 0

f = 0
c = 0 

for tweet in amazon:
  tweet_blob = textblob.TextBlob(tweet)

  polarity_data = tweet_blob.polarity
  amazon_polarity_list.append(polarity_data)

  subjectivity_data = tweet_blob.subjectivity
  amazon_subjectivity_list.append(subjectivity_data)

  words = tweet_blob.words
  sentences = tweet_blob.sentences

  amazon_words += len(words)
  amazon_sentences += len(sentences)
  amazon_syllables += syllables.estimate(tweet)

  for word in words:
    if syllables.estimate(word) >= 3:
      amazon_pollysyllables += 1

  tags = tweet_blob.tags

  for word, tag in tags:
    noun = re.search("NN\w*", tag)
    adjective = re.search("JJ\w*", tag)
    preposition = re.search("IN\w*", tag)
    determiner = re.search("DT\w*", tag)
    pronoun = re.search("PR\w*", tag)
    verb = re.search("VB\w*", tag)
    adverb = re.search("RB\w*", tag)
    interjection = re.search("UH\w*", tag)

    if noun or adjective or preposition or determiner:
      f += 1
    elif pronoun or verb or adverb or interjection:
      c += 1
  
amazon_polarity = sum(amazon_polarity_list) / len(amazon)
amazon_subjectivity = sum(amazon_subjectivity_list) / len(amazon)

amazon_fkgl = 0.39 * (amazon_words / amazon_sentences) + 11.8 * (amazon_syllables / amazon_words) - 15.59
amazon_smog = 1.043 * math.sqrt(amazon_pollysyllables * (30 / amazon_sentences)) + 3.1291

amazon_formality = 50 * ((f - c) / (f + c) + 1)

# Apple calculations
apple_polarity_list = []
apple_subjectivity_list = []

apple_words = 0
apple_sentences = 0
apple_syllables = 0
apple_pollysyllables = 0

f = 0
c = 0 

for tweet in apple:
  tweet_blob = textblob.TextBlob(tweet)
  
  polarity_data = tweet_blob.polarity
  apple_polarity_list.append(polarity_data)
  
  subjectivity_data = tweet_blob.subjectivity
  apple_subjectivity_list.append(subjectivity_data)

  words = tweet_blob.words
  sentences = tweet_blob.sentences

  apple_words += len(words)
  apple_sentences += len(sentences)
  apple_syllables += syllables.estimate(tweet)

  for word in words:
    if syllables.estimate(word) >= 3:
      apple_pollysyllables += 1

  tags = tweet_blob.tags

  for word, tag in tags:
    noun = re.search("NN\w*", tag)
    adjective = re.search("JJ\w*", tag)
    preposition = re.search("IN\w*", tag)
    determiner = re.search("DT\w*", tag)
    pronoun = re.search("PR\w*", tag)
    verb = re.search("VB\w*", tag)
    adverb = re.search("RB\w*", tag)
    interjection = re.search("UH\w*", tag)

    if noun or adjective or preposition or determiner:
      f += 1
    elif pronoun or verb or adverb or interjection:
      c += 1
  
apple_polarity = sum(apple_polarity_list) / len(apple)
apple_subjectivity = sum(apple_subjectivity_list) / len(apple)

apple_fkgl = (0.39 * (apple_words / apple_sentences)) + (11.8 * (apple_syllables / apple_words)) - 15.59
apple_smog = 1.043 * math.sqrt(apple_pollysyllables * (30 / apple_sentences)) + 3.1291

apple_formality = 50 * ((f - c) / (f + c) + 1)

# Uber calculations
uber_polarity_list = []
uber_subjectivity_list = []

uber_words = 0
uber_sentences = 0
uber_syllables = 0
uber_pollysyllables = 0

f = 0
c = 0 

for tweet in uber:
  tweet_blob = textblob.TextBlob(tweet)

  polarity_data = tweet_blob.polarity
  uber_polarity_list.append(polarity_data)

  subjectivity_data = tweet_blob.subjectivity
  uber_subjectivity_list.append(subjectivity_data)

  words = tweet_blob.words
  sentences = tweet_blob.sentences

  uber_words += len(words)
  uber_sentences += len(sentences)
  uber_syllables += syllables.estimate(tweet)

  for word in words:
    if syllables.estimate(word) >= 3:
      uber_pollysyllables += 1

  tags = tweet_blob.tags

  for word, tag in tags:
    noun = re.search("NN\w*", tag)
    adjective = re.search("JJ\w*", tag)
    preposition = re.search("IN\w*", tag)
    determiner = re.search("DT\w*", tag)
    pronoun = re.search("PR\w*", tag)
    verb = re.search("VB\w*", tag)
    adverb = re.search("RB\w*", tag)
    interjection = re.search("UH\w*", tag)

    if noun or adjective or preposition or determiner:
      f += 1
    elif pronoun or verb or adverb or interjection:
      c += 1
    
uber_polarity = sum(uber_polarity_list) / len(uber)
uber_subjectivity = sum(uber_subjectivity_list) / len(uber)

uber_fkgl = (0.39 * (uber_words / uber_sentences)) + (11.8 * (uber_syllables / uber_words)) - 15.59
uber_smog = 1.043 * math.sqrt(uber_pollysyllables * (30 / uber_sentences)) + 3.1291

uber_formality = 50 * ((f - c) / (f + c) + 1)

# Spotify calculations
spotify_polarity_list = []
spotify_subjectivity_list = []

spotify_words = 0
spotify_sentences = 0
spotify_syllables = 0
spotify_pollysyllables = 0

f = 0
c = 0 

for tweet in spotify:
  tweet_blob = textblob.TextBlob(tweet)
  
  polarity_data = tweet_blob.polarity
  spotify_polarity_list.append(polarity_data)
  
  subjectivity_data = tweet_blob.subjectivity
  spotify_subjectivity_list.append(subjectivity_data)

  words = tweet_blob.words
  sentences = tweet_blob.sentences

  spotify_words += len(words)
  spotify_sentences += len(sentences)
  spotify_syllables += syllables.estimate(tweet)

  for word in words:
    if syllables.estimate(word) >= 3:
      spotify_pollysyllables += 1

  tags = tweet_blob.tags

  for word, tag in tags:
    noun = re.search("NN\w*", tag)
    adjective = re.search("JJ\w*", tag)
    preposition = re.search("IN\w*", tag)
    determiner = re.search("DT\w*", tag)
    pronoun = re.search("PR\w*", tag)
    verb = re.search("VB\w*", tag)
    adverb = re.search("RB\w*", tag)
    interjection = re.search("UH\w*", tag)

    if noun or adjective or preposition or determiner:
      f += 1
    elif pronoun or verb or adverb or interjection:
      c += 1
    
spotify_polarity = sum(spotify_polarity_list) / len(spotify)
spotify_subjectivity = sum(spotify_subjectivity_list) / len(spotify)

spotify_fkgl = (0.39 * (spotify_words / spotify_sentences)) + (11.8 * (spotify_syllables / spotify_words)) - 15.59
spotify_smog = 1.043 * math.sqrt(spotify_pollysyllables * (30 / spotify_sentences)) + 3.1291

spotify_formality = 50 * ((f - c) / (f + c) + 1)

# Comcast calculations
comcast_polarity_list = []
comcast_subjectivity_list = []

comcast_words = 0
comcast_sentences = 0
comcast_syllables = 0
comcast_pollysyllables = 0

f = 0
c = 0 

for tweet in comcast:
  tweet_blob = textblob.TextBlob(tweet)
  
  polarity_data = tweet_blob.polarity
  comcast_polarity_list.append(polarity_data)
  
  subjectivity_data = tweet_blob.subjectivity
  comcast_subjectivity_list.append(subjectivity_data)

  words = tweet_blob.words
  sentences = tweet_blob.sentences

  comcast_words += len(words)
  comcast_sentences += len(sentences)
  comcast_syllables += syllables.estimate(tweet)

  for word in words:
    if syllables.estimate(word) >= 3:
      comcast_pollysyllables += 1

  tags = tweet_blob.tags

  for word, tag in tags:
    noun = re.search("NN\w*", tag)
    adjective = re.search("JJ\w*", tag)
    preposition = re.search("IN\w*", tag)
    determiner = re.search("DT\w*", tag)
    pronoun = re.search("PR\w*", tag)
    verb = re.search("VB\w*", tag)
    adverb = re.search("RB\w*", tag)
    interjection = re.search("UH\w*", tag)

    if noun or adjective or preposition or determiner:
      f += 1
    elif pronoun or verb or adverb or interjection:
      c += 1
    
comcast_polarity = sum(comcast_polarity_list) / len(comcast)
comcast_subjectivity = sum(comcast_subjectivity_list) / len(comcast)

comcast_fkgl = (0.39 * (comcast_words / comcast_sentences)) + (11.8 * (comcast_syllables / comcast_words)) - 15.59
comcast_smog = 1.043 * math.sqrt(comcast_pollysyllables * (30 / comcast_sentences)) + 3.1291

comcast_formality = 50 * ((f - c) / (f + c) + 1)

# Tmobile calculations
tmobile_polarity_list = []
tmobile_subjectivity_list = []

tmobile_words = 0
tmobile_sentences = 0
tmobile_syllables = 0
tmobile_pollysyllables = 0

f = 0
c = 0 

for tweet in tmobile:
  tweet_blob = textblob.TextBlob(tweet)

  polarity_data = tweet_blob.polarity
  tmobile_polarity_list.append(polarity_data)

  subjectivity_data = tweet_blob.subjectivity
  tmobile_subjectivity_list.append(subjectivity_data)

  words = tweet_blob.words
  sentences = tweet_blob.sentences

  tmobile_words += len(words)
  tmobile_sentences += len(sentences)
  tmobile_syllables += syllables.estimate(tweet)

  for word in words:
    if syllables.estimate(word) >= 3:
      tmobile_pollysyllables += 1

  tags = tweet_blob.tags

  for word, tag in tags:
    noun = re.search("NN\w*", tag)
    adjective = re.search("JJ\w*", tag)
    preposition = re.search("IN\w*", tag)
    determiner = re.search("DT\w*", tag)
    pronoun = re.search("PR\w*", tag)
    verb = re.search("VB\w*", tag)
    adverb = re.search("RB\w*", tag)
    interjection = re.search("UH\w*", tag)

    if noun or adjective or preposition or determiner:
      f += 1
    elif pronoun or verb or adverb or interjection:
      c += 1
  
tmobile_polarity = sum(tmobile_polarity_list) / len(tmobile)
tmobile_subjectivity = sum(tmobile_subjectivity_list) / len(tmobile)

tmobile_fkgl = (0.39 * (tmobile_words / tmobile_sentences)) + (11.8 * (tmobile_syllables / tmobile_words)) - 15.59
tmobile_smog = 1.043 * math.sqrt(tmobile_pollysyllables * (30 / tmobile_sentences)) + 3.1291

tmobile_formality = 50 * ((f - c) / (f + c) + 1)

# Hulu calculations
hulu_polarity_list = []
hulu_subjectivity_list = []

hulu_words = 0
hulu_sentences = 0
hulu_syllables = 0
hulu_pollysyllables = 0

f = 0
c = 0 

for tweet in hulu:
  tweet_blob = textblob.TextBlob(tweet)
  polarity_data = tweet_blob.polarity
  hulu_polarity_list.append(polarity_data)

  subjectivity_data = tweet_blob.subjectivity
  hulu_subjectivity_list.append(subjectivity_data)

  words = tweet_blob.words
  sentences = tweet_blob.sentences

  hulu_words += len(words)
  hulu_sentences += len(sentences)
  hulu_syllables += syllables.estimate(tweet)

  for word in words:
    if syllables.estimate(word) >= 3:
      hulu_pollysyllables += 1

  tags = tweet_blob.tags

  for word, tag in tags:
    noun = re.search("NN\w*", tag)
    adjective = re.search("JJ\w*", tag)
    preposition = re.search("IN\w*", tag)
    determiner = re.search("DT\w*", tag)
    pronoun = re.search("PR\w*", tag)
    verb = re.search("VB\w*", tag)
    adverb = re.search("RB\w*", tag)
    interjection = re.search("UH\w*", tag)

    if noun or adjective or preposition or determiner:
      f += 1
    elif pronoun or verb or adverb or interjection:
      c += 1
    
hulu_polarity = sum(hulu_polarity_list) / len(hulu)
hulu_subjectivity = sum(hulu_subjectivity_list) / len(hulu)

hulu_fkgl = (0.39 * (hulu_words / hulu_sentences)) + (11.8 * (hulu_syllables / hulu_words)) - 15.59
hulu_smog = 1.043 * math.sqrt(hulu_pollysyllables * (30 / hulu_sentences)) + 3.1291

hulu_formality = 50 * ((f - c) / (f + c) + 1)

# Start of user inputs. All calculations are done beforehand. 
print("Welcome to the customer service linguistics analyzer!")

repeat = "yes"

while repeat.lower() == "yes":

  user_choice = input("\nWhich analysis would you like to perform (polarity/subjectivity/readability/formality/search)? ")

  if user_choice.lower() == "polarity":

    print("\n@sprintcare:", sprint_polarity)
    print("@ask_spectrum:", spectrum_polarity)
    print("@askplaystation:", play_station_polarity)
    print("@xboxsupport:", xbox_polarity)
    print("@upshelp:", ups_polarity)
    print("@amazonhelp:", amazon_polarity)
    print("@applesupport:", apple_polarity)
    print("@uber_spport:", uber_polarity)
    print("@spotifycares:", spotify_polarity)
    print("@comcastcares:", comcast_polarity)
    print("@tmobilehelp:", tmobile_polarity)
    print("@hulu_support:", hulu_polarity, "\n")

    plt.bar(["@sprintcare", "@ask_spectrum", "@askplaystation", "@xboxsupport", "@upshelp", "@amazonhelp", "@applesupport", "@uber_spport", "@spotifycares", "@comcastcares", "@tmobilehelp", "@hulu_support"], 
            [sprint_polarity, spectrum_polarity, play_station_polarity, xbox_polarity, ups_polarity, amazon_polarity, apple_polarity, uber_polarity, spotify_polarity, comcast_polarity, tmobile_polarity, hulu_polarity])
    plt.xticks(rotation = 45, ha = "right")
    plt.title("Polarities by Twitter handle")
    plt.ylabel('Polarity')
    plt.xlabel('Twitter handle')
    plt.show()

  elif user_choice.lower() == "subjectivity":

    print("\n@sprintcare:", sprint_subjectivity)
    print("@ask_spectrum:", spectrum_subjectivity)
    print("@askplaystation:", play_station_subjectivity)
    print("@xboxsupport:", xbox_subjectivity)
    print("@upshelp:", ups_subjectivity)
    print("@amazonhelp:", amazon_subjectivity)
    print("@applesupport:", apple_subjectivity)
    print("@uber_spport:", uber_subjectivity)
    print("@spotifycares:", spotify_subjectivity)
    print("@comcastcares:", comcast_subjectivity)
    print("@tmobilehelp:", tmobile_subjectivity)
    print("@hulu_support:", hulu_subjectivity, "\n")

    plt.bar(["@sprintcare", "@ask_spectrum", "@askplaystation", "@xboxsupport", "@upshelp", "@amazonhelp", "@applesupport", "@uber_spport", "@spotifycares", "@comcastcares", "@tmobilehelp", "@hulu_support"], 
            [sprint_subjectivity, spectrum_subjectivity, play_station_subjectivity, xbox_subjectivity, ups_subjectivity, amazon_subjectivity, apple_subjectivity, uber_subjectivity, spotify_subjectivity, comcast_subjectivity, tmobile_subjectivity, hulu_subjectivity])
    plt.xticks(rotation = 45, ha = "right")
    plt.title("Subjectivities by Twitter handle")
    plt.ylabel('Subjectivity')
    plt.xlabel('Twitter handle')
    plt.show()
  
  elif user_choice.lower() == "readability":
    readability_choice = input("Would you like to analyze FKGL or SMOG? ")
    
    if readability_choice.lower() == "fkgl":

      print("\n@sprintcare:", sprint_fkgl)
      print("@ask_spectrum:", spectrum_fkgl)
      print("@askplaystation:", play_station_fkgl)
      print("@xboxsupport:", xbox_fkgl)
      print("@upshelp:", ups_fkgl)
      print("@amazonhelp:", amazon_fkgl)
      print("@applesupport:", apple_fkgl)
      print("@uber_spport:", uber_fkgl)
      print("@spotifycares:", spotify_fkgl)
      print("@comcastcares:", comcast_fkgl)
      print("@tmobilehelp:", tmobile_fkgl)
      print("@hulu_support:", hulu_fkgl, "\n")

      plt.bar(["@sprintcare", "@ask_spectrum", "@askplaystation", "@xboxsupport", "@upshelp", "@amazonhelp", "@applesupport", "@uber_spport", "@spotifycares", "@comcastcares", "@tmobilehelp", "@hulu_support"], 
              [sprint_fkgl, spectrum_fkgl, play_station_fkgl, xbox_fkgl, ups_fkgl, amazon_fkgl, apple_fkgl, uber_fkgl, spotify_fkgl, comcast_fkgl, tmobile_fkgl, hulu_fkgl])
      plt.xticks(rotation = 45, ha = "right")
      plt.title("Flesch-Kincaid Grade Levels by Twitter Handle")
      plt.ylabel('Flesch-Kincaid Grade Level')
      plt.xlabel('Twitter handle')
      plt.show()

    elif readability_choice.lower() == "smog":

      print("\n@sprintcare:", sprint_smog)
      print("@ask_spectrum:", spectrum_smog)
      print("@askplaystation:", play_station_smog)
      print("@xboxsupport:", xbox_smog)
      print("@upshelp:", ups_smog)
      print("@amazonhelp:", amazon_smog)
      print("@applesupport:", apple_smog)
      print("@uber_spport:", uber_smog)
      print("@spotifycares:", spotify_smog)
      print("@comcastcares:", comcast_smog)
      print("@tmobilehelp:", tmobile_smog)
      print("@hulu_support:", hulu_smog, "\n")

      plt.bar(["@sprintcare", "@ask_spectrum", "@askplaystation", "@xboxsupport", "@upshelp", "@amazonhelp", "@applesupport", "@uber_spport", "@spotifycares", "@comcastcares", "@tmobilehelp", "@hulu_support"], 
              [sprint_smog, spectrum_smog, play_station_smog, xbox_smog, ups_smog, amazon_smog, apple_smog, uber_smog, spotify_smog, comcast_smog, tmobile_smog, hulu_smog])
      plt.xticks(rotation = 45, ha = "right")
      plt.title("Simple Measure of Gobbledygook Index by Twitter Handle")
      plt.ylabel('Simple Measure of Gobbledygook Index')
      plt.xlabel('Twitter handle')
      plt.show()

    else:
      print("Sorry, that type of analysis is not supported. Please try again.")

  elif user_choice.lower() == "formality":

    print("\n@sprintcare:", sprint_formality)
    print("@ask_spectrum:", spectrum_formality)
    print("@askplaystation:", play_station_formality)
    print("@xboxsupport:", xbox_formality)
    print("@upshelp:", ups_formality)
    print("@amazonhelp:", amazon_formality)
    print("@applesupport:", apple_formality)
    print("@uber_spport:", uber_formality)
    print("@spotifycares:", spotify_formality)
    print("@comcastcares:", comcast_formality)
    print("@tmobilehelp:", tmobile_formality)
    print("@hulu_support:", hulu_formality, "\n")

    plt.bar(["@sprintcare", "@ask_spectrum", "@askplaystation", "@xboxsupport", "@upshelp", "@amazonhelp", "@applesupport", "@uber_spport", "@spotifycares", "@comcastcares", "@tmobilehelp", "@hulu_support"], 
            [sprint_formality, spectrum_formality, play_station_formality, xbox_formality, ups_formality, amazon_formality, apple_formality, uber_formality, spotify_formality, comcast_formality, tmobile_formality, hulu_formality])
    plt.xticks(rotation = 45, ha = "right")
    plt.title("Formalities by Twitter handle")
    plt.ylabel('Formality')
    plt.xlabel('Twitter handle')
    plt.show()
  
  elif user_choice.lower() == "search":
    search_choice = input("Which Twitter handle would you like to search? ")

    if search_choice.lower() == "@sprintcare":
      print("\nAverage polarity:", sprint_polarity)
      print("Average subjectivity:", sprint_subjectivity)
      print("Average Flesch-Kincaid Grade Level:", sprint_fkgl)
      print("Average SMOG index:", sprint_smog)
      print("Average Formality index:", sprint_formality)

    elif search_choice.lower() == "@ask_spectrum":
      print("\nAverage polarity:", spectrum_polarity)
      print("Average subjectivity:", spectrum_subjectivity)
      print("Average Flesch-Kincaid Grade Level:", spectrum_fkgl)
      print("Average SMOG index:", spectrum_smog)
      print("Average Formality index:", spectrum_formality)
      
    elif search_choice.lower() == "@askplaystation":
      print("\nAverage polarity:", play_station_polarity)
      print("Average subjectivity:", play_station_subjectivity)
      print("Average Flesch-Kincaid Grade Level:", play_station_fkgl)
      print("Average SMOG index:", play_station_smog)
      print("Average Formality index:", play_station_formality)

    elif search_choice.lower() == "@xboxsupport":
      print("\nAverage polarity:", xbox_polarity)
      print("Average subjectivity:", xbox_subjectivity)
      print("Average Flesch-Kincaid Grade Level:", xbox_fkgl)
      print("Average SMOG index:", xbox_smog)
      print("Average Formality index:", xbox_formality)

    elif search_choice.lower() == "@upshelp":
      print("\nAverage polarity:", ups_polarity)
      print("Average subjectivity:", ups_subjectivity)
      print("Average Flesch-Kincaid Grade Level:", ups_fkgl)
      print("Average SMOG index:", ups_smog)
      print("Average Formality index:", ups_formality)

    elif search_choice.lower() == "@amazonhelp":
      print("\nAverage polarity:", amazon_polarity)
      print("Average subjectivity:", amazon_subjectivity)
      print("Average Flesch-Kincaid Grade Level:", amazon_fkgl)
      print("Average SMOG index:", amazon_smog)
      print("Average Formality index:", amazon_formality)

    elif search_choice.lower() == "@applesupport":
      print("\nAverage polarity:", apple_polarity)
      print("Average subjectivity:", apple_subjectivity)
      print("Average Flesch-Kincaid Grade Level:", apple_fkgl)
      print("Average SMOG index:", apple_smog)
      print("Average Formality index:", apple_formality)

    elif search_choice.lower() == "@uber_support":
      print("\nAverage polarity:", uber_polarity)
      print("Average subjectivity:", uber_subjectivity)
      print("Average Flesch-Kincaid Grade Level:", uber_fkgl)
      print("Average SMOG index:", uber_smog)
      print("Average Formality index:", uber_formality)    

    elif search_choice.lower() == "@spotifycares":
      print("\nAverage polarity:", spotify_polarity)
      print("Average subjectivity:", spotify_subjectivity)
      print("Average Flesch-Kincaid Grade Level:", spotify_fkgl)
      print("Average SMOG index:", spotify_smog)
      print("Average Formality index:", spotify_formality)

    elif search_choice.lower() == "@comcastcares":
      print("\nAverage polarity:", comcast_polarity)
      print("Average subjectivity:", comcast_subjectivity)
      print("Average Flesch-Kincaid Grade Level:", comcast_fkgl)
      print("Average SMOG index:", comcast_smog)
      print("Average Formality index:", comcast_formality)
    
    elif search_choice.lower() == "@tmobilehelp":
      print("\nAverage polarity:", tmobile_polarity)
      print("Average subjectivity:", tmobile_subjectivity)
      print("Average Flesch-Kincaid Grade Level:", tmobile_fkgl)
      print("Average SMOG index:", tmobile_smog)
      print("Average Formality index:", tmobile_formality)

    elif search_choice.lower() == "@hulu_support":
      print("\nAverage polarity:", hulu_polarity)
      print("Average subjectivity:", hulu_subjectivity)
      print("Average Flesch-Kincaid Grade Level:", hulu_fkgl)
      print("Average SMOG index:", hulu_smog)
      print("Average Formality index:", hulu_formality)
  
    else:
      print("Sorry, that Twitter handle was not found. Please try again.")
      
  else:
    print("Sorry, that type of analysis is not supported. Please try again.")
    
  repeat = input("\nWould you like to run another analysis (yes/no)? ")

print("\nThank you for using the customer service linguistics analyzer!")