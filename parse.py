import requests
import bs4
import json

# Constants to access a music catalogue
URL = "https://ru.hitmotop.com/search?q="
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/96.0.4664.174 YaBrowser/22.1.4.840 Yowser/2.5 Safari/537.36",
    "accept": "*/*",
}


def parse(plain_html: requests.Response):
    """
    Find url of .mp3 file
    :param plain_html: requested html
    :return: url
    """
    soup = bs4.BeautifulSoup(plain_html.text, "html.parser")
    audio_info = soup.find("li", {"class": "tracks__item track mustoggler"})
    audio_dict = json.loads(audio_info['data-musmeta'])
    return audio_dict['url']


def request_page(song_name: str):
    """
    Requests page with songs
    :param song_name: name of song user wants to find
    :return: url of .mp3 file
    """
    requested_html = requests.get(f"{URL}{'+'.join(song_name.split())}",
                                  headers=HEADERS, params=None)
    return parse(requested_html)
