import csv

with open('profiles1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["name artisst", "name song", "enveloppe"]
    
    writer.writerow(field)
    writer.writerow(["Oladele Damilola", "40", "Nigeria"])
    writer.writerow(["Alina Hricko", "23", "Ukraine"])
    writer.writerow(["Isabel Walter", "50", "United Kingdom"])
