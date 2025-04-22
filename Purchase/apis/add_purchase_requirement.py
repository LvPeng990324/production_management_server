from Purchase.models import PurchaseRequirement
from Item.models import Item

from utils.custom_response import json_response
from utils.custom_response import ERROR_CODE
from utils.user_log import add_user_log
from utils.permission_check import login_required
from utils.data_covert import str_to_date
from utils.data_covert import date_to_str


@login_required
def add_purchase_requirement(request):
    """ 新增采购需求
    POST请求
    """
    item_id = request.json.get('item_id')
    count = request.json.get('count')
    date = str_to_date(request.json.get('date'))

    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "message": "物品不存在"
        })

    PurchaseRequirement.objects.create(
        item=item,
        count=count,
        date=date,
    )

    # 记录用户日志
    add_user_log(
        request=request,
        action='新增采购需求',
        detail=f'''订单号：{item.order.order_num}
        物品名：{item.name}
        数量：{count}
        需求日期：{date_to_str(date=date)}'''
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        'res': 'success',
    })
