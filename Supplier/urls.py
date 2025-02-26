from django.urls import path

from Supplier.apis.test_api import test_api


app_name = 'Supplier'

urlpatterns = [
    # 测试api
    path('test-api/', test_api, name='test_api'),
]