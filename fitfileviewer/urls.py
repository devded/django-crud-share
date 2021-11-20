from django.urls import path

from fitfileviewer.views import FitFileViewerServerCheckView

urlpatterns = [
    path('status/', FitFileViewerServerCheckView.as_view(), name="base-api"),
]
