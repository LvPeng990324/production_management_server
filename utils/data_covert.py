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
    fen = int(fen or 0)

    if fen % 100 == 0:
        return fen // 100

    return fen / 100


def get_list_default_value(data: list, index: int, default):
    """ 获取列表的值，没有的话就返回指定的默认值
    """
    if len(data) <= index:
        return default

    return data[index]


def set_list_value_by_index(data: list, index: int, value, default=None):
    """ 通过下标给数组set值
    如果跨越空位的话，就用default来填充
    """
    # 计算需要扩展的长度
    required_length = index + 1
    current_length = len(data)
    
    # 如果索引超出范围，填充默认值
    if required_length > current_length:
        extension = [default] * (required_length - current_length)
        data += extension  # 直接扩展列表
    
    # 设置目标索引的值
    data[index] = value
    return data