from unittest.mock import MagicMock, Mock

import pytest
from part1 import (
    calculate_checksum,
    compact_disk_map,
    find_last_digit_idx,
    load_disk_map,
    parse_disk_map,
)


### load_disk_map
@pytest.fixture
def mock_open(mocker: Mock) -> MagicMock:
    """Fixture to mock the open function."""
    return mocker.patch("builtins.open")


def test_load_disk_map_valid(mock_open: MagicMock):
    mock_open.return_value.__enter__.return_value.readline.return_value = "12345\n"
    output = load_disk_map("test_input.txt")
    assert output == "12345"


def test_load_disk_map_empty_file(mock_open: MagicMock):
    mock_open.return_value.__enter__.return_value.readline.return_value = ""
    output = load_disk_map("test_input.txt")
    assert output == ""


def test_load_disk_map_file_not_found(mocker: MagicMock):
    mocker.patch("builtins.open", side_effect=FileNotFoundError)
    with pytest.raises(FileNotFoundError):
        load_disk_map("nonexistent.txt")


### parse_disk_map
def test_parse_disk_map_valid():
    output = parse_disk_map("12345")
    assert output == "0..111....22222"


def test_parse_disk_map_single():
    output = parse_disk_map("1")
    assert output == "0"


def test_parse_disk_map_empty():
    output = parse_disk_map("")
    assert output == ""


def test_parse_disk_map_invalid():
    with pytest.raises(ValueError):
        parse_disk_map("12a45")


### compact_disk_map
def test_compact_disk_map_valid():
    output = compact_disk_map("0..111....22222")
    assert output == "022111222......"


def test_compact_disk_map_all_free():
    output = compact_disk_map("......")
    assert output == "......"


def test_compact_disk_map_all_full():
    output = compact_disk_map("01111222")
    assert output == "01111222"


def test_compact_disk_map_empty():
    output = compact_disk_map("")
    assert output == ""


### find_last_digit_idx
def test_find_last_digit_idx_valid():
    assert find_last_digit_idx("0..11.2222..", 0) == 9


def test_find_last_digit_idx_empty():
    assert find_last_digit_idx("", 0) == None


def test_find_last_digit_idx_no_digits():
    assert find_last_digit_idx("...", 0) == None


def test_find_last_digit_idx_valid_start():
    assert find_last_digit_idx("011...", 2) == 2


def test_find_last_digit_idx_empty_start():
    assert find_last_digit_idx("011...", 3) == None


def test_find_last_digit_idx_invalid_start():
    with pytest.raises(ValueError):
        find_last_digit_idx("0..11.2", 8)


### calculate_checksum
def test_calculate_checksum_valid():
    assert calculate_checksum("022111222......") == 60


def test_calculate_checksum_empty():
    assert calculate_checksum("") == 0


def test_calculate_checksum_no_digits():
    assert calculate_checksum("...") == 0
