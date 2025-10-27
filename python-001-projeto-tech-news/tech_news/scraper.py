import time
import requests
from bs4 import BeautifulSoup
from tech_news.database import create_news

STATUS_CODE = 200
TIMEOUT = 3
SLEEP_TIME = 1


def fetch(url):
    """Seu código deve vir aqui"""
    headers = {"user-agent": "Fake user-agent"}

    try:
        time.sleep(SLEEP_TIME)
        response = requests.get(url, headers=headers, timeout=TIMEOUT)

        if response.status_code == STATUS_CODE:
            return response.text
        return None
    except (requests.Timeout, requests.RequestException):
        return None


def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    soup = BeautifulSoup(html_content, "html.parser")
    link_tags = soup.find_all("a", class_="cs-overlay-link")
    url_links = [link.get("href") for link in link_tags]
    return url_links


def scrape_next_page_link(html_content: str) -> str | None:
    """
    Scrapes the URL for the "next page" link from the homepage HTML
    using BeautifulSoup.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    next_page_tag = soup.find("a", class_=["next", "page-numbers"])
    if next_page_tag:
        return next_page_tag.get("href")
    else:
        return None


def scrape_news(html_content: str) -> dict | None:
    """
    Scrapes all details from a single news page HTML
    using BeautifulSoup.
    """
    soup = BeautifulSoup(html_content, "html.parser")

    url_tag = soup.find("link", rel="canonical")
    url = url_tag.get("href") if url_tag else None

    title_tag = soup.find("h1", class_="entry-title")
    title = title_tag.get_text().strip() if title_tag else None

    timestamp_tag = soup.find("li", class_="meta-date")
    timestamp = timestamp_tag.get_text() if timestamp_tag else None

    writer_tag = soup.find("span", class_="author")
    writer = (
        writer_tag.find("a").get_text()
        if (writer_tag and writer_tag.find("a"))
        else None
    )

    reading_time_tag = soup.find("li", class_="meta-reading-time")
    reading_time = 0
    if reading_time_tag:
        try:

            time_text = reading_time_tag.get_text()
            reading_time = int(time_text.split()[0])
        except (ValueError, IndexError):
            reading_time = 0

    summary_p = soup.find("div", class_="entry-content").find("p")
    summary = summary_p.get_text().strip() if summary_p else None

    category_tag = soup.find("div", class_="meta-category")
    category = (
        category_tag.find("span", class_="label").get_text()
        if (category_tag and category_tag.find("span", class_="label"))
        else None
    )

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


def _scrape_all_links(n: int) -> list[str]:
    """
    Função auxiliar para coletar 'n' links de notícias,
    cuidando da paginação.
    """
    BASE_URL = "https://blog.betrybe.com"
    current_url = BASE_URL
    all_news_links = []

    while len(all_news_links) < n:
        html_content = fetch(current_url)

        if not html_content:
            break

        all_news_links.extend(scrape_updates(html_content))

        current_url = scrape_next_page_link(html_content)

        if not current_url:
            break

    return all_news_links[:n]


def _scrape_news_data(news_links: list[str]) -> list[dict]:
    """
    Função auxiliar para raspar os dados de uma lista de links.
    """
    scraped_news_list = []

    for link in news_links:
        news_html = fetch(link)
        if news_html:
            news_data = scrape_news(news_html)
            if news_data:
                scraped_news_list.append(news_data)

    return scraped_news_list


def get_tech_news(n: int) -> list[dict]:
    """
    Orquestra a busca, raspagem e salvamento de 'n' notícias.
    """

    required_links = _scrape_all_links(n)

    scraped_news = _scrape_news_data(required_links)

    if scraped_news:
        create_news(scraped_news)

    return scraped_news
