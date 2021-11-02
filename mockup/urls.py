from django.urls import path

from mockup.views import TestMockApiView, TrainingPlanApiView

urlpatterns = [
     path('', TestMockApiView.as_view(), name="base-api"),
     path('training-plan', TrainingPlanApiView.as_view(), name="training-plan"),
]