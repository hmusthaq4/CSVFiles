import csv

with open('RentPrices.csv', newline='', encoding='utf-8') as infile, open('FilteredRentPrices.csv', 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
        if row['city'] in ['Bangalore', 'Chennai']:
            writer.writerow(row)