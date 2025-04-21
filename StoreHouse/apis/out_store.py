import datetime

from StoreHouse.models import StoreHouse
from Item.models import Item
from UserManagement.models import User

from utils.custom_response import ERROR_CODE
from utils.custom_response import json_response
from utils.permission_check import login_required
from utils.data_covert import datetime_to_str
from utils.user_log import add_user_log


@login_required
def out_store(request):
    """ 出库
    POST请求
    """
    contract_number = request.json.get('contract_number')
    item_number = request.json.get('item_number')
    count = int(request.json.get('out_store_count'))

    # 取出这个物品
    try:
        item = Item.objects.get(contract_number=contract_number, item_number=item_number)
    except Item.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "message": "物品不存在",
        })
    except Item.MultipleObjectsReturned:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "message": "物品存在多个，请联系管理员",
        })

    try:
        store_house = StoreHouse.objects.get(item=item)
    except StoreHouse.DoesNotExist:
        store_house = StoreHouse.objects.create(item=item, remain_count=0)

    # 减库存
    store_house.remain_count -= count
    if store_house.remain_count < 0:
        return json_response(code=ERROR_CODE.ILLEGAL, data={
            "message": "库存不足",
        })

    # 记录操作记录
    user = User.objects.get(id=request.session.get('user_id'))
    log_str = f'[{datetime_to_str(datetime=datetime.datetime.now())}] {user.name} 出库 {item.name} {count}个'
    store_house.operate_log_list.append(log_str)

    # 保存
    store_house.save()

    # 记录用户日志
    add_user_log(
        request=request,
        action='仓库出库',
        detail=log_str,
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        
    })
