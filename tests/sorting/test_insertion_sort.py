import pytest

from dsa_python.sorting import insertion_sort


@pytest.mark.parametrize(
    "data",
    [
        [],
        [1],
        [5, 2, 4, 6, 1, 3],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [3, 1, 3, 2, 1],
        [-1, 0, -5, 10],
    ],
)
def test_insertion_sort_matches_sorted(data: list[int]) -> None:
    assert insertion_sort(data.copy()) == sorted(data)


def test_insertion_sort_is_in_place() -> None:
    data = [3, 1, 2]
    result = insertion_sort(data)
    assert result is data
    assert data == [1, 2, 3]
