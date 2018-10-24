"""
This program generates passages that are generated in mad-lib format
Author: Damion
"""

# The template for the story

STORY = "This morning _ woke up feeling _. 'It is going to be a _ day!' Outside, a bunch of _s were protesting to keep _ in stores. They began to _ to the rhythm of the _, which made all the _s very _. Concerned, _ texted _, who flew _ to _ and dropped _ in a puddle of frozen _. _ woke up in the year _, in a world where _s ruled the world."

print 'Mad Libs is running'

name = raw_input( 'Enter a Name:')

adj_1 = raw_input ( 'First adjective:')
adj_2 = raw_input ( 'Second adjective:')
adj_3 = raw_input ( 'Third adjective:')

verb_1 = raw_input ( 'Let\'s have a verb:')

noun_1 = raw_input ( 'Need a noun:')
noun_2 = raw_input ( 'One more noun:')

animal = raw_input ( 'Enter an animal:')
food = raw_input ( 'Enter a food:')
fruit = raw_input ( 'Enter a fruit:')
superhero = raw_input ( 'Favorite superhero:')
country = raw_input ( 'Enter the name of a country:')
dessert = raw_input ( 'Favorite dessert:')
year = raw_input ( 'Random year:')

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print STORY %( name, adj_1, adj_2, animal, food, verb_1, noun_1, fruit, adj_3, name, superhero, name, country, name, dessert, name, year, noun_2)
