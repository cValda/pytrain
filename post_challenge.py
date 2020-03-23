#this is a solution to a challenge - no real use outside of that
#you are at a post office and they process people in alphabetical order
#each request takes 20 minutes to process (i know, whatever)
#input your name, the number of available clerks and names of other people, who arrived at the same time as you
#output is time required to hande your request

name = input()
agents = int(input())
others = input()

import math

people = others.split(' ')
people.append(name)

people.sort()
print(people)

place = people.index(name) + 1
print(place)

sets = math.ceil(place / agents)
print(sets)

time = sets * 20
print(time)