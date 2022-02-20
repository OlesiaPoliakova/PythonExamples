import pytest
from HumanClassesandMethods import Man, Woman, Androgin, Sex
from datetime import date

@pytest.fixture(scope="module")
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

@pytest.mark.parametrize("husband_is_father, father_sex",
                         [(True, Sex.man),
                          (False, Sex.man),
                          (True, Sex.androgin),
                          (False, Sex.androgin)
                          ]
                         )

def test_child_surname_creation(parents, husband_is_father, father_sex):
    mother = parents[0]
    if father_sex == Sex.man:
        father = parents[1]
    else:
        father = parents[2]
    if husband_is_father:
        mother.marry(father)
    child = mother.birth('Yakov', 52, 3.5, Sex.man, father)
    assert child.surname == father.surname

