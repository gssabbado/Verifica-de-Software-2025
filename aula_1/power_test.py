import pytest
from power import power_to
from negative_power_error import NegativeError


def test_square():
    ret = power_to(2, 2)
    assert ret == 4

def test_negative():
    with pytest.raises(NegativeError):
        assert power_to(2, -3)