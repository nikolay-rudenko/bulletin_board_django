from django.urls import path
from .views import index, by_rubric

urlpatterns = [
    path('bboard/<int:rubric_id>/', by_rubric),
    path('bboard/', index),
    path('', index),
]
