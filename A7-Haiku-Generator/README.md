# MIS 515 ASSIGNMENT 7:

# HAIKU GENERATOR

Your assignment is to use the Datamuse API to generate a predictive text-driven Haiku on a
topic of the user’s choice. Your program should first request that the user provide a topic to
begin the Haiku generation. Then, your program should connect to the Datamuse API to find
related words that satisfy the requirements of a Haiku (described below). Print your completed
Haiku for the user to enjoy. Finally, your program should allow the user to generate as many
Haikus as desired.

For the purposes of this assignment, the requirements of Haikus are:

- A Haiku is a 3-line poem, where the first line contains 5 syllables, the second line contains 7
    syllables, and the third line contains 5 syllables.
- The last words of each line in the Haiku must rhyme.
- A Haiku may not use the same word more than once

The Datamuse API supports several forms of queries that will assist you in this assignment. For
the first word of the Haiku, choose a word related to the topic selected by the user. Use
"https://api.datamuse.com/words?md=s&rel_trg=word” to search for a word related to your
user’s topic (replace “word” in the URL above with whatever topic you would like to search).
This mode of the API searches for “related triggers,” which the API abbreviates as “rel_trg.”
These words are not necessarily synonyms, but rather words that follow the same topic. For
example, a related trigger of “cow” might be a word like “milking.” These two words are not
synonyms but pertain to the same topic. For example, if your topic were “food,” you might use
"https://api.datamuse.com/words?md=s&rel_trg=food” to search for related words. The first few
words returned by this search are “FDA”, “beverage”, and “nutrition”.

For the next words of your Haiku, rather than using related triggers, instead, use
"https://api.datamuse.com/words?md=s&lc=word” to search for words that commonly follow the
previous word. The “lc” in the URL stands for “left context,” meaning that the word you search
commonly appears to the left of (just before) whatever words the API returns. For example, if the
previous word in your Haiku were “jump,” then you might use
"https://api.datamuse.com/words?md=s&lc=jump” to search for words that commonly appear
after “jump.” The first few words returned by this search are “to”, “in”, and “into”.

At the end of each line of the Haiku, you must meet the rhyming requirement mentioned above.
To do so, use "https://api.datamuse.com/words?md=s&lc=word&rel_rhy=rhyme” to search for
words that are both related to the previous word in the sentence and rhyme with the end of each
line. This URL uses two parameters in its querystring: the “lc” or left context to 2 search, and the
“rel_rhy” or rhyming word to match. For example, suppose that you needed a word that
commonly followed “by” in a sentence and also rhymed with “grape.” In this case, you might
use “https://api.datamuse.com/words?md=s&lc=by&rel_rhy=grape” to search for words. The
first few words returned by this search are “shape”, “tape”, and “escape”.


The Datamuse API returns its responses in a JSON format. The API attempts to determine the
words that are the best fit for your query, and it lists what it believes to be the most likely fits
first, ranked by a score. For example, you may expect responses to use the following format:
```
[{"word": "fda", "score": 1448, "numSyllables": 2},

{"word": "beverage", "score": 1437, "numSyllables": 3},

{"word": "nutrition", "score": 1382, "numSyllables": 3}]
```
Suppose that you use json.loads() to load the response above into a Python JSON parser named
data. A for loop can efficiently sift through your response, such as:
```
for line in data:

print(“Word:”, line[“word”])

print(“Syllables:”, line[“numSyllables”])

The printout would be:

Word: fda
Syllables: 2
Word: beverage
Syllables: 3
Word: nutrition
Syllables: 3
```
The Datamuse API is not perfect. As you can see above, it reports that the word “FDA” is 2
syllables (probably “F-DA”), whereas it is usually pronounced as 3 syllables (“F-D-A”). For the
purposes of this assignment, you may assume that the results of the API are valid, and you do not
need to correct any mistakes that the API may make.

Allocating words to use exactly 5, 7, and 5 syllables in each line can be a complicated problem.
For the purposes of this assignment, you may have some flexibility in how you address that
problem. One approach, which is strongly recommended, is to always use a fixed number of
syllables for each word in the Haiku. For example, the implementation in the example below
uses (3-2) to achieve 5 syllables in the first line, (3- 2 - 2) to achieve 7 syllables in the second line,
and (3-2) achieve to 5 syllables in the third line. You may experiment with different schemes, or
you may use the same scheme mentioned here. Occasionally, using this approach, you may find
that some topics cannot result in valid Haikus because of a lack of related and/or rhyming words.
Should this occur, simply print a message stating that a valid Haiku could not be generated.

Some considerations to note:

- Consider the possibility that, when attempting connection to the Datamuse API, some
    connection issue occurs (that is, a status code other than 200). Ensure that your code handles
    this case and provides the user with a helpful printout if it does occur.
- When your program asks the user whether they would like to see another Haiku, consider the
    possibility that the user will respond in uppercase, lowercase, or mixed case letters (“YES”)
- The words returned by the Datamuse API are always in lowercase formatting. Capitalizing
    word(s) in your Haiku is not required. Additionally, adding other punctuation such as
    commas or periods to your Haiku is not required.
- Ensure that your prompts and output are crisp, professional, and well-formatted. For
    example, ensure that you have used spaces appropriately and checked your spelling.
- Adding comments in your code is encouraged. You may decide how best to comment your
    code. At minimum, please use a comment at the start of your code to describe its basic
    functionality


