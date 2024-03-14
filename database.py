import csv

with open('profiles1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["artist name", "song name", "enveloppe"]
    # l'enveloppe est un array 2D avec les fingerprints
    
    writer.writerow(field)
    writer.writerow(["Bakermat", "You Got Me Where You Want", ""])
    writer.writerow(["Eminem", "Love Yourself", ""])
    writer.writerow(["Fred Again", "Delilah", ""])
    writer.writerow(["Maneskin", "Gasoline", ""])
    writer.writerow(["Mome", "Aloha", ""])
    writer.writerow(["Steve Wonder", "Part Time Lover", ""])
    writer.writerow(["The Rolling Stones", "Satisfaction", ""])
    writer.writerow(["The Weeknd", "Save Your Tears", ""])
    writer.writerow(["TRYM", "Falling Star", ""])

