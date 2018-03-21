#!/usr/bin/env python
import time
import datetime


def get_percent():
    now = time.localtime(time.time())
    passed_days = now.tm_yday
    year = now.tm_year
    start_date = datetime.datetime(year=year, month=1, day=1)
    end_date = datetime.datetime(year=year, month=12, day=31)
    total_days = (end_date - start_date).days + 1
    percent = (float(passed_days) / float(total_days)) * 100
    percent = int(round(percent, 0))
    return passed_days, percent


def draw():
    thick_bar = '▓'
    thin_bar = '░'
    passed_days, percent = get_percent()
    bar = percent * thick_bar + (100 - percent) * thin_bar
    print('passed days: %s' % passed_days)
    print(bar + str(percent) + '%')


if __name__ == '__main__':
    draw()
