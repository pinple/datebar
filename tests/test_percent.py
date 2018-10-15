"""
Test if the percentage is legal
"""
from datebar.date_bar import get_percent

def test_percent():
    percent_num = get_percent()
    assert (percent_num >= 0 and percent_num <= 100)
