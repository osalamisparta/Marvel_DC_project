import json
import csv


def transform_data(csv_file_name):
    selected_data = []

    # Gathering data into a List containing Dict items
    with open(csv_file_name, newline='') as csvfile:
        character_details = csv.reader(csvfile, delimiter=',')

        for character in character_details:
            to_selected_data = {
                'name': character[0],
                'intelligence': character[2],
                'combat': character[7]
            }

            selected_data.append(to_selected_data)

    # Create a JSON file containing details gathered from above
    with open('intelligence_vs_comabt.json', 'w') as jsonfile:
        jsonfile.write(json.dumps(selected_data))

    print(selected_data)


transform_data('charcters_stats.csv')
