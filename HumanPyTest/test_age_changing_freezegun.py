from freezegun import freeze_time
from HumanClassesandMethods import Man
from datetime import date, datetime
import pytest

@pytest.fixture(scope="module")
def person():
    return Man('Vladimir',
                'Velikiy',
                195,
                80,
                date(1990, 5, 18))
@pytest.mark.parametrize("now, expected_age",
                         [("1990-05-19", 0),
                          ("1991-05-19", 1),
                          ("1900-05-19", None)
                          ]
                         )

def test_age_changes(person, now, expected_age):
    with freeze_time(now):
        assert person.age == expected_age




