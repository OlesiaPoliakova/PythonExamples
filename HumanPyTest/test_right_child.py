import pytest
from HumanClassesandMethods import Man, Woman, Sex, Androgin, NoFatherException
from datetime import date

def generate_parent(sex):
    if sex == Sex.woman:
        return Woman('Yana',
                  'Klochko',
                  190,
                  65,
                  date(1989, 5, 25))
    elif sex == Sex.man:
        return Man('Vladimir',
                'Velikiy',
                195,
                80,
                date(1990, 5, 18))
    else:
        return Androgin('Yaro',
                     'Garah',
                     187,
                     80,
                     date(1995, 5, 25))

@pytest.fixture(scope="module")
def parents():
    return [generate_parent(Sex.woman),
            generate_parent(Sex.man),
            generate_parent(Sex.androgin)
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



@pytest.mark.parametrize("parent1_sex, parent2_sex, expected_exception",
                         [(Sex.man, Sex.man, AttributeError),
                          (Sex.man, Sex.woman, AttributeError),
                          (Sex.man, Sex.androgin, AttributeError),
                          (Sex.woman, Sex.woman, NoFatherException),
                          (Sex.woman, Sex.man, True),
                          (Sex.woman, Sex.androgin, True),
                          (Sex.androgin, Sex.androgin, True),
                          (Sex.androgin, Sex.man, True),
                          (Sex.androgin, Sex.woman, NoFatherException),
                          ]
                         )

def test_birth_possibility(parent1_sex, parent2_sex, expected_exception):
    human1 = generate_parent(parent1_sex)
    human2 = generate_parent(parent2_sex)
    if type(expected_exception) is bool and expected_exception:
        child = human1.birth('Ada', 58, 4.0, Sex.androgin, human2)
        assert child.height == 58
        assert type(child) == Androgin
        assert child.surname == human2.surname
        assert child.name == 'Ada'
        assert child.weight == 4.0
    else:
        with pytest.raises(expected_exception):
            human1.birth('Ada', 58, 4.0, Sex.androgin, human2)



