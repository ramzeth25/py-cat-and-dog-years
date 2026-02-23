import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(0, 0, [0, 0],
                     id="cat and dog years 0 gives [0, 0]"),
        pytest.param(15, 15, [1, 1],
                     id="cat and dog years 15 gives [1, 1]"),
        pytest.param(24, 24, [2, 2],
                     id="cat and dog years 24 gives [2, 2]"),
        pytest.param(14, 14, [0, 0],
                     id="cat and dog years 14 gives [0, 0]"),
        pytest.param(100, 100, [21, 17],
                     id="cat and dog years 100 gives [1, 1]"),
        pytest.param(24, 100, [2, 17],
                     id="cat 24 and dog 100 years  gives [2, 17]"),
        pytest.param(100, 28, [21, 2],
                     id="cat 100 and dog 28 years  gives [21, 2]"),
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_result: list
                       ) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result, \
        "get human age should equal expected result"
