import pytest
from get_email import my_email
from invalid_syntax_error import InvalidSyntaxError

def test_syntax_match():
    assert my_email("string@string.com")

def test_syntax_1_error():
    with pytest.raises(InvalidSyntaxError):
        my_email("@string.com")

def test_syntax_2_error():
    with pytest.raises(InvalidSyntaxError):
        my_email("stringstring.com")

def test_syntax_3_error():
    with pytest.raises(InvalidSyntaxError):
        my_email("string@com")

def test_syntax_4_error():
    with pytest.raises(InvalidSyntaxError):
        my_email("string@string.")



