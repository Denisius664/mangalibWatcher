import feedparser
import re

import pprint

class MangaLibRSS:

    def __init__(self, *watch_list):
        self.watch_list = watch_list
        self.last_links = {}

        for link in self.watch_list:
            if "https://mangalib.me/manga-rss/" not in link:
                raise Exception(link + " - it is not MangaLibRSS link")

        for link in self.watch_list:
            rss = feedparser.parse(link)
            self.last_links[rss.feed.title] = rss.entries[0].link

    def get_updates(self):
        r = {}

        for link in self.watch_list:
            rss = feedparser.parse(link)
            title = rss.feed.title
            item = rss.entries[0]
            cur_link = item.link

            if self.last_links[title] != cur_link:
                r[title] = {
                    "name": title[6:],
                    "volume": re.search(r"/v(\d+)/", cur_link).group(1),
                    "chapter": re.search(r"/c(\d+)", cur_link).group(1),
                    "chapter_name": item.summary,
                    "chapter_link": cur_link,
                    "link": re.sub(r"/v.+/c.+", "", cur_link),
                    "published": item.published
                }

                self.last_links[title] = cur_link

        return r

    def get_last(self):
        r = {}

        for link in self.watch_list:
            rss = feedparser.parse(link)
            title = rss.feed.title
            item = rss.entries[0]
            cur_link = item.link

            r[title] = {
                "name": title[6:],
                "volume": re.search(r"/v(\d+)/", cur_link).group(1),
                "chapter": re.search(r"/c(\d+)", cur_link).group(1),
                "chapter_name": item.summary,
                "chapter_link": cur_link,
                "link": re.sub(r"/v.+/c.+", "", cur_link),
                "published": item.published
            }

        return r
if __name__ == '__main__':
    links = (
        "https://mangalib.me/manga-rss/tapir-edge",
        "https://mangalib.me/manga-rss/yakusoku-no-neverland",
        "https://mangalib.me/manga-rss/dr-stone",
        "https://mangalib.me/manga-rss/ijiranaide-nagatoro-san",
        "https://mangalib.me/manga-rss/lv2-kara-cheat-datta-moto-yuusha-kouho-no-mattari-isekai-life",
    )

    rss = MangaLibRSS(*links)
    pprint.pprint(rss.get_last())
