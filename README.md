# 🎲 GenreRoulett - Balanced Pair Generator with Categories

This Python script generates a specified number of **balanced random pairs** from a given list of people. Each person is assigned to approximately the same number of pairs. Optionally, the script also assigns a **category** (e.g., genre, topic) to each pair and saves the results to a CSV file.

---

## ✅ Features

- Fair distribution – ensures each person appears in roughly the same number of pairs.
- Support for categories – assign external labels (e.g., game genres) to pairs.
- Output to terminal or `.csv` file.
- Works great for generating randomized assignments for games, debates, tasks, etc.

---

## 🛠 Usage

### Configuration

Edit the following variables in the script:

```python
num_people = 6       # Total number of people
num_pairs = 50       # Total number of pairs to generate
work_with_file = True  # If True, loads categories and saves to file
```

If work_with_file is True:

- Provide a games_genre.txt file with one category per line.
- Results will be saved to result.txt.

If False, the script prints all pairs and counts directly in the terminal.

Example (Terminal Output)
```bash
+-----+----------+----------+
| No. | Person 1 | Person 2 |
+-----+----------+----------+
|  1  | Person2  | Person4  |
|  2  | Person0  | Person1  |
...
+-----+----------+----------+

Occurrences:
+---------+--------------+
| Person  | Occurrences  |
+---------+--------------+
| Person0 |      17      |
| Person1 |      16      |
...
```

### 📂 Input Files
games_genre.txt – a list of categories (e.g., genres) used to label each pair.
```
FPS
Platformer
Puzzle
Horror
RPG
```

### 📦 Output File
```
No.,Category,Person 1,Person 2
1,FPS,Person0,Person3
2,Horror,Person2,Person1
...
```

## 👨‍💻 Author
Michał Łukaszczyk

## 📜 License
MIT License – feel free to use and modify.




