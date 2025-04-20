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
def in_store(request):
    """ 入库
    POST请求
    """
    item_id = request.json.get('item_id')
    count = request.json.get('count')

    # 取出这个物品
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return json_response(code=ERROR_CODE.NOT_FOUND, data={
            "message": "物品不存在",
        })

    try:
        store_house = StoreHouse.objects.get(item_id=item_id)
    except StoreHouse.DoesNotExist:
        store_house = StoreHouse.objects.create(item=item, remain_count=0)

    # 加库存
    store_house.remain_count += count

    # 记录操作记录
    user = User.objects.get(id=request.session.get('user_id'))
    log_str = f'[{datetime_to_str(datetime=datetime.datetime.now())}] {user.name} 入库 {item.name} {count}个'
    store_house.operate_log_list.append(log_str)

    # 保存
    store_house.save()

    # 记录用户日志
    add_user_log(
        request=request,
        action='仓库入库',
        detail=log_str,
    )

    return json_response(code=ERROR_CODE.SUCCESS, data={
        
    })
