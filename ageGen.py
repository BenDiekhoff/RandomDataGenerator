
import random
import os
import math

age = os.path.dirname(__file__) + '/ages.txt'

POPULATION = 1000

AGES = [17,24,34,44,54,64,116]
RANGES = [(13,17),(18,24),(25,34),(35,44),(45,54),(55,64),(65,116)]
PER = [.058,.25,.322,.165,.102,.06,.043] # added 0.002 to index 2 this to make the total 100%

agelist = []


for i in range (len(AGES)):
    for x in range (int(POPULATION * PER[i])):
        agelist.append(random.randint(RANGES[i][0], RANGES[i][1]))

with open(age,'w+',encoding='utf-8') as file:
    for age in agelist:
        file.write(str(age) + '\n')

