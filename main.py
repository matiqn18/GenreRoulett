import random
from collections import Counter
from tabulate import tabulate


# Function to randomly assign balanced pairs
def generate_balanced_pairs(people, num_pairs):
    # Calculate the base number of pairs each person should have
    base_pairs = (num_pairs * 2) // len(people)
    # Calculate the number of people who will have one extra pair
    extra_pairs = (num_pairs * 2) % len(people)

    # Initialize the person count dictionary
    person_count = {person: base_pairs for person in people}

    # Distribute the extra pairs to the first `extra_pairs` people
    for i in range(extra_pairs):
        person_count[people[i]] += 1

    # Flatten the list of people based on their pair count
    available_people = []
    for person, count in person_count.items():
        available_people.extend([person] * count)

    # Shuffle the list of people to randomize pairing
    random.shuffle(available_people)

    # Now, create pairs from the available people
    pairs = []
    while available_people:
        person1 = available_people.pop()
        person2 = available_people.pop()
        pairs.append((person1, person2))

    return pairs



num_people = 6 # Number of people to assign category

num_pairs = 50  # Number of pairs to generate

# people = ['Person1', 'Person2', 'Person3', 'Person4', 'Person5', 'Person6']
people = []
for person in range(num_people):
    people.append("Person"+str(person))
pairs = generate_balanced_pairs(people, num_pairs)

# Count the occurrences of each person in the pairs
count = Counter([person for pair in pairs for person in pair])
numbered_pairs = [(i + 1, pair[0], pair[1]) for i, pair in enumerate(pairs)]

# Print results in terminal using tabulate
print("Pairs:")
print(tabulate(numbered_pairs, headers=['No.', 'Person 1', 'Person 2'], tablefmt='pretty'))
print("\nOccurrences:")
print(tabulate(count.items(), headers=['Person', 'Occurrences'], tablefmt='pretty'))
