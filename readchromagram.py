import csv
import numpy as np

def read_constellation_from_csv(csv_file):
    constellation = []
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 3:  # Ensure the row has at least three elements
                artist_name = row[0]
                song_name = row[1]
                constellation_str = row[2]
                # Convert the string representation of constellation back to numpy array
                constellation = np.array(eval(constellation_str))
                constellations.append((artist_name, song_name, constellation))
    return constellations

# Example usage:
constellations = read_constellations_from_csv('profiles2.csv')

# Now you can loop through the list of constellations
for artist_name, song_name, constellation in constellations:
    print(f"Artist: {artist_name}, Song: {song_name}")
    print(chromagram)
