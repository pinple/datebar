"""
Test if the percentage is legal
"""
import datebar


def test_percent():
    _, percent_num = datebar.get_percent()
    assert (0 <= percent_num <= 100)
