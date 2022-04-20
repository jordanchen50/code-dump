##################################################
## Assignment 8: MOVIE ANALYTICS
## Author: Jordan Chen
## Email: jordanchen50@gmail.com
## Class: MIS-515 Spring 2021
##################################################

# %pip install xmltodict
# This code will allow users to find, print, and show information about movies
import textblob
import wordcloud
import skimage.io
import requests, xmltodict, json
import matplotlib.pyplot as plt

print("Welcome to the movie analytics tool! ")

repeat_analyzer = "yes"

# There are two while loops. The first is to search another movie. The next is to find more information on movie.
while repeat_analyzer.lower() == "yes":
  
  # User inputs what movie they want to search up here
  user_movie = textblob.TextBlob(input("What movie would you like to analyze? "))
  user_movie = user_movie.correct()
  user_movie = str(user_movie)

  # Getting XML Data (OBDb API)
  xml_respone = requests.get("https://www.omdbapi.com/?r=xml&apikey=61bef303&t=" + user_movie)

  # Checks if there is a resposne from website
  if xml_respone.status_code != 200:
    print("An error has occured connecting to the OMDb API. Please try again.")
    break
  else:
    xml_data = xmltodict.parse(xml_respone.text)
  
  # Checks if user inputs valid movie title
  try:
    test_xml = xml_data["root"]["movie"]
  except:
    print("Please try again and input a valid movie title.")
    break

  # Getting JSON Data (NY Times API)
  json_respone = requests.get("https://api.nytimes.com/svc/movies/v2/reviews/search.json?query=" + user_movie + "&api-key=PEMFzlgIN36SWAiTXfkrnjRq4EDGOdCj")

  # Checks if there is a resposne from website
  if json_respone.status_code != 200:
    print("An error has occured connecting to the NY Times API. Please try again")
    break
  else:
    json_data = json.loads(json_respone.text)

  # Checks if user inputs valid movie title
  try:
    text_json = json_data["results"]
  except:
    print("Please try again and input a valid movie title.")
    break

  repeat_movie = "yes"

  while repeat_movie.lower() == "yes":
    
    # Allow users to choose what they want to see about specified movies 
    user_choice = textblob.TextBlob(input("What would you like to see (background/reception/poster/wordcloud/sentiment)? "))
    user_choice = user_choice.correct()

    # BACKGROUND
    if user_choice.lower() == "background":
      print("Year: " + xml_data["root"]["movie"]["@year"])
      print("Rating: " + xml_data["root"]["movie"]["@rated"])
      print("Runtime: " + xml_data["root"]["movie"]["@runtime"])
      print("Genre: " + xml_data["root"]["movie"]["@genre"])
      print("Actors: " + xml_data["root"]["movie"]["@actors"])
      print("Plot: " + xml_data["root"]["movie"]["@plot"])

    # RECEPTION
    elif user_choice.lower() == "reception":
      print("Awards: " + xml_data["root"]["movie"]["@awards"])
      print("Metascore: " + xml_data["root"]["movie"]["@metascore"])
      print("IMDb Rating: " + xml_data["root"]["movie"]["@imdbRating"])

    # POSTER
    elif user_choice.lower() == "poster":
      image_url = xml_data["root"]["movie"]["@poster"]
      image = skimage.io.imread(image_url)
      plt.imshow(image, interpolation = "bilinear")
      plt.axis("off")
      plt.show()

    # WORDCLOUD
    elif user_choice.lower() == "wordcloud":
      word_cloud_data = ""
      for line in json_data["results"]:
        summary = line["summary_short"]
        word_cloud_data = word_cloud_data + " " + summary

      cloud = wordcloud.WordCloud(width = 2000, height = 2000, background_color = "white", colormap = "inferno")
      cloud.generate(word_cloud_data)
      plt.imshow(cloud, interpolation = 'bilinear')
      plt.axis('off')
      plt.show()

    # SENTIMENT
    elif user_choice.lower() == "sentiment":
      polarity_data = []
      subjectivity_data = []

      for line in json_data["results"]:
        temp_data = textblob.TextBlob(line["summary_short"])

        polarity_data.append(temp_data.polarity)
        subjectivity_data.append(temp_data.subjectivity)

      average_polarity = sum(polarity_data) / len(polarity_data)
      average_subjectivity = sum(subjectivity_data) / len(subjectivity_data)

      print("Average New York Times review polarity:", average_polarity)
      print("Average New York Times review subjectivity:", average_subjectivity)
    
    # IF USER ENTERS AN ANALYSIS THAT ISN'T SUPPORTED
    else:
      print("Sorry, that analysis is not supported. Please try again.")
  
    repeat_movie = textblob.TextBlob(input("Would you like to further analyze this movie (yes/no)? "))
    repeat_movie = repeat_movie.correct()

  repeat_analyzer = textblob.TextBlob(input("Would you like to analyze another movie (yes/no)? "))
  repeat_analyzer = repeat_analyzer.correct()

# At the end of the program, it will thank user for using it
print("Thank you for using the movie analytics tool! ")