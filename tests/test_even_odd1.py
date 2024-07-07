import pytest
from Check.even_odd import check_even_odd

def test_check_even():
    assert check_even_odd(2) == "2 is even."
    assert check_even_odd(4) == "4 is even."
    assert check_even_odd(0) == "0 is even."

def test_check_odd():
    assert check_even_odd(1) == "1 is odd."
    assert check_even_odd(3) == "3 is odd."
    assert check_even_odd(5) == "5 is odd."
  

if __name__ == "__main__":
    pytest.main()