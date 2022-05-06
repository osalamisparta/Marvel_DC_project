import requests
import json
import csv

def transform_data(csv_file_name):
    selected_data = []
    with open(csv_file_name, newline='') as csvfile:
        character_details = csv.reader(csvfile, delimiter=',')

        for character in character_details:
            to_selected_data = []
            to_selected_data.append(character[0])
            to_selected_data.append(character[3])

            selected_data.append(to_selected_data)

    print(selected_data)


transform_data('charcters_stats.csv')