import datetime


def get_local_date() -> datetime.date:
    utc_now = datetime.datetime.now(datetime.timezone.utc)

    ## Moscow time
    hours_offset = 3
    custom_tz = datetime.timezone(datetime.timedelta(hours=hours_offset))

    return utc_now.astimezone(custom_tz)


def get_local_day() -> str:
    return get_local_date().strftime("%Y-%m-%d")
