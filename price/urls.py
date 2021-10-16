from django.urls import path
from . import views

urlpatterns = [
    path('startech/', views.StartechPriceApiView.as_view(), name="startech-price"),
]
