from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.views.generic import ListView, DetailView

# Create your views here.

# function-base views
def list(request):
    Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'blogs/blog.html', Data)

def post(request, id):
    message = 'Không tìm thấy đường dẫn này'
    try:
        post = Post.objects.get(id = id)
    except Post.DoesNotExist:
        raise Http404(message)

    return render(request, 'blogs/post.html', {'post': post})


# class-base views 
class PostListView(ListView):
    queryset = Post.objects.all().order_by('-date')
    template_name = 'blogs/blog.html'
    context_object_name = 'Posts'
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogs/post.html'

#     # urls.py
# urlpatterns = [
#     url(r'^user/(?P<pk>\d+)/$', UserDetailView.as_view(), name="user_view"),
# ]

# # views.py
# class UserDetailView(DetailView):
#     model = User

#     def get_context_data(self):
#         context = super().get_context_data()
#         context['posts'] = self.object.posts.all()
#         return context