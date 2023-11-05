'''
we skip header
'''
import csv

file_path = '/home/art/tmp/artist.csv'

# Open file
with open( file_path ) as file_obj:
    # Skips the heading
    # Using next() method
    heading = next(file_obj)

    # Create reader object by passing the file
    # object to reader method
    reader_obj = csv.reader(file_obj)

    # Iterate over each row in the csv file
    # using reader object
    for row in reader_obj:
        print(row)