from django.urls import path

from . import views

urlpatterns = [
    path('', views.BaseApiView.as_view(), name="base-api"),
    path('create/', views.CreateTodoApiView.as_view(), name="create-todo")
]
