from unittest.mock import MagicMock, Mock

import pytest
from part1 import count_trailhead_scores, read_map, traverse_trailhead


### load_disk_map
@pytest.fixture
def mock_open(mocker: Mock) -> MagicMock:
    """Fixture to mock the open function."""
    return mocker.patch("builtins.open")


def test_read_map_valid(mock_open: MagicMock):
    mock_open.return_value.__enter__.return_value.read.return_value = "123\n456\n789\n"
    assert read_map("test") == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_load_disk_map_file_not_found(mocker: MagicMock):
    mocker.patch("builtins.open", side_effect=FileNotFoundError)
    with pytest.raises(FileNotFoundError):
        read_map("test")


# Valid sample map to be used in multiple tests
SAMPLE_TRAIL_MAP = [
    [0, 1, 2, 3, 4, 5],
    [1, 3, 9, 8, 7, 6],
    [2, 3, 4, 5, 6, 7],
    [1, 0, 9, 0, 9, 8],
]


def test_count_trailhead_scores_valid():
    assert count_trailhead_scores(SAMPLE_TRAIL_MAP) == 3


def test_score_trailhead_valid():
    assert traverse_trailhead(SAMPLE_TRAIL_MAP, (0, 0), set()) == 2


def test_score_trailhead_invalid():
    assert traverse_trailhead(SAMPLE_TRAIL_MAP, (3, 3), set()) == 0
