import csv
import json

# Define the input CSV file and the output JSON file
input_file = 'INPUT.csv'
output_file = 'OUTPUT.json'

# List to hold all JSON objects
json_data = []

# Open the CSV file and read the data
with open(input_file, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
   # Loop through each row in the CSV file
    for row in csvreader:
        # Create a dictionary for each row with the required format
        json_row = {
            "Name": f"{row['Parents']}",
            "Child": f"{row['Child']}",
            #"Age": f"{row['Age']}",
            "Location": row['Location'],
            "lat": row['"lat"'].replace('"', ''),
            "lng": row['"lng"'].replace('"', ''),
            #"Date": row['"Date"'].replace('"', ''),
            "Date": row['Date'],
            "url": row['url'],
            "PageNumber": row['"Page Number"'].replace('"', '')
        }
        # Add the dictionary to the list
        json_data.append(json_row)

# Write the list of dictionaries to the output JSON file
with open(output_file, 'w', encoding='utf-8') as jsonfile:
    json.dump(json_data, jsonfile, indent=4)

print("CSV data has been converted to JSON format and saved to", output_file)
