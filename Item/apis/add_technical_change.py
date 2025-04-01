from Item.models import TechnicalChange
from Item.models import Item

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.permission_check import login_required


@login_required
def add_technical_change(request):
    """ 新增技术变更
    POST请求
    """
    name = request.json.get('name')
    item_id = request.json.get('item_id')

    # 取出要关联的物品
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "message": "该物品不存在",
        })

    TechnicalChange.objects.create(
        name=name,
        item=item,
    )

    # 记录用户日志
    add_user_log(
        request=request,
        action='新增技术变更',
        detail=f'''名字：{name}
        关联物品：{item.name}'''
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
