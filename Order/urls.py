from django.urls import path

from Order.apis.add_order import add_order
from Order.apis.get_order_list import get_order_list
from Order.apis.edit_order import edit_order
from Order.apis.delete_order import delete_order
from Order.apis.get_order_list import get_order_select_list


app_name = 'Order'

urlpatterns = [
    # 新增订单
    path('add-order/', add_order, name='add_order'),
    # 获取order列表
    path('get-order-list/', get_order_list, name='get_order_list'),
    # 编辑订单
    path('edit-order/', edit_order, name='edit_order'),
    # 删除订单
    path('delete-order/', delete_order, name='delete_order'),
    # 获取订单选项列表
    path('get-order-select-list/', get_order_select_list, name='get_order_select_list'),
]