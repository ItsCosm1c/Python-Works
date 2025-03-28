#Week 9 Homework
#Badge C7-1 (Random)

import random

random_name = input('Please enter a Villager Name:\n>> ')

personalities = ['Normal', 'Lazy', 'Sisterly', 'Snooty', 'Cranky', 'Jock','Peppy', 'Smug']
hobbies = ['Education', 'Fashion', 'Fitness', 'Music', 'Nature', 'Playing']

per_num = random.randint(0, len(personalities) - 1) #(C7-1)
hob_num = random.randint(0, len(hobbies) - 1)

per = personalities[per_num]
hob = hobbies[hob_num]

print(f'{random_name} is {per} and into {hob}')