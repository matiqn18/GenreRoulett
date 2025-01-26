import csv
import random
from collections import Counter
from tabulate import tabulate

#fuction to random assing
def generate_balanced_pairs(people, num_pairs): 
    pairs = []
    occurrence_limit = (num_pairs * 2) // len(people)
    person_count = Counter()

    while len(pairs) < num_pairs:
        possible_pairs = [(a, b) for i, a in enumerate(people) for b in people[i + 1:]]
        random.shuffle(possible_pairs)
        for pair in possible_pairs:
            if len(pairs) >= num_pairs:
                break
            if person_count[pair[0]] < occurrence_limit and person_count[pair[1]] < occurrence_limit:
                pairs.append(pair)
                person_count[pair[0]] += 1
                person_count[pair[1]] += 1
    return pairs

people = ['Person1', 'Person2', 'Person3', 'Person4', 'Person5', 'Person6']
#number of category to randomly assign
num_pairs = 60 

pairs = generate_balanced_pairs(people, num_pairs)

count = Counter([person for pair in pairs for person in pair])
numbered_pairs = [(i + 1, pair[0], pair[1]) for i, pair in enumerate(pairs)]

#Print result in terminal using tabulate
print("Pairs:")
print(tabulate(numbered_pairs, headers=['No.', 'Person 1', 'Person 2'], tablefmt='pretty'))
print("\nOccurrences:")
print(tabulate(count.items(), headers=['Person', 'Occurrences'], tablefmt='pretty'))
