
from HumanClassesandMethods import Man
from datetime import date

def test_age_changes(mocker):
    human = Man("Vasiliy", "King", 170, 58, date(2011, 5, 25))
    mocker.patch("HumanClassesandMethods.get_today", return_value=date(2011, 5, 25))
    assert human.age == 0
    mocker.patch("HumanClassesandMethods.get_today", return_value=date(2012, 5, 25))
    assert human.age == 1
    mocker.patch("HumanClassesandMethods.get_today", return_value=date(2012, 5, 25))
    assert human.age == 10

