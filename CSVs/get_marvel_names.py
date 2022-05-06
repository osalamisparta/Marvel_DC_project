import csv

def transform_data(csv_file_name):
    selected_data = []

    with open(csv_file_name, newline='') as csvfile:
        character_details = csv.reader(csvfile, delimiter=',')

        for character in character_details:
            selected_data.append(character[1])

    print(selected_data)


transform_data('marvel_characters_info.csv')