import time


def write_log(log_level: str, log_msg):
    print(f'[{time.strftime("%Y-%m-%d %H:%M:%S")}] {log_msg}')
