from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from django.conf import settings

# Create your views here.

# Blog list 
# function-base views
# def list(request):                    #------------------------------ function-base view
#     Data = {'Posts': Post.objects.all().order_by('-date')}
#     return render(request, 'blogs/blog.html', Data)

class PostListView(ListView):           #------------------------------ class-base view | Method_1
    queryset = Post.objects.all().order_by('-date')
    template_name = 'blogs/blog.html'
    context_object_name = 'Posts'
    paginate_by = 5

# Post detail 
# def post(request, id):                #------------------------------ function-base view
#     message = 'This link could not be found'
#     try:
#         post = Post.objects.get(id = id)
#     except Post.DoesNotExist:
#         raise Http404(message)
#     return render(request, 'blogs/post.html', {'post': post})

# class PostDetailView(DetailView):     #------------------------------ class-base view
#     model = Post
#     template_name = 'blogs/post.html' 

def PostDetailView(request, pk):        #------------------------------ function-base view + comment form
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, 'blogs/post.html', {'post': post, 'form':form})

class PostCreateView(CreateView):
    model = Post
    template_name = 'blogs/newpost.html'
    fields = '__all__'

    # user detail 
# class UserDetailView(DetailView):
#     model = settings.AUTH_USER_MODEL

#     def get_context_data(self):
#         context = super().get_context_data()
#         context['posts'] = self.object.posts.all()
#         return context