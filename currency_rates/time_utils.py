from datetime import date, datetime, timedelta, timezone


def get_local_date() -> date:
    utc_now = datetime.now(timezone.utc)

    ## Moscow time
    hours_offset = 3
    custom_tz = timezone(timedelta(hours=hours_offset))

    return utc_now.astimezone(custom_tz).date()


def get_local_day() -> str:
    return get_local_date().strftime("%Y-%m-%d")
