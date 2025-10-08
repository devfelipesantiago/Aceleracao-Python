from src.word_finder import lines_with_word_occurrences


def test_lines_with_word_occurrences():
    file_path = "tests/test_data/word_finder.txt"
    search_word = "python"
    occurrences = lines_with_word_occurrences(file_path, search_word)
    assert occurrences == [1, 2, 3, 4, 6, 8]
