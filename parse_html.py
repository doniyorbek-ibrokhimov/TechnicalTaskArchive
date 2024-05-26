from typing import List, Dict, Any, Union
from bs4 import BeautifulSoup
from logger import logger


def process_page(html: str) -> Union[List[Dict[str, Any]], None]:
    """
    Processes HTML content of a page to extract product information.

    Parameters:
        html (str): HTML content of the page.

    Returns:
        Union[List[Dict[str, Any]], None]: List of parsed product dictionaries or None if the page is not found (404).

    """
    # Creating a BeautifulSoup object to parse HTML
    soup = BeautifulSoup(html, 'lxml')

    # Checking if the page is a 404 error page
    is_404 = soup.find('body', class_='error404')
    if is_404 is not None:
        logger.warn('Page not found')
        return None

    # Finding all product elements on the page
    products = soup.find_all('li', class_='product')

    # List to store parsed product dictionaries
    parsed_products: List[Dict[str, Any]] = []

    # Iterating through each product element
    for product in products:
        # Extracting product attributes
        id_ = product.find('a', class_='button').get('data-product_id')
        if id_ is not None:
            id_ = int(id_)
        sku = product.find('a', class_='button').get('data-product_sku')
        name = product.find('h2', class_='woocommerce-loop-product__title').text
        price = product.find('span', class_='woocommerce-Price-amount').text
        img_src = product.find('img', class_='attachment-woocommerce_thumbnail').get('src')

        # Creating a dictionary for the product and adding it to the list of parsed products
        product_data = {
            'id': id_,
            'name': name,
            'price': price,
            'sku': sku,
            'image_url': img_src
        }
        parsed_products.append(product_data)

    return parsed_products  # Returning the list of parsed product dictionaries
