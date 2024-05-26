from aiohttp import ClientSession
from logger import logger


async def get_html(session: ClientSession, url: str) -> str:
    """
    Asynchronous function to fetch HTML content from a given URL using aiohttp.

    Parameters:
        session (ClientSession): aiohttp ClientSession instance.
        url (str): URL from which to fetch HTML content.

    Returns:
        str: HTML content of the response.

    Raises:
        Exception: If fetching HTML content fails.
    """

    # Sending an HTTP GET request to the provided URL using the aiohttp session.
    async with session.get(url) as response:
        try:
            # Checking if the response status code indicates a successful request.
            response.raise_for_status()
            # If successful, returning the HTML content of the response.
            return await response.text()
        except Exception as e:
            # If an exception occurs during the request, logging the error and re-raising it.
            logger.error(f'Failed to fetch [{url}]')
            raise e
