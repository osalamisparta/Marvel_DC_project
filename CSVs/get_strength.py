import json
import csv
import get_marvel_names

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


# Extracting only Marvel characters from 'character_strength_data' list
def get_marvel_characters(csv_file_name):
    marvel_character_data = []
    dc_character_data = []

    with open(csv_file_name, newline='') as csvfile:
        character_details = csv.reader(csvfile, delimiter=',')

        print(character_details)

        for character in character_details:
            # print(character[0])

            if character[0] in get_marvel_names.marvel_names_list:
                to_new_character_data = {
                    'name': character[0],
                    'strength': character[3]
                }
                marvel_character_data.append(to_new_character_data)
            else:
                to_new_character_data = {
                    'name': character[0],
                    'strength': character[3]
                }
                dc_character_data.append(to_new_character_data)

    print(marvel_character_data)
    print('------------------------------------')
    print(dc_character_data)

get_marvel_characters('charcters_stats.csv')