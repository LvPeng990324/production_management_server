from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from SystemManagement.models import UserLog

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.pack_api_data import pack_user_log_info_list
from utils.permission_check import login_required


@login_required
def get_user_log_list(request):
    """ 获取用户日志列表
    GET请求
    """
    current_page = request.GET.get('currentPage') or 1
    page_size = request.GET.get('size') or 10
    user_name = request.GET.get('user_name')
    action = request.GET.get('action')
    detail = request.GET.get('detail')

    user_logs = UserLog.objects.all().order_by('-create_time')
    total = user_logs.count()

    # 筛选：
    if user_name:
        user_logs = user_logs.filter(user__name__contains=user_name)
    if action:
        user_logs = user_logs.filter(action__contains=action)
    if detail:
        user_logs = user_logs.filter(detail__contains=detail)

    # 加入分页
    paginator = Paginator(user_logs, page_size)
    try:
        user_logs = paginator.get_page(current_page)
    except PageNotAnInteger:  # 页码非法，返回第一页
        user_logs = paginator.get_page(1)
    except EmptyPage:  # 页码超出范围，返回最后一页
        user_logs = paginator.get_page(paginator.num_pages)

    user_log_info_list = pack_user_log_info_list(user_logs=user_logs)

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "total": total,
        "list": user_log_info_list,
    })
