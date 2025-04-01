from UserManagement.models import User

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response
from utils.user_log import add_user_log
from utils.data_covert import str_to_md5
from utils.permission_check import login_required


@login_required
def change_self_info(request):
    """ 更改自己信息
    POST请求
    """
    name = request.json.get('name')
    phone = request.json.get('phone')
    new_password = request.json.get('new_password')
    new_password_md5 = str_to_md5(new_password or '')

    try:
        user = User.objects.get(id=request.session.get('user_id'))
    except User.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "message": "未找到当前用户，重新登录",
        })

    # 记录本次修改的内容描述
    edit_log_str = ''

    # 按需修改
    if user.name != name:
        edit_log_str += f'姓名：{user.name} -> {name}\n'
        user.name = name

    if user.phone != phone:
        edit_log_str += f'手机号：{user.phone} -> {phone}\n'
        user.phone = phone

    # 密码是给了才修改
    if new_password and user.password_md5 != new_password_md5:
        edit_log_str += '修改了密码\n'
        user.password_md5 = new_password_md5

    user.save()

    # 记录用户日志
    add_user_log(
        request=request,
        action='修改自己信息',
        detail=edit_log_str,
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "username": "admin11",
    })
