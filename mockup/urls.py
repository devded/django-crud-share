from django.urls import path

from mockup.views import TestMockApiView

urlpatterns = [
     path('', TestMockApiView.as_view(), name="base-api"),
]