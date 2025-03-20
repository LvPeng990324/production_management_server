import datetime
from hashlib import md5
from typing import Union


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


def str_to_md5(data: str):
    """ 字符串转md5
    """
    mixer = md5()
    mixer.update(data.encode('utf8'))
    return mixer.hexdigest()


def yuan_to_fen(yuan: Union[float, str]):
    """ 元转分
    """
    yuan = float(yuan or 0)
    return int(yuan * 100)


def fen_to_yuan(fen: int):
    """ 分转元
    """
    fen = fen or 0

    if fen % 100 == 0:
        return fen // 100

    return fen / 100