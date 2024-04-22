from django.urls import path
from userapp.views import *

urlpatterns = [
    path('hello', hello_world, name='hello_world'),
    path('category/list', category_list, name='category-list'),
    path('category/add', category_add, name='category-add'),
    path('product/list', product_list, name='product-list'),
    path('product/add', product_add, name='product-add'),
    path('category/<int:category_id>/view/', category_view, name='category-view'),
    path('product/<int:product_id>/view/', product_view, name='product-view'),
    path('category/<int:category_id>/delete/', category_delete, name='category-delete'),
    path('category/<int:category_id>/edit/', category_edit, name='category-edit'),
    path('product/<int:product_id>/edit/', product_edit, name='product-edit'),
    path('category/<int:category_id>/update/', category_update, name='category-update'),
]