from django.urls import path
from .models import Post
from . import views
from django.views.generic import ListView

urlpatterns = [
    # Blog list view
    # path('', views.list, name='blog'),                        #----------------------- Normal view controller
    # path('', views.PostListView.as_view(), name='blog'),      #----------------------- Generic view controller | Method_1
    path('', ListView.as_view(                                  #----------------------- Generic view controller | Method_2
        queryset = Post.objects.all().order_by('-date'),
        template_name = 'blogs/blog.html',
        context_object_name = 'Posts',
        paginate_by = 5
        ), name='blog'),

    # Post detail view
    # path('<int:id>/', views.post, name='post'),               #----------------------- Normal view controller
    # path('<int:pk>/', views.PostDetailView.as_view(), name='post'),   #--------------- Generic view controller
    path('<int:pk>/', views.PostDetailView, name='post'),       #----------------------- Normal view controller + Comment Form

    # Create new post
    path('post/new/', views.PostCreateView.as_view(), name='newpost'),    #----------------------- Normal view controller

    # url(r'^user/(?P<pk>\d+)/$', UserDetailView.as_view(), name="user_view"),  #------- user detail
]