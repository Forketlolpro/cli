import datetime

from currency_rates.time_utils import get_local_date


def test_get_local_date() -> None:
    result: datetime.date = get_local_date()

    assert isinstance(result, datetime.date)
