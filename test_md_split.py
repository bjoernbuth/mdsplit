from md_split import split_by_h1
from md_split import get_valid_filename


def test_example():
    assert 1 == 1


def test_split_by_h1_simple():
    with open("test_resources/simple.md") as fh:
        parts = list(split_by_h1(fh))
        assert len(parts) == 2

        assert parts[0].heading == "Heading 1"
        assert len(parts[0].text) == 7
        assert parts[1].heading == "Heading 2"
        assert len(parts[1].text) == 3


def test_split_by_h1_nested():
    with open("test_resources/nested.md") as fh:
        parts = list(split_by_h1(fh))
        assert len(parts) == 3

        assert parts[0].heading == "Heading 1"
        assert len(parts[0].text) == 11
        assert parts[1].heading == "Heading 2 (dense)"
        assert len(parts[1].text) == 8
        assert parts[2].heading == "Heading 3 (deeply nested)"
        assert len(parts[2].text) == 26


def test_split_by_h1_codeblock():
    with open("test_resources/codeblock.md") as fh:
        parts = list(split_by_h1(fh))
        assert len(parts) == 1

        assert parts[0].heading == "Beware of Code Blocks"
        assert len(parts[0].text) == 21


def test_get_valid_filename():
    assert get_valid_filename("test.txt") == "test.txt"
    assert get_valid_filename("test with spaces-and-dashes") == "test with spaces-and-dashes"
    assert get_valid_filename("test/\\~#*+.txt") == "test.txt"
    assert get_valid_filename("non_ascii_Äß鳥_ჩიტები") == "non_ascii_Äß鳥_ჩიტები"