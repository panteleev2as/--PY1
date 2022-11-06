import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file: str, delimiter: str = ",", new_line: str = "\n") -> list[dict]:
    with open(file, "rt") as f:
        list_of_lists = [i.split(delimiter) for i in f.read().split(new_line) if i]
        list_of_headers = list_of_lists[0]
        list_of_values = list_of_lists[1:]
        output_list = []
        for line in list_of_values:
            output_list.append({list_of_headers[i]: value for i, value in enumerate(line)})
        return output_list

    # TODO реализовать конвертер из csv в json

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
