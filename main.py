import random
from collections import Counter
from tabulate import tabulate
import csv

# Function to randomly assign balanced pairs
def generate_balanced_pairs(people, num_pairs):
    # Calculate the base number of pairs each person should have
    base_pairs = (num_pairs * 2) // len(people)
    # Calculate the number of people who will have one extra pair
    extra_pairs = (num_pairs * 2) % len(people)

    # Initialize the person count dictionary, assigning each person the base number of pairs
    person_count = {person: base_pairs for person in people}

    # Distribute the extra pairs to the first `extra_pairs` people
    for i in range(extra_pairs):
        person_count[people[i]] += 1

    # Flatten the list of people based on the number of pairs they should have
    available_people = []
    for person, count in person_count.items():
        available_people.extend([person] * count)

    # Shuffle the list of available people to randomize pairing
    random.shuffle(available_people)

    # Now, create pairs from the available people
    pairs = []
    while available_people:
        # Pop two people from the list to form a pair
        person1 = available_people.pop()
        person2 = available_people.pop()
        pairs.append((person1, person2))

    return pairs

# Function to load categories from a file
def load_categories(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        # Read and return each line (category) from the file, excluding empty lines
        return [line.strip() for line in f if line.strip()]

# Function to save the pairs and categories to a CSV file
def save_to_csv(filename, categories, pairs):
    with open(filename, 'w', newline="", encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header row to the CSV
        writer.writerow(['No.', 'Category', 'Person 1', 'Person 2'])
        # Write each pair along with its category to the CSV
        for i, (category, pair) in enumerate(zip(categories, pairs), start=1):
            writer.writerow([i, category, pair[0], pair[1]])




# Define the number of people and pairs
num_people = 6  # Number of people to assign category
num_pairs = 50  # Number of pairs to generate
work_with_file = True   # Set to True to work with file (load categories from file and save results),
                        # False for console output only


# people = ['Person1', 'Person2', 'Person3', 'Person4', 'Person5', 'Person6']
# Create a list of people based on the num_people
people = []
for person in range(num_people):
    people.append("Person" + str(person))

# Generate the balanced pairs
pairs = generate_balanced_pa irs(people, num_pairs)

# Count the occurrences of each person in the pairs
count = Counter([person for pair in pairs for person in pair])
# Number each pair for display purposes
numbered_pairs = [(i + 1, pair[0], pair[1]) for i, pair in enumerate(pairs)]

if(work_with_file):
    # Load categories from the file 'games_genre.txt'
    categories = load_categories('games_genre.txt')
    # Save the results to a CSV file
    save_to_csv('wyniki.txt', categories, numbered_pairs)
else:
    # Print results in terminal using tabulate
    print("Pairs:")
    print(tabulate(numbered_pairs, headers=['No.', 'Person 1', 'Person 2'], tablefmt='pretty'))
    print("\nOccurrences:")
    print(tabulate(count.items(), headers=['Person', 'Occurrences'], tablefmt='pretty'))