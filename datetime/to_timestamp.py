from datetime import datetime, timezone, timedelta
import re
# 输入一个时间和时区，获得timestamp
def to_timestamp(dt_str, tz_str):
    #string to time
    t = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # extract offset hours
    hours_str = (re.match(r'^(UTC\+)(\d+)(:00)$', tz_str)).group(2)
    hoursdelta = int(hours_str)
    # get inout time timezone
    input_tz_info = timezone(timedelta(hours = hoursdelta))
    t = t.replace(tzinfo=input_tz_info)
    # convert to utc time
    utc_time = t.astimezone(timezone.utc)
    # convert to timestamp
    result = utc_time.timestamp()
    return result

if __name__ == '__main__':
    t = '2015-12-6 16:25:30'
    tz = 'UTC+8:00'
    print(to_timestamp(t, tz))