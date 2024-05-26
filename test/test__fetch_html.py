import pytest
from aiohttp import ClientSession
from aioresponses import aioresponses
from fetch_html import get_html
from main import BASE_URL, BASE_DIR


@pytest.mark.asyncio
async def test_get_html_success():
    url = BASE_URL
    html_path = BASE_DIR / 'test' / 'home_page.html'
    html_content = html_path.read_text()

    with aioresponses() as mock:
        mock.get(url, status=200, body=html_content)

        async with ClientSession() as session:
            response = await get_html(session, url)
            assert response == html_content


@pytest.mark.asyncio
async def test_get_html_failure():
    url = BASE_URL + '404'
    with aioresponses() as mock:
        mock.get(url, status=404)

        async with ClientSession() as session:
            with pytest.raises(Exception):
                await get_html(session, url)
