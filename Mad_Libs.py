'''
ESYST-131 IoT - Python Programming - MadLibs
I. Romero
Goal: The program will capture input from the user with a number of prompts.
It will then select and save a few random choices from a HUGE list of adjectives.
This code will print the sick note via an fString.
variables: silly_Word_1,last_Name,illness,noun_plural,silly_Word_2,place,number (Does not need to be converted to int), adjectives - The list to hold these adjectives,
Adjective1, Adjective2, Adjective3, story - the string variable to hold the story
'''

#Importing the randrange() method
from random import randrange

#Creating variables that will be used in the story
silly_Word_1 = ""
last_Name = " "
illness = " "
noun_plural = " "
silly_Word_2 = " "
place = " "
number = " "

#Create a list called adjectives
adjectives = ["adorable", " adventurous", " aggressive",
"agreeable", " alert", " alive",
"amused", " angry", " annoyed",
"annoying", " anxious", " arrogant",
"ashamed", " attractive", " average",
"awful", " bad", " beautiful",
"better", " bewildered", " black",
"bloody", " blue", " blue-eyed",
"blushing", " bored", " brainy",
"brave", " breakable", " bright",
"busy", " calm", " careful",
"cautious", " charming", " cheerful",
"clean", " clear", " clever",
"cloudy", " clumsy", " colorful",
"combative", " comfortable", " concerned",
"condemned", " confused", " cooperative", 
"courageous", " crazy", " creepy",
"crowded", " cruel", " curious",
"cute", " dangerous", " dark",
"dead", " defeated", " defiant",
"delightful", " depressed", " determined",
"different", " difficult", " disgusted",
"distinct", " disturbed", " dizzy",
"doubtful", " drab", " dull",
"eager","easy","elated"
"elegant","embarrassed","enchanting"
"encouraging","energetic","enthusiastic"
"envious","evil","excited"
"expensive","exuberant","fair"
"faithful","famous","fancy"
"fantastic","fierce","filthy"
"fine","foolish","fragile"
"frail","frantic","friendly"
"frightened","funny","gentle"
"gifted","glamorous","gleaming"
"glorious","good","gorgeous"
"graceful","grieving","grotesque"
"grumpy","handsome","happy"
"healthy","helpful","helpless"
"hilarious","homeless","homely"
"horrible","hungry","hurt"
"ill","important","impossible"
"inexpensive","innocent","inquisitive"
"itchy","jealous","jittery"
"jolly","joyous","kind",
"lazy","light","lively"
"lonely","long","lovely"
"lucky","magnificent","misty"
"modern","motionless","muddy"
"mushy","mysterious","nasty"
"naughty","nervous","nice"
"nutty","obedient","obnoxious"
"odd","old-fashioned","open"
"outrageous","outstanding","panicky"
"perfect","plain","pleasant"
"poised","poor","powerful"
"precious","prickly","proud"
"putrid","puzzled","quaint"
"real","relieved","repulsive"
"rich","scary","selfish"
"shiny","shy","silly"
"sleepy","smiling","smoggy"
"sore","sparkling","splendid"
"spotless","stormy","strange"
"stupid","successful","super",
"talented","tame","tasty"
"tender","tense","terrible"
"thankful","thoughtful","thoughtless"
"tired","tough","troubled"
"ugliest","ugly","uninterested"
"unsightly","unusual","upset"
"uptight","vast","victorious"
"vivacious","wandering","weary"
"wicked","wide-eyed","wild"
"witty","worried","worrisome"
"wrong","zany","zealous"]

#Prompt the user to enter the first Silly word
silly_Word_1 = input("Enter a Silly Word ")

#Prompt the user to enter a last name
last_Name = input("Enter a last name ")

#Prompt the user to enter an illness of their choosing
illness = input("Enter an illness ")

#Prompt the user to enter a plural noun
noun_plural = input("Enter a plural noun ")

#Prompt the user to enter the second Silly word
silly_Word_2 = input("Enter another Silly Word ")

#Prompt the user to enter a place
place = input("Enter a place ")

#Prompt the user to enter a number
number = input("Enter a number ")

#Using the len method to determine the amount of words in the adjective list
print(len(adjectives))

#Come up with three random adjectives from the list adjectives
Adjective1 = adjectives[randrange(0,179,1)]
Adjective2 = adjectives[randrange(0,179,1)]
Adjective3 = adjectives[randrange(0,179,1)]

#Create a variable (it is a string) that holds the story text
story = f"""Dear School Nurse: 
{silly_Word_1} {last_Name} will not be attending school today. 
He/she has come down with a case of {illness} and has horrible {noun_plural} and a/an {Adjective1} fever. 
We have made an appointment with the {Adjective2} Dr. {silly_Word_2}, who studied for many years in {place} and has {number} degrees in pediatrics. 
He will send you all the information you need. Thank you! 
Sincerely 
Mrs. {Adjective3}. """

#print the story
print(story)