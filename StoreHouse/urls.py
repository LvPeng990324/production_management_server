from django.urls import path

from StoreHouse.apis.get_store_house_list import get_store_house_list


app_name = 'StoreHouse'

urlpatterns = [
    # 获取库存列表
    path('get-store-house-list/', get_store_house_list, name='get_store_house_list'),
]