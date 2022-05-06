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

            to_selected_data_dict = {
                'name': character[0],
                'strength': character[3]
            }

            selected_data.append(to_selected_data_dict)
            # selected_data.append(to_selected_data)

    # print(selected_data)
    return selected_data


character_strength_data = transform_data('charcters_stats.csv')


# Turning data into a JSON file
with open('character_strength.json', 'w') as jsonfile:
    jsonfile.write(json.dumps(character_strength_data))