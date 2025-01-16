import csv

input_file = 'input.csv'
output_file = 'output.csv'

with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for row in reader:
        attr4_values = row['Attr4'].split('|')
        if len(attr4_values) > 1:
            for value in attr4_values:
                new_row = row.copy()
                new_row['Attr4'] = value
                writer.writerow(new_row)
        else:
            writer.writerow(row)