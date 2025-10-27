from tech_news.database import db


def top_5_categories() -> list[str]:
    """
    Finds the top 5 most frequent categories in the database.
    Sorts by frequency (desc) and then alphabetically (asc) for ties.
    """

    pipeline = [
        {
            "$group": {
                "_id": "$category",
                "count": {"$sum": 1},
            }
        },
        {
            "$sort": {
                "count": -1,
                "_id": 1,
            }
        },
        {"$limit": 5},
    ]

    try:

        results = db.news.aggregate(pipeline)

        top_categories = [result["_id"] for result in results if result["_id"]]

        return top_categories

    except Exception:
        return []
