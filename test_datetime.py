import datetime
from unittest.mock import Mock

# Save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

# Mock datetime to control today's date
mock_datetime = Mock()


def is_weekday():
    today = mock_datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)


# Test Tuesday is a weekday
def test_tuesday():
    # Mock .today() to return Tuesday
    mock_datetime.datetime.today.return_value = tuesday
    assert is_weekday()


# Test Saturday is not a weekday
def test_saturday():
    # Mock .today() to return Saturday
    mock_datetime.datetime.today.return_value = saturday
    assert not is_weekday()
