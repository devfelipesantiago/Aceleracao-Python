import csv
import sys
from unittest.mock import patch
from src import spotify
import pytest

TEST_DATA_PATH = "tests/test_data/spotify.csv"

pytestmark = pytest.mark.dependency()


def sample_reader(path):
    with open(path, "r") as file:
        return list(csv.DictReader(file))


@patch("src.spotify.read_csv")
@patch.object(sys, "argv", ["script-name"])
def test_spotify_analyzer_main_no_option(mock_reader, capsys):
    exit_code = spotify.main(TEST_DATA_PATH)
    assert exit_code == 1

    captured = capsys.readouterr()
    mock_reader.assert_not_called()

    assert "Modo de uso:\n    python3 src/spotify.py [ opção ]" in captured.out


@patch.object(sys, "argv", ["script-name", "INVALID"])
def test_spotify_analyzer_invalid_option(capsys):
    res = spotify.main(TEST_DATA_PATH)
    assert res == 1

    captured = capsys.readouterr()

    assert "Opção 'INVALID' inválida." in captured.out


@patch.object(sys, "argv", ["script-name", "1"])
@patch("src.spotify.handle_user_input")
@patch("src.spotify.read_csv")
@patch("src.spotify.process_music_analysis")
def test_spotify_analyzer_valid_option(
    mock_processer, mock_reader, mock_handler
):
    res = spotify.main(TEST_DATA_PATH)
    assert res == 0

    mock_reader.assert_called_once_with(TEST_DATA_PATH)
    mock_handler.assert_called_once_with(mock_reader.return_value, "1")


@patch.object(sys, "argv", ["script-name", "2"])
def test_spotify_analyzer_integration(capsys):

    res = spotify.main(TEST_DATA_PATH)
    assert res == 0

    captured = capsys.readouterr()

    assert captured.out == (
        "Top 10 músicas mais dançantes:\n"
        " 1 - 'Give It To Me' de Timbaland\n"
        " 2 - 'GIRL LIKE ME' de Black Eyed Peas\n"
        " 3 - 'Blueberry Yum Yum' de Ludacris\n"
        " 4 - 'Around the World' de Daft Punk\n"
        " 5 - 'Temperature' de Sean Paul\n"
        " 6 - 'The Real Slim Shady' de Eminem\n"
        " 7 - 'Frikitona' de Plan B\n"
        " 8 - 'Back That Up To The Beat - sped up version' de Madonna\n"
        " 9 - 'Shake That (Remix)' de Nate Dogg\n"
        "10 - 'The Watcher' de Dr. Dre\n"
    )


@patch("src.spotify.process_music_analysis")
def test_spotify_handler_calls_processor(mock_processor):
    csv_data = [{"fake_key": "fake_value"}]
    spotify.handle_user_input(csv_data, "1")

    mock_processor.assert_called_once_with(csv_data, "1")


def test_spotify_handler_raises_when_invalid_option():
    csv_data = [{"fake_key": "fake_value"}]

    with pytest.raises(ValueError):
        spotify.handle_user_input(csv_data, "INVALID")


def test_spotify_processor_calls_get_most_instrumental_songs():
    csv_data = sample_reader(TEST_DATA_PATH)
    res = spotify.get_most_instrumental_songs(csv_data)
    for i in range(len(res) - 1):
        assert res[i]["Instrumentalness"] >= res[i + 1]["Instrumentalness"]


def test_spotify_processor_calls_get_most_danceable_songs():
    csv_data = sample_reader(TEST_DATA_PATH)
    res = spotify.get_most_danceable_songs(csv_data)
    for i in range(len(res) - 1):
        assert res[i]["Danceability"] >= res[i + 1]["Danceability"]


def test_spotify_processor_calls_get_most_energetic_songs():
    csv_data = sample_reader(TEST_DATA_PATH)
    res = spotify.get_most_energetic_songs(csv_data)
    for i in range(len(res) - 1):
        assert res[i]["Energy"] >= res[i + 1]["Energy"]


@pytest.mark.dependency(
    depends=[
        "test_spotify_analyzer_main_no_option",
        "test_spotify_analyzer_invalid_option",
        "test_spotify_analyzer_valid_option",
        "test_spotify_analyzer_integration",
        "test_spotify_handler_calls_processor",
        "test_spotify_handler_raises_when_invalid_option",
        "test_spotify_processor_calls_get_most_instrumental_songs",
        "test_spotify_processor_calls_get_most_danceable_songs",
        "test_spotify_processor_calls_get_most_energetic_songs",
    ]
)
def test_spotify_final():
    pass
