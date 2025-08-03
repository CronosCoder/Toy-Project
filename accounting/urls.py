from django.urls import path
from accounting import views

urlpatterns = [
    path('api/v1/transactions/', views.TransactionCreateAPIView.as_view(), name='transaction_create'),
]