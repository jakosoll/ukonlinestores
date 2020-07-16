
import json

def convert_text_to_json():
    with open('payloads.txt', 'r') as f:
        new_dict = {}
        for line in f:
            try:
                first = line.split(':')[0].strip()
                second = line.split(':')[1].strip()
                try:
                    second = int(second)
                except ValueError:
                    pass
                new_dict[first] = second
            except Exception as e:
                print(e)
        return new_dict


def save_to_json(file, dictionary):
    with open(file, 'w', encoding='utf-8') as file:
        json.dump(dictionary, file)




if __name__ == "__main__":
   d = convert_text_to_json()
   save_to_json('../payloads.json', d)
