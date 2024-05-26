# Technical Task Archive

This repository contains the solution for the technical task provided as part of the job application process. 
The task involves developing a web scraper to extract pokemon information from [ScrapeMe](https://scrapeme.live/shop) and saving it to a JSON file.

## Overview

The task is divided into several components:

1. **Fetching HTML**: The `fetch_html.py` module utilizes the `aiohttp` library to asynchronously fetch HTML content from a given URL.

2. **Parsing HTML**: The `parse_html.py` module uses `BeautifulSoup` to parse HTML content and extract product information from the page.

3. **Saving to JSON**: The `save_to_json.py` module saves the parsed pokemon data to a JSON file.

4. **Main Script**: The `main.py` script orchestrates the execution of fetching, parsing, and saving processes for multiple pages of pokemon collections.

## Usage

To run the scraper:

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/doniyorbek-ibrokhimov/TechnicalTaskArchive.git
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Execute the main script:

    ```
    python main.py
    ```

4. Check the `data` directory for the saved JSON file containing the product information.

## Project Structure

- `fetch_html.py`: Contains a function to fetch HTML content asynchronously using `aiohttp`.
- `parse_html.py`: Defines a function to parse HTML content using `BeautifulSoup` and extract product information.
- `save_to_json.py`: Provides a function to save parsed product data to a JSON file.
- `main.py`: Entry point script that orchestrates the fetching, parsing, and saving processes.
- `logger.py`: Configuration for logging.
- `data/`: Directory to store the saved JSON file.
- `requirements.txt`: List of project dependencies.

## Requirements

- Python 3.6+
- `aiohttp`
- `beautifulsoup4`
- `lxml`

## Author

[Doniyorbek Ibrokhimov](https://github.com/doniyorbek-ibrokhimov)

## License

This project is licensed under the [MIT License](LICENSE).
