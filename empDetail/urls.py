from django.urls import path
from .views import EmployeeList,EmployeeCreate,EmployeeDeleteView,EmployeeDetailView,EmployeeUpdateView

urlpatterns = [
    path('',EmployeeList.as_view(),name='Home'),
    path('create/',EmployeeCreate.as_view(),name='create-employee'),
    path('detail/<int:pk>',EmployeeDetailView.as_view(), name='employee-detail'),
    path('delete/<int:pk>/',EmployeeDeleteView.as_view(),name='delete-employee'),
    path('update/<int:pk>/',EmployeeUpdateView.as_view(),name='update-employee'),
]