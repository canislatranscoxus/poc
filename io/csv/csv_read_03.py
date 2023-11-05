'''
we read line as dictionary
'''
import csv

file_path = '/home/art/tmp/artist.csv'

with open( file_path ) as file_obj:
    # Create reader object by passing the file
    # object to DictReader method
    reader_obj = csv.DictReader(file_obj)

    # Iterate over each row in the csv file
    # using reader object
    for row in reader_obj:
        print(row)