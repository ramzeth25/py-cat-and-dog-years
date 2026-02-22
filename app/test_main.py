from app.main import get_human_age


def test_should_return_zero_list_for_zero_age() -> None:
    assert get_human_age(14, 14) == [0, 0], \
        "should return zero list for zero age"


def test_should_return_list_with_all_one_if_ages_is_15() -> None:
    assert get_human_age(15, 15) == [1, 1], \
        "should return list with all one if ages is 15"


def test_should_return_list_more_than_one_age() -> None:
    assert get_human_age(100, 100) == [21, 17], \
        "should return list more than one age"


def test_should_return_one_human_age() -> None:
    assert get_human_age(23, 23) == [1, 1], \
        "should return one human age"
