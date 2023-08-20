from django.urls import path
from . import views
from django.views.generic import ListView

urlpatterns = [
    # Blog list view
    path('', views.PostListView.as_view(), name='blog'),      #----------------------- Generic view controller | Method_1

    # User post view
    path('user/<str:username>/', views.UserPostListView.as_view(), name='user_posts'),

    # Post detail view
    path('post/<int:pk>/', views.PostDetailView, name='post'),       #----------------------- Normal view controller + Comment Form

    # Create new post
    path('post/new/', views.create_post, name='new_post'),    #----------------------- Normal view controller

    # Edit post
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='update_post'),

    # Delete post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='dele_post'),
    # url(r'^user/(?P<pk>\d+)/$', UserDetailView.as_view(), name="user_view"),  #------- user detail
]