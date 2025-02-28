from django.urls import path

from Item.apis.add_item import add_item
from Item.apis.get_item_list import get_item_list
from Item.apis.edit_item import edit_item
from Item.apis.delete_item import delete_item
from Item.apis.add_technical_change import add_technical_change
from Item.apis.get_technical_change_list import get_technical_change_list
from Item.apis.edit_technical_change import edit_technical_change
from Item.apis.delete_technical_change import delete_technical_change


app_name = 'Item'

urlpatterns = [
    # 新增物品
    path('add-item/', add_item, name='add_item'),
    # 获取物品列表
    path('get-item-list/', get_item_list, name='get_item_list'),
    # 编辑物品
    path('edit-item/', edit_item, name='edit_item'),
    # 删除物品
    path('delete-item/', delete_item, name='delete_item'),
    # 新增技术变更
    path('add-technical-change/', add_technical_change, name='add_technical_change'),
    # 获取技术变更列表
    path('get-technical-change-list/', get_technical_change_list, name='get_technical_change_list'),
    # 编辑技术变更
    path('edit-technical-change/', edit_technical_change, name='edit_technical_change'),
    # 删除技术变更
    path('delete-technical-change/', delete_technical_change, name='delete_technical_change'),
]