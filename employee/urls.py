from django.urls import path
from .views import EmployeeViews

urlpatterns=[
    path('employee/', EmployeeViews.as_view()),
    path('employee/<int:EmployeeId>', EmployeeViews.as_view()),
]