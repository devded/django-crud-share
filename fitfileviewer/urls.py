from django.urls import path

from fitfileviewer.views import FitFileViewerServerCheckView, WakeUpView

urlpatterns = [
    path('wakeup/', WakeUpView.as_view(), name='wakeup'),
    path('status/', FitFileViewerServerCheckView.as_view(), name="base-api"),
]
