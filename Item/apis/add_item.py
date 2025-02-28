from Item.models import Item

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE


def add_item(request):
    """ 新增物品
    POST请求
    """
    name = request.json.get('name')

    Item.objects.create(
        name=name,
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        "res": 'success',
    })
