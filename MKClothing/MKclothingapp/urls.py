from django.urls import path
from . import views

urlpatterns = [
  path('', views.defshop, name='shop'),
  path('adminlogin/', views.defadminlogin, name='adminlogin'),
  path('cart/', views.defcart, name='cart'),
  path('checkout/', views.defcheckout, name='checkout'),
  path('adminchangepass/', views.defadminchangepass, name='adminchangepass'),
  path('addingform/', views.defaddingform, name='addingform'),
  path('edit/<pd_id>/', views.defedit, name='edit'),
  path('delete/<pdd_id>/', views.defdel, name='del'),
  path('history/', views.defhistory, name='history'),
  path('inventory/', views.definventory, name='inventory'),
  path('adminreg/', views.defadminreg, name='adminreg'),
]

