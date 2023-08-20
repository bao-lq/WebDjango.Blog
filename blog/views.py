from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, edit
from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
class PostListView(ListView):           #------------------------------ class-base view | Method_1
    queryset = Post.objects.all().order_by('-date')
    template_name = 'blogs/blog.html'
    context_object_name = 'Posts'
    paginate_by = 5

class UserPostListView(ListView):       #------------------------------ class-base view | Method_1
    model = Post
    template_name = 'blogs/user_posts.html'
    context_object_name = 'Posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')

# Post detail
def PostDetailView(request, pk):        #------------------------------ function-base view + comment form
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        form = CommentForm()
    return render(request, 'blogs/post.html', {'post': post, 'form':form})

# Create/new post 
@login_required
def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm(user=request.user, initial={'author': request.user})}
        return render(request, 'blogs/new_post.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(
                request, 'The post has been created successfully.')
            return redirect('blog')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blogs/new_post.html', {'form': form})

# Edit/update post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'blogs/update_post.html'
    context_object_name = 'PostUpdate'
    success_message = 'The post has been updated successfully.'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Dele post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Post
    fields = '__all__'
    template_name = 'blogs/dele_post.html'
    context_object_name = 'PostDelete'
    success_url = '/blog/'
    success_message = 'The post has just been deleted.'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False