from Item.models import Item

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE


def delete_item(request):
    """ 删除物品
    POST请求
    """
    item_id = request.json.get('item_id')

    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
        "msg": '该物品不存在',
    })

    item.delete()

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
