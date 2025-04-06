from django.urls import path

from Customer.apis.add_customer import add_customer
from Customer.apis.delete_customer import delete_customer
from Customer.apis.get_customer_list import get_customer_list
from Customer.apis.edit_customer import edit_customer


app_name = 'Customer'

urlpatterns = [
    # 新增客户
    path('add-customer/', add_customer, name='add_customer'),
    # 删除客户
    path('delete-customer/', delete_customer, name='delete_customer'),
    # 获取客户列表
    path('get-customer-list/', get_customer_list, name='get_customer_list'),
    # 编辑供应商
    path('edit-customer/', edit_customer, name='edit_customer'),
]
