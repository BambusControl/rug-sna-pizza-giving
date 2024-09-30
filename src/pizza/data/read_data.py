import json
from pathlib import Path

from src.pizza.data import PizzaRequest


def read_data(data_path) -> list[PizzaRequest]:
    filepath = Path.cwd() / Path(data_path)

    if not filepath.exists():
        raise FileNotFoundError(
            f"File not found: {filepath}; " +
            f"Current working directory: {Path.cwd()}; " +
            f"Relative path to data file: {Path(data_path)}"
        )

    print(f"Using file: {filepath.absolute()}")

    with filepath.open("r", encoding="UTF-8") as file:
        raw_data = json.load(file)
        # Turn loaded dict into a list of PizzaRequest objects
        return [
            PizzaRequest(**datapoint)
            for datapoint
            in raw_data
        ]
