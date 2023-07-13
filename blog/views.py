from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.conf import settings

# Create your views here.

# function-base views
def list(request):
    Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'blogs/blog.html', Data)

def post(request, id):
    message = 'This link could not be found'
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

# generic view 
# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blogs/post.html' 

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "blogs/post.html", {'post': post, 'form':form})

    # use detail 
# class UserDetailView(DetailView):
#     model = settings.AUTH_USER_MODEL

#     def get_context_data(self):
#         context = super().get_context_data()
#         context['posts'] = self.object.posts.all()
#         return context

