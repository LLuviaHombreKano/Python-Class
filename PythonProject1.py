
#Programmed by Isaiah Romero

#Create list of friends
newList1 = ["johnny bravo",
"marilyn Monroe",
"Nikola Tesla",
"cleopatra",
"Steve rogers",
"helen of Troy",
"bruce bAnner",
"Natasha Romanoff"
    ]

#Assign newList1 to variable "friends"
friends = newList1

#print friends list 

print(friends) 

#print friends by first name only

print(friends[0].split("bravo"))
print(friends[1].split("Monroe"))
print(friends[2].split("Tesla"))
print(friends[3])
print(friends[4].split("rogers"))
print(friends[5].split("of Troy"))
print(friends[6].split("bAnner"))
print(friends[7].split("Romanoff"))

#split friends and print out first name first letter capitalized

print (friends[0].split(" ")[0].title())
print (friends[1].split(" ")[0].title())
print (friends[2].split(" ")[0].title())
print (friends[3].title())
print (friends[4].split(" ")[0].title())
print (friends[5].split(" ")[0].title())
print (friends[6].split(" ")[0].title())
print (friends[7].split(" ")[0].title())

#Send out 8 greetings for the people in the list to a party

name1 = friends[0].split(" ")[0].title()
name2 = friends[1].split(" ")[0].title()
name3 = friends[2].split(" ")[0].title()
name4 = friends[3].title() 
name5 = friends[4].split(" ")[0].title()
name6 = friends[5].split(" ")[0].title()
name7 = friends[6].split(" ")[0].title()
name8 = friends[7].split(" ")[0].title()

print(f"There's gonna be a freakshow on the dancefloor, pull up at the crib, {name1}!")
print(f"There's gonna be a freakshow on the dancefloor, pull up at the crib, {name2}!")
print(f"There's gonna be a freakshow on the dancefloor, pull up at the crib, {name3}!")
print(f"There's gonna be a freakshow on the dancefloor, pull up at the crib, {name4}!")
print(f"There's gonna be a freakshow on the dancefloor, pull up at the crib, {name5}!")
print(f"There's gonna be a freakshow on the dancefloor, pull up at the crib, {name6}!")
print(f"There's gonna be a freakshow on the dancefloor, pull up at the crib, {name7}!")
print(f"There's gonna be a freakshow on the dancefloor, pull up at the crib, {name8}!")