import json
from typing import Dict, Any, List
from pathlib import Path
from logger import logger


def save_products_to_json(products: List[Dict[str, Any]], data_dir: Path):
    """
    Saves a list of product dictionaries to a JSON file.

    Parameters:
        products (List[Dict[str, Any]]): List of product dictionaries to be saved.
        data_dir (Path): Directory where the JSON file will be saved.

    """
    # Creating a JSON file and writing the product data into it
    with open(data_dir / 'result.json', 'w') as f:
        json.dump(products, f, indent=4, ensure_ascii=False)

        # Logging that data has been saved
        logger.info('Data saved')
