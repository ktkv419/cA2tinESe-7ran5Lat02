import json, os

current_dir = os.path.dirname(__file__)  # Get the directory of the current file
assets_path = os.path.join(current_dir, "../assets/leet_dict.json")  # Build the path to


def leet(text):
    with open(assets_path, "r") as file:
        leet_dict = json.load(file)

    leet_text = "".join(leet_dict.get(char, char) for char in text)

    return leet_text
