from django.urls import path
from accounting import views

urlpatterns = [
    path('api/v1/check-out/', views.TransactionCreateAPIView.as_view(), name='transaction_create'),
    path('api/v1/payment-success/', views.PaymentSuccessAPIView.as_view(), name='payment_success'),
    path('api/v1/payment-fail/', views.PaymentFailAPIView.as_view(), name='payment_fail'),
]