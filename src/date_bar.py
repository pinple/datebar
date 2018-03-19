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
    print('total_days: %s' % total_days)
    print('passed_days: %s' % passed_days)
    percent = (passed_days / total_days) * 100
    percent = int(round(percent, 0))
    print('the progress of the year: %s%%' % percent)
    return percent


def draw():
     thick_bar = '▓'
     thin_bar = '░'
     percent = get_percent()
     bar = percent * thick_bar + (100 - percent) * thin_bar
     print(bar + str(percent) + '%')

if __name__ == '__main__':
    draw()
