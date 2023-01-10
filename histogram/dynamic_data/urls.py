from django.urls import path

from . import views

app_name = 'dd'
urlpatterns = [
    # 定义动态数据主页
    path('', views.index, name='index'),
    # 定义标题组的列表视图
    path('title-set/', views.ListTitleView.as_view(), name='listTitle'),
    # 定义标题组的编辑视图
    path('title-set/<int:pk>/', views.DetailTitleView.as_view(), name='detailTitle'),
    # 定义标题组的详情视图
    path('title-set/<int:pk>/result', views.ResultTitleView.as_view(), name='resultTitle'),
    # 定义标题组的编辑处理器
    path('title-set/<int:title_set_id>/edit/', views.edit_title, name='editTitle'),
    # for test
    path('test/<int:title_set_id>/', views.result, name='testResult')
]
