import datetime


def is_leap_year(year):
    if (year % 4) != 0:
        return False
    if (year % 100) == 0:
        return (year % 400) == 0
    return True


def get_time_from_ticks(ticks):
    one_millisecond = 10000
    days_per_year = 365
    days_per_4_years = days_per_year * 4 + 1
    days_per_100_years = days_per_4_years * 25 - 1
    days_per_400_years = days_per_100_years * 4 + 1
    year_day_acc = (
        (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365),
        (0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366))
    acc = ticks // one_millisecond
    # millisecond = acc % 1000
    acc //= 1000
    second = acc % 60
    acc //= 60
    minute = acc % 60
    acc //= 60
    hour = acc % 24
    acc //= 24
    # total_days = acc

    y400 = acc // days_per_400_years
    acc -= y400 * days_per_400_years

    y100 = acc // days_per_100_years
    if y100 == 4:
        y100 = 3
    acc -= y100 * days_per_100_years

    y4 = acc // days_per_4_years
    acc -= y4 * days_per_4_years

    y1 = acc // days_per_year
    if y1 == 4:
        y1 = 3
    acc -= y1 * days_per_year

    year = 1601 + y400 * 400 + y100 * 100 + y4 * 4 + y1
    is_leap = is_leap_year(year)

    month = 0
    while acc >= year_day_acc[is_leap][month]:
        month += 1

    day = acc - year_day_acc[is_leap][month - 1] + 1
    # day_of_week = (total_days + 1) % 7

    return datetime.datetime(
        year=year,
        month=month,
        day=day,
        hour=hour,
        minute=minute,
        second=second)
