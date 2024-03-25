import csv
import numpy as np

def read_chromagrams_from_csv(csv_file):
    chromagrams = []
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 3:  # Ensure the row has at least three elements
                artist_name = row[0]
                song_name = row[1]
                chromagram_str = row[2]
                # Convert the string representation of chromagram back to numpy array
                chromagram = np.array(eval(chromagram_str))
                chromagrams.append((artist_name, song_name, chromagram))
    return chromagrams

# Example usage:
chromagrams = read_chromagrams_from_csv('profiles2.csv')

# Now you can loop through the list of chromagrams
for artist_name, song_name, chromagram in chromagrams:
    print(f"Artist: {artist_name}, Song: {song_name}")
    print(chromagram)
