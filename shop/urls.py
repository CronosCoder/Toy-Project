from django.urls import path
from shop import views

urlpatterns = [
    path('api/v1/products/', views.ProductListCreateView.as_view(), name='product_list_create'),
]