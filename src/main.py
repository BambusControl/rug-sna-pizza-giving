import json
from pathlib import Path


def main(
        data_path: str
):
    data = read_data(data_path)

    print(data[0])


def read_data(data_path):
    filepath = Path.cwd() / Path(data_path)

    if not filepath.exists():
        raise FileNotFoundError(
            f"File not found: {filepath}; " +
            f"Current working directory: {Path.cwd()}; " +
            f"Relative path to data file: {Path(data_path)}"
        )

    print(f"Using file: {filepath.absolute()}")

    # Open and load the JSON file
    with filepath.open("r", encoding="UTF-8") as file:
        return json.load(file)


if __name__ == "__main__":
    main("./dataset/pizza_request_dataset.json")
