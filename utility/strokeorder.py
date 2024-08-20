import requests
from bs4 import BeautifulSoup
import os
import json


def download_characters():
    with open('source.json') as f:
        d: list[str] = json.load(f)
        for character in d:
            if len(character) != 1:
                splitted = list(character)
                for char in splitted:
                    scrape_stroke_order(char)
            else:
                scrape_stroke_order(char)


def scrape_stroke_order(input_string):
    url = f"https://www.strokeorder.com/chinese/{input_string}"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed. Status code: {response.status_code}")

    soup = BeautifulSoup(response.content, 'html.parser')
    download_link = soup.find('a', href=lambda href: href and "pdf" in href)
    pdf_url = download_link['href']
    full_pdf_url = f"https://www.strokeorder.com{pdf_url}"
    download_folder = "./downloads"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    pdf_response = requests.get(full_pdf_url)
    if pdf_response.status_code == 200:
        pdf_filename = os.path.join(download_folder, input_string+".pdf")
        with open(pdf_filename, 'wb') as f:
            f.write(pdf_response.content)
        print(f"Downloaded: {pdf_filename}")

    title = soup.title.string
    print(f"Title of the page: {title}")
