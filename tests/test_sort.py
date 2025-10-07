from pytest import raises
from random import sample
from scheduler.sort import (
    insertion_sort,
    merge_sort,
    quick_sort,
    sort_data,
    SortingAlgorithm,
)
from scheduler.event import Event


# Test parameters
sorted_list = [
    Event(
        id=i,
        title="",
        date=f"2025-10-{str(1 + i).zfill(2)}",
        time="01:30",
        location="",
    )
    for i in range(25)
]
unsorted_list = sample(sorted_list, k=len(sorted_list))


def test_insertion_sort():
    assert insertion_sort(unsorted_list) == sorted_list


def test_merge_sort():
    assert merge_sort(unsorted_list) == sorted_list


def test_quick_sort():
    assert quick_sort(unsorted_list) == sorted_list


def test_sortingalgorithm():
    expected_algorithms = {
        "INSERTION": insertion_sort,
        "MERGE": merge_sort,
        "QUICK": quick_sort,
    }
    assert list(expected_algorithms) == list(SortingAlgorithm.__members__)
    assert list(expected_algorithms.values()) == [alg.value for alg in SortingAlgorithm]


def test_sort_data():
    # Insertion sort
    assert (
        sort_data(data=unsorted_list, algorithm=SortingAlgorithm.INSERTION)
        == sorted_list
    )

    # Merge sort
    assert (
        sort_data(data=unsorted_list, algorithm=SortingAlgorithm.MERGE) == sorted_list
    )

    # Quick sort
    assert (
        sort_data(data=unsorted_list, algorithm=SortingAlgorithm.QUICK) == sorted_list
    )

    # Catch value errors
    with raises(ValueError) as exception:
        sort_data(data=unsorted_list, algorithm="INVALID ALGORITHM")
    assert "INVALID ALGORITHM is an invalid or undefined sorting algorithm." == str(
        exception.value
    )
