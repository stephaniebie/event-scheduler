import pytest
from random import sample
from scheduler.search import (
    binary_search,
    linear_search,
    SearchAlgorithm,
    search_data,
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


@pytest.mark.parametrize(
    "target, expected_target",
    [
        (
            10,
            Event(
                id=10,
                title="",
                date="2025-10-11",
                time="01:30",
                location="",
            ),
        ),
        (
            0,
            Event(
                id=0,
                title="",
                date="2025-10-01",
                time="01:30",
                location="",
            ),
        ),
        (100, None),
    ],
)
def test_search(target, expected_target):
    # Linear search
    if expected_target is None:
        assert linear_search(data=unsorted_list, target=target) is None
        assert linear_search(data=sorted_list, target=target) is None
    else:
        assert vars(linear_search(data=unsorted_list, target=target)) == vars(
            expected_target
        )
        assert vars(linear_search(data=sorted_list, target=target)) == vars(
            expected_target
        )

    # Binary search
    if expected_target is None:
        assert binary_search(data=unsorted_list, target=target) is None
        assert binary_search(data=sorted_list, target=target) is None
    else:
        assert vars(binary_search(data=unsorted_list, target=target)) == vars(
            expected_target
        )
        assert vars(binary_search(data=sorted_list, target=target)) == vars(
            expected_target
        )


def test_searchalgorithm():
    expected_algorithms = {
        "LINEAR": linear_search,
        "BINARY": binary_search,
    }
    assert list(expected_algorithms) == list(SearchAlgorithm.__members__)
    assert list(expected_algorithms.values()) == [alg.value for alg in SearchAlgorithm]


def test_search_data():
    target_id = 10
    expected_target = Event(
        id=10,
        title="",
        date="2025-10-11",
        time="01:30",
        location="",
    )

    # Linear search
    assert vars(
        search_data(data=unsorted_list, id=target_id, algorithm=SearchAlgorithm.LINEAR)
    ) == vars(expected_target)

    # Binary search
    assert vars(
        search_data(data=unsorted_list, id=target_id, algorithm=SearchAlgorithm.BINARY)
    ) == vars(expected_target)

    # Catch value errors
    with pytest.raises(ValueError) as exception:
        search_data(data=unsorted_list, id=target_id, algorithm="INVALID ALGORITHM")
    assert "INVALID ALGORITHM is an invalid or undefined search algorithm." == str(
        exception.value
    )
