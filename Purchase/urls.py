from django.urls import path

from Purchase.apis.get_purchase_requirement_list import get_purchase_requirement_list
from Purchase.apis.add_purchase_requirement import add_purchase_requirement


app_name = 'Purchase'

urlpatterns = [
    # 获取采购需求列表
    path('get-purchase-requirement-list/', get_purchase_requirement_list, name='get_purchase_requirement_list'),
    # 新增采购需求
    path('add-purchase-requirement/', add_purchase_requirement, name='add_purchase_requirement'),
]