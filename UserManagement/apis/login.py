from UserManagement.models import User

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response


def login(request):
    """ 登录
    POST请求
    """
    # 先固定一个用户，等用户系统实现好了再完善
    users = User.objects.all()
    if not users.exists():
        User.objects.create(
            name='测试用户',
            phone='11111111111',
            password_md5='aaaaaa',
        )
        users = User.objects.all()
    user = users.first()

    # 记录session信息
    request.session['name'] = user.name
    request.session['phone'] = user.phone
    request.session['user_id'] = user.id

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "token": "token-admin",
    })
