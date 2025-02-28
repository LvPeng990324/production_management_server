from django.urls import path

from Supplier.apis.add_supplier import add_supplier
from Supplier.apis.delete_supplier import delete_supplier
from Supplier.apis.get_supplier_list import get_supplier_list
from Supplier.apis.edit_supplier import edit_supplier


app_name = 'Supplier'

urlpatterns = [
    # 新增供应商
    path('add-supplier/', add_supplier, name='add_supplier'),
    # 删除供应商
    path('delete-supplier/', delete_supplier, name='delete_supplier'),
    # 获取供应商列表
    path('get-supplier-list/', get_supplier_list, name='get_supplier_list'),
    # 编辑供应商
    path('edit-supplier/', edit_supplier, name='edit_supplier'),
]
