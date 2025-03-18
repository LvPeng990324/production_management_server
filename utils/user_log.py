from SystemManagement.models import UserLog

from utils.logger import write_log


def add_user_log(request, action, detail):
    """ 增加用户日志
    """
    user_id = request.session.get('user_id')
    write_log('info', f'add_user_log {user_id} {action} {detail}')

    UserLog.objects.create(
        user_id=user_id,
        action=action,
        detail=detail,
    )
