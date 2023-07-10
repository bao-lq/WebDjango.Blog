from django.urls import path
from . import views

urlpatterns = [
    # normal view controler 
    # path('', views.list, name='blog'),
    # path('<int:id>', views.post, name='post'),

    # Generic view 
    path('', views.PostListView.as_view(), name='blog'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post'),
]