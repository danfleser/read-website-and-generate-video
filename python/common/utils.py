import io
import json
import os
import re


def is_file_broken_size(path):
    is_file_broken = False

    generated_file_size = os.path.getsize(path)
    if generated_file_size < 100:
        is_file_broken = True

    return is_file_broken


def write_json_file(json_file_path, data):
    with io.open(json_file_path, 'w', encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_json_file(json_file_path):
    with io.open(json_file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)

    return data


def remove_alphanumeric_chars_from_string(text):
    return re.sub("[^a-zA-Z0-9]+", "", str(text))
