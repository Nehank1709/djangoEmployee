from django.urls import path
from .views import EmployeeViews

urlpatterns=[
    path('employee/', EmployeeViews.as_view()),
    path('employee/<int:id>', EmployeeViews.as_view()),
    path('employee/<str:EmployeeName>', EmployeeViews.as_view()),
]