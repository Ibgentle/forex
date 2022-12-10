from django.urls import path
from . import views


app_name = 'journal'



urlpatterns = [
        path('', views.trade_list, name='trade_list'),
        path('<int:id>/', views.trade_detail, name='trade_detail'),
        ]

