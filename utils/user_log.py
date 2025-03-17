from SystemManagement.models import UserLog


def add_user_log(request, action, detail):
    """ 增加用户日志
    """
    UserLog.objects.create(
        user_id=request.session.get('user_id'),
        action=action,
        detail=detail,
    )
