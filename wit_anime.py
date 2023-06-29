import requests
from bs4 import BeautifulSoup
import json


class WitAnime:
    def __init__(self):
        self.server = "https://witanime.com"

    def _get_soup(self, url):
        req = requests.get(url)
        soup = BeautifulSoup(req.content, "html.parser")
        return soup

    def _extract_episodes(self, items):
        episodes = []
        for item in items:
            card_title = item.select(".anime-card-title h3 > a")
            episode = {
                "name": card_title[0].text if card_title else "",
                "episode": item.select("h3 > a")[0].text,
                "alt": item.select(".img-responsive")[0]["alt"],
                "src": item.select(".img-responsive")[0]["src"],
                "anime_url": card_title[0]["href"] if card_title else "",
                "episode_url": item.select("h3 > a")[0]["href"],
                "download_links": self.get_episode_dl(item.select("h3 > a")[0]["href"]),
            }
            episodes.append(episode)
        return episodes

    def _extract_results(self, items):
        shows = []
        for item in items:
            card_title = item.select(".anime-card-title")[0]["data-content"]
            show = {
                "name": item.select("h3 > a")[0].text,
                "url": item.select("h3 > a")[0]["href"],
                "img": item.select(".img-responsive")[0]["src"],
                "type": item.select(".anime-card-type a")[0].text,
                "status": item.select(".anime-card-status a")[0].text,
                "story": card_title,
            }
            shows.append(show)
        return shows

    def search_anime(self, text):
        url = f"{self.server}/?search_param=animes&s={text}"
        soup = self._get_soup(url)
        items = soup.select(".anime-card-container")
        return json.dumps(self._extract_results(items), ensure_ascii=False)

    def get_episodes(self, anime_id):
        url = f"{self.server}/anime/{anime_id}"
        soup = self._get_soup(url)
        items = soup.select(".episodes-card")
        return json.dumps(self._extract_episodes(items), ensure_ascii=False)

    def get_episode_dl(self, ep_id):
        url = f"{self.server}/episode/{ep_id}"
        soup = self._get_soup(url)
        items = soup.select('a.btn.btn-default[href*="drive.google.com"]')
        episodes = [item["href"] for item in items]
        return episodes

    def latest_episodes(self):
        url = f"{self.server}/episode"
        soup = self._get_soup(url)
        items = soup.select(".anime-card-container")
        return json.dumps(self._extract_episodes(items), ensure_ascii=False)

    def fetch_seasonals(self):
        m_soup = self._get_soup(self.server)
        m_link = m_soup.select("#menu-item-107 a")[0]["href"]
        soup = self._get_soup(m_link)
        items = soup.select(".anime-card-container")
        return json.dumps(self._extract_results(items), ensure_ascii=False)

    def get_anime_info(self, anime_id):
        url = f"{self.server}/anime/{anime_id}"
        soup = self._get_soup(url)
        key_mapping = {
            "النوع:": "type",
            "بداية العرض:": "start_date",
            "حالة الأنمي:": "status",
            "عدد الحلقات:": "episode_count",
            "مدة الحلقة:": "episode_duration",
            "الموسم:": "season",
            "المصدر:": "source",
        }

        title = soup.find("h1", class_="anime-details-title").text.strip()
        genres = [genre.text.strip() for genre in soup.select("ul.anime-genres a")]
        story = soup.find("p", class_="anime-story").text.strip()

        anime_info = {}
        info_items = soup.select(".anime-info")
        for item in info_items:
            key = item.find("span").text.strip()
            value = item.text.replace(key, "").strip()
            translated_key = key_mapping.get(key, key)
            anime_info[translated_key] = value

        data = {
            "title": title,
            "genres": genres,
            "story": story,
            "anime_info": anime_info,
        }
        return json.dumps(data, ensure_ascii=False)
