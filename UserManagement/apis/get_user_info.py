from UserManagement.models import User

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response
from utils.permission_check import login_required


@login_required
def get_user_info(request):
    """ 获取用户信息
    GET请求
    """
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "username": user.name,
    })
