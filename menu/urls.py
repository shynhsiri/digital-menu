from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('category/<slug:category_slug>/', views.category_list, name='category_list'),
] 