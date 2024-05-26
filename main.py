import asyncio
import time
from pathlib import Path
from fetch_products import fetch_all_products
from save_to_json import save_products_to_json
from logger import logger

BASE_URL = 'https://scrapeme.live/shop'
BASE_DIR = Path(__file__).resolve().parent
data_dir = BASE_DIR / 'data'
data_dir.mkdir(exist_ok=True)
ALL_COLLECTIONS_COUNT = 48


def main():
    """
    Main function to execute the parsing and saving process.
    """
    s_time = time.time()

    # Logging the start of the parsing process
    logger.info(f'Starting to parse [{BASE_URL}]')

    # Getting the event loop for asyncio
    loop = asyncio.get_event_loop()

    # Running the asynchronous fetching of products
    products = loop.run_until_complete(fetch_all_products(BASE_URL, ALL_COLLECTIONS_COUNT))

    # Saving the fetched products to a JSON file
    save_products_to_json(products, data_dir)

    # Logging the completion of the parsing process and the total execution time
    logger.info(f'Finished parsing [{BASE_URL}] in {(time.time() - s_time):.2f} seconds')


if __name__ == '__main__':
    main()
