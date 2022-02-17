import pytest
from HumanClassesandMethods import Man, Woman, Sex, Androgin
from datetime import date


@pytest.fixture(scope="module", autouse=True)
def parents():
    return [Woman('Yana',
                  'Klochko',
                  190,
                  65,
                  date(1989, 5, 25)),
            Man('Vladimir',
                'Velikiy',
                195,
                80,
                date(1990, 5, 18)),
            Androgin('Yaro',
                     'Garah',
                     187,
                     80,
                     date(1995, 5, 25))
            ]

def test_boy_creation(parents):
    child = parents[0].birth('Yakov', 52, 3.5, Sex.man, parents[1])
    assert child.height == 52
    assert type(child) == Man
    assert child.surname == parents[1].surname
    assert child.name == 'Yakov'
    assert child.weight == 3.5


def test_girl_creation(parents):
    child = parents[0].birth('Irina', 50, 3.2, Sex.woman, parents[1])
    assert child.height == 50
    assert type(child) == Woman
    assert child.surname == parents[1].surname
    assert child.name == 'Irina'
    assert child.weight == 3.2


def test_androgin_creation(parents):
    child = parents[0].birth('Ada', 58, 4.0, Sex.androgin, parents[2])
    assert child.height == 50
    assert type(child) == Androgin
    assert child.surname == parents[2].surname
    assert child.name == 'Ada'
    assert child.weight == 4.0


@pytest.mark.parametrize
def test_exception_birth_possibility(expected_exception, parent1, parent2):
    child = parents[0].birth('Ada', 58, 4.0, Sex.androgin, parents[2])
    with pytest.raises(expected_exception):
        child.birth(parent1, parent2)



