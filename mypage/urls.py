from django.urls import path
from django.conf.urls import url, static
from django.conf import settings

from . import views


app_name = 'mypage'
urlpatterns = [
    #path of index view class
    # path('', views.IndexView.as_view(), name='index'),
    #path for index def
    path('', views.index, name='index'),

    path('cinfo', views.CDetailView.as_view(), name='cdetail'),
    path('linfo', views.LDetailView.as_view(), name='ldetail'),
    #for pass id of the cdtails
    path('<int:cdetalis_id>', views.CD, name='CD'),
    # path('<int:pk>/', views.LDetailView.as_view(), name='ldetail'),
]

