from django.urls import path

from Dashboard.apis.get_dashboard_show_data import get_dashboard_show_data


app_name = 'Dashboard'

urlpatterns = [
    # 获取首页展示数据
    path('get-dashboard-show-data/', get_dashboard_show_data, name='get_dashboard_show_data'),
]