from django.urls import path

from StoreHouse.apis.get_store_house_list import get_store_house_list
from StoreHouse.apis.in_store import in_store
from StoreHouse.apis.out_store import out_store


app_name = 'StoreHouse'

urlpatterns = [
    # 获取库存列表
    path('get-store-house-list/', get_store_house_list, name='get_store_house_list'),
    # 仓库入库
    path('in-store/', in_store, name='in_store'),
    # 仓库出库
    path('out-store/', out_store, name='out_store'),
]