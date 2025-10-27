from datetime import datetime
import re
from tech_news.database import db


def search_by_title(title: str) -> list[tuple[str, str]]:
    """
    Searches news by title (case-insensitive) in the database.
    """
    try:
        query = {"title": {"$regex": re.escape(title), "$options": "i"}}

        search_results = db.news.find(query)

        formatted_results = []
        for news in search_results:
            formatted_results.append((news["title"], news["url"]))

        return formatted_results

    except Exception:
        return []


def search_by_date(date: str) -> list[tuple[str, str]]:
    """
    Searches news by date (ISO format YYYY-MM-DD).
    Converts to dd/mm/AAAA format for DB query.
    Raises ValueError for invalid date formats.
    """
    try:
        iso_date = datetime.strptime(date, "%Y-%m-%d")
        db_date_format = iso_date.strftime("%d/%m/%Y")

    except ValueError:
        raise ValueError("Data inválida")

    query = {"timestamp": db_date_format}
    search_results = db.news.find(query)

    formatted_results = []
    for news in search_results:
        formatted_results.append((news["title"], news["url"]))

    return formatted_results


def search_by_category(category: str) -> list[tuple[str, str]]:
    """
    Searches news by category (case-insensitive) in the database.
    """
    try:
        query = {"category": {"$regex": re.escape(category), "$options": "i"}}

        search_results = db.news.find(query)

        formatted_results = []
        for news in search_results:
            formatted_results.append((news["title"], news["url"]))

        return formatted_results

    except Exception:
        return []
