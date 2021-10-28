from django.urls import path
from . import views

urlpatterns = [
  path('', views.defindex, name='index'),
  path('Allproducts/', views.defAllproducts, name='Allproducts'),
  path('forhim/', views.defforhim, name='forhim'),
  path('login/', views.deflogin, name='login'),
  path('productpage/', views.defproductpage, name='productpage'),
  path('signup/', views.defsignup, name='signup'),
]

