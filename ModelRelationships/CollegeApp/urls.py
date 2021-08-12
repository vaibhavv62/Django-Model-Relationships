from django.urls import path
from .views import DeptCreateView, DeptDeleteView, DeptUpdateView, DeptListView

urlpatterns = [
    path('create/',DeptCreateView.as_view(),name='create'),
    path('retrive/',DeptListView.as_view(),name='retrive'),
    path('update/<int:pk>/',DeptUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',DeptDeleteView.as_view(),name='delete'),
]