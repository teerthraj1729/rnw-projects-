from datetime import datetime,timedelta
import time

def current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def diff_between_dates(date_str1,date_str2,fmt="%Y-%m-%d"):
    d1 = datetime.strptime(date_str1,fmt)
    d2 = datetime.strptime(date_str2,fmt)
    return abs((d2-d1).days)


def format_date(date_str,in_fmt="%Y-%m-%d",out_fmt="%d %b %Y"):
    d = datetime.strptime(date_str,in_fmt)
    return d.strftime(out_fmt)


def stopwatch(run_seconds=0):
    start = time.time()
    time.sleep(run_seconds)
    end = time.time()
    elapsed = end-start
    return elapsed


def countdown(seconds):
    for s in range(seconds,0,-1):
        yield s
