import requests
from lxml import html


def get_current_chapter(url):
    res = requests.get(url)
    page = html.document_fromstring(res.text)
    path = '/html/body/div[3]/div/div[2]/div[3]/section[1]/div[2]/div[1]/div[2]/a'
    return page.xpath(path)[0].text.replace('\n', '').replace(' ', '', 11).strip()


def main():
    print(get_current_chapter("https://mangalib.me/castle-swimmer"))



if __name__ == '__main__':
    main()

# json.dump(lst, fw, ensure_ascii=False, sort_keys=True, indent='\t', separators=(',', ':'))
# TODO программа должна уведомлять пользователя о выходе новой главы определённой манги через панель уведомлений
