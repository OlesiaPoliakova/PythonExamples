
from HumanClassesandMethods import Man
from datetime import date
import pytest

@pytest.fixture(scope="module")
def person():
    return Man('Vladimir',
                'Velikiy',
                195,
                80,
                date(1990, 5, 18))

@pytest.mark.parametrize("now, expected_age",
                         [(date(1990, 5, 19), 0),
                          (date(1991, 5, 19), 1),
                          (date(1900, 5, 19), None)
                          ]
                         )

def test_age_changes(mocker, person, now, expected_age):
    mocker.patch("HumanClassesandMethods.get_today", return_value=now)
    assert person.age == expected_age
    mocker.patch("HumanClassesandMethods.get_today", return_value=now)
    assert person.age == expected_age
    mocker.patch("HumanClassesandMethods.get_today", return_value=now)
    assert person.age == expected_age
