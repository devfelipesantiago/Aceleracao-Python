import pytest
from unittest.mock import patch
from tech_news.analyzer.reading_plan import ReadingPlanService


MOCK_DB_NEWS = [
    {"title": "Notícia A (8 min)", "reading_time": 8},
    {"title": "Notícia B (2 min)", "reading_time": 2},
    {"title": "Notícia D (5 min)", "reading_time": 5},
    {"title": "Notícia E (3 min)", "reading_time": 3},
    {"title": "Notícia C (12 min)", "reading_time": 12},
]


MOCK_DB_NEWS_COMPLEX = [
    {"title": "Notícia 1 (4 min)", "reading_time": 4},
    {"title": "Notícia 2 (7 min)", "reading_time": 7},
    {"title": "Notícia 3 (10 min)", "reading_time": 10},
]


def test_reading_plan_group_news():
    """
    Testa se group_news_for_available_time agrupa corretamente
    as notícias legíveis e ilegíveis.
    """

    AVAILABLE_TIME = 10

    with patch(
        "tech_news.analyzer.reading_plan.find_news", return_value=MOCK_DB_NEWS
    ) as mock_find_news:

        result = ReadingPlanService.group_news_for_available_time(
            AVAILABLE_TIME
        )

    expected_readable = [
        {
            "chosen_news": [
                ("Notícia A (8 min)", 8),
                ("Notícia B (2 min)", 2),
            ],
            "unfilled_time": 0,
        },
        {
            "chosen_news": [
                ("Notícia D (5 min)", 5),
                ("Notícia E (3 min)", 3),
            ],
            "unfilled_time": 2,
        },
    ]
    expected_unreadable = [("Notícia C (12 min)", 12)]

    assert result["readable"] == expected_readable
    assert result["unreadable"] == expected_unreadable
    mock_find_news.assert_called_once()

    with patch(
        "tech_news.analyzer.reading_plan.find_news",
        return_value=MOCK_DB_NEWS_COMPLEX,
    ):
        result_complex = ReadingPlanService.group_news_for_available_time(10)

    expected_readable_complex = [
        {
            "chosen_news": [("Notícia 3 (10 min)", 10)],
            "unfilled_time": 0,
        },
        {
            "chosen_news": [("Notícia 2 (7 min)", 7)],
            "unfilled_time": 3,
        },
        {
            "chosen_news": [("Notícia 1 (4 min)", 4)],
            "unfilled_time": 6,
        },
    ]
    assert result_complex["readable"] == expected_readable_complex
    assert result_complex["unreadable"] == []

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(0)
