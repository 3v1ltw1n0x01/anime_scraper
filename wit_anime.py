import json
import base64
import requests
from bs4 import BeautifulSoup

server = "https://witanime.art/"


def get_soup(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    return soup


def extract_episodes(items):
    episodes = []

    for item in items:
        card_title = item.select(".anime-card-title h3 > a")
        episode = {}

        if card_title:
            episode["name"] = card_title[0].text
            episode["anime_url"] = card_title[0]["href"]

        episode["episode"]     = item.select("h3 > a")[0].text
        episode["alt"]         = item.select(".img-responsive")[0]["alt"]
        episode["src"]         = item.select(".img-responsive")[0]["src"]
        episode["episode_url"] = item.select("h3 > a")[0]["href"]

        episodes.append(episode)

    return episodes


def extract_results(items):
    shows = []

    for item in items:
        card_title = item.select(".anime-card-title")[0]["data-content"]
        show = {
            "name"   : item.select("h3 > a")[0].text,
            "url"    : item.select("h3 > a")[0]["href"],
            "img"    : item.select(".img-responsive")[0]["src"],
            "type"   : item.select(".anime-card-type a")[0].text,
            "status" : item.select(".anime-card-status a")[0].text,
            "story"  : card_title,
        }
        shows.append(show)

    return shows


def select_soup(param, selector):
    url = f"{server}{param}"
    soup = get_soup(url)
    items = soup.select(selector)
    return extract_episodes(items) if extract_episodes(items) else extract_results(items)


def latest_episodes():
    return select_soup("episode", ".anime-card-container")


def search_anime(name):
    return select_soup(f"?search_param=animes&s={name}", ".anime-card-container")


def get_episodes(aid):
    return select_soup(f"anime/{aid}", ".episodes-card")


def get_episode_dl(eid):
    url = f"{server}episode/{eid}"
    soup = get_soup(url)
    return extract_qualities(soup)


def fetch_seasonals():
    m_soup = get_soup(server)
    m_link = m_soup.select("#menu-item-107 a")[0]["href"]
    soup = get_soup(m_link)
    items = soup.select(".anime-card-container")
    return extract_results(items)


def extract_qualities(html):
    qualities = {}
    quality_elements = html.find_all("ul", class_="quality-list")

    for quality_element in quality_elements:
        quality_name = quality_element.find("li").text
        links = quality_element.find_all("a")
        download_links = []

        for link in links:
            decoded_url = base64.urlsafe_b64decode(link["href"]).decode("utf-8")
            download_links.append(decoded_url)

        qualities[quality_name] = download_links

    return qualities


def get_anime_info(aid):
    url = f"{server}/anime/{aid}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    anime_info = {}
    anime_info["title"] = soup.find("h1", class_="anime-details-title").text.strip()
    anime_info["genres"] = [
        genre.text for genre in soup.find("ul", class_="anime-genres").find_all("a")
    ]

    story = soup.find("p", class_="anime-story").text.strip()
    anime_info["story"] = translate_info(story)

    details = soup.find_all("div", class_="anime-info")

    for detail in details:
        key = detail.find("span").text.strip()
        value = (
            detail.find("a").text.strip()
            if detail.find("a")
            else detail.contents[-1].strip()
        )
        key = translate_info(key)
        anime_info[key] = value

    return anime_info


def translate_info(text):
    translation_dictionary = {
        "النوع:"       : "type",
        "بداية العرض:"  : "start_date",
        "حالة الأنمي:"   : "status",
        "عدد الحلقات:"   : "episodes_count",
        "مدة الحلقة:"   : "episode_duration",
        "الموسم:"      : "season",
        "المصدر:"      : "source",
    }

    return translation_dictionary.get(text, text)
