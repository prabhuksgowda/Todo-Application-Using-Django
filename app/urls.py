from django.urls import path
from .views import TaskView,TaskUpdateView,TaskDeleteView

urlpatterns = [
    path('', TaskView.as_view(), name='TaskView'),
    path('update/<int:pk>',TaskUpdateView.as_view(), name='TaskUpdate'),
    path('delete/<int:pk>/remove',TaskDeleteView.as_view(), name='TaskDelete'),
]