#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to JSON and saves it to a file.

    Parameters:
    data (dict): The Python dictionary to serialize.
    filename (str): The name of the output JSON file.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


def load_and_deserialize(filename):
    """
    Loads a JSON file and deserializes it to a Python dictionary.

    Parameters:
    filename (str): The name of the input JSON file.

    Returns:
    dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data


if __name__ == "__main__":
    # Sample data to be serialized
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Serialize the data to JSON and save it to a file
    serialize_and_save_to_file(data_to_serialize, 'data.json')

    # Output: The data has been serialized and saved to 'data.json'
    print("Data serialized and saved to 'data.json'.")

    # Load and deserialize data from 'data.json'
    deserialized_data = load_and_deserialize('data.json')

    # Output: The deserialized data
    print("Deserialized Data:")
    print(deserialized_data)
