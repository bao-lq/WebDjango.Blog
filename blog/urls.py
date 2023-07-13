from django.urls import path
from .models import Post
from . import views
from django.views.generic import ListView

urlpatterns = [
    # Normal view controler 
    # path('', views.list, name='blog'),
    path('<int:pk>/', views.post, name='post'),

    # Generic view 
    # path('<int:pk>/', views.PostDetailView.as_view(), name='post'),

    # path('', views.PostListView.as_view(), name='blog'),      #----------------------- Post_list_view Method_1

    path('', ListView.as_view(                                  #----------------------- Post_list_view Method_2
        queryset = Post.objects.all().order_by('-date'),
        template_name = 'blogs/blog.html',
        context_object_name = 'Posts',
        paginate_by = 5
        ), name='blog'),
 
    # url(r'^user/(?P<pk>\d+)/$', UserDetailView.as_view(), name="user_view"),  #------- user detail
]