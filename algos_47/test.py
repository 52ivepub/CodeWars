import pytest

from main import meeting


def test_meeting_00():
    assert meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;"
                   "Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn") == ("(ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)"
                                                                        "(DORNY, ABBA)(KERN, LEWIS)(KORN, ALEX)"
                                                                        "(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)"
                                                                        "(STAN, MEGAN)(WAHL, ALEXIS)")



def test_meeting_01():
    assert meeting("John:Gates;Michael:Wahl;Megan:Bell;Paul:Dorries;James:Dorny;Lewis:Steve;Alex:Meta;Elizabeth:Russel;Anna:Korn;Ann:Kern;Amber:Cornwell") == "(BELL, MEGAN)(CORNWELL, AMBER)(DORNY, JAMES)(DORRIES, PAUL)(GATES, JOHN)(KERN, ANN)(KORN, ANNA)(META, ALEX)(RUSSEL, ELIZABETH)(STEVE, LEWIS)(WAHL, MICHAEL)"


# def test_meeting_02():
#     assert meeting(20) == 78


def test_error_meeting_03():
    with pytest.raises(IndexError):
        assert meeting('123') == '123'
