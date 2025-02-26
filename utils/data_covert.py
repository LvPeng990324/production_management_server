import datetime


def str_to_datetime(datetime_str: str):
    """ 字符串转时间对象
    """
    if 'T' in datetime_str:
        return datetime.datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')
    else:
        return datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')


def date_to_str(date: datetime.date):
    """ 日期转字符串方法
    格式：YYYY-MM-DD
    """
    if not date:
        return ''
    return date.strftime('%Y-%m-%d')


def datetime_to_str(datetime: datetime.datetime):
    """ 日期时间转字符串方法
    格式：YYYY-MM-DD hh:mm:ss
    """
    if not datetime:
        return ''
    return datetime.strftime('%Y-%m-%d %H:%M:%S')