from Item.models import Item

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response
from utils.pack_api_data import pack_item_info_list


def get_item_list(request):
    """ 获取物品列表
    GET请求
    """
    name = request.GET.get('name')

    items = Item.objects.all()

    # 筛选
    if name:
        items = items.filter(name__contains=name)

    item_info_list = pack_item_info_list(items=items)

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "total": len(item_info_list),
        "list": item_info_list,
    })
