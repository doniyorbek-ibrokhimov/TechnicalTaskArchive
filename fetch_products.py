import asyncio
from typing import List, Dict, Any
import aiohttp
from fetch_html import get_html
from parse_html import process_page
from logger import logger


async def fetch_all_products(base_url: str, all_collections_cnt: int) -> List[Dict[str, Any]]:
    """
    Asynchronously fetches and processes HTML pages containing product information.

    Parameters:
        base_url (str): Base URL for the product pages.
        all_collections_cnt (int): Total number of collections to fetch.

    Returns:
        List[Dict[str, Any]]: List of parsed product dictionaries.

    """
    # List to store parsed product dictionaries
    parsed_products: List[Dict[str, Any]] = []
    # Set to keep track of unique product IDs
    seen_ids = set()

    # Creating an aiohttp ClientSession context
    async with aiohttp.ClientSession() as session:
        tasks = []
        # Creating tasks for fetching HTML content for each collection page
        for i in range(1, all_collections_cnt + 1):
            url = f'{base_url}/page/{i}/'
            tasks.append(get_html(session, url))

        # Gathering HTML content from all tasks concurrently
        pages = await asyncio.gather(*tasks)

        # Processing each HTML page and extracting product information
        for i, html in enumerate(pages):
            products = process_page(html)
            logger.info(f'Page {i + 1}')

            if products is not None:
                # Iterating through products on the page
                for product in products:
                    # Checking if product ID is not already seen
                    if product['id'] not in seen_ids:
                        # Adding product ID to the set of seen IDs
                        seen_ids.add(product['id'])
                        # Adding parsed product to the list
                        parsed_products.append(product)

    # Returning the list of parsed product dictionaries
    return parsed_products
