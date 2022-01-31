from django.urls import path
from . import views

urlpatterns = [
  path('', views.defshop, name='shop'),
  path('adminlogin/', views.defadminlogin, name='adminlogin'),
  path('checkout/<data_id>/', views.defcheckout, name='checkout'),
  path('addingform/', views.defaddingform, name='addingform'),
  path('edit/<pd_id>/', views.defedit, name='edit'),
  path('delete/<pdd_id>/', views.defdel, name='del'),
  path('history/', views.defhistory, name='history'),
  path('inventory/', views.definventory, name='inventory'),
  path('adminreg/', views.defadminreg, name='adminreg'),
  path('logout/', views.deflogout, name='logout'),
  path('complete_order/<i_id>/', views.complete_order, name='complete_order'),
  path('cancel_order/<i_id>/', views.cancel_order, name='cancel_order')
]

