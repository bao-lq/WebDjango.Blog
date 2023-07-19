from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, edit
from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy

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
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        form = CommentForm()
    return render(request, 'blogs/post.html', {'post': post, 'form':form})

#new post 
def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'blogs/new_post.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'The post has been created successfully.')
            return redirect('blog')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blogs/new_post.html', {'form': form})

#edit post
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'GET':
        context = {'form': PostForm(instance=post), 'pk': pk}
        return render(request, 'blogs/edit_post.html', context)

    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'The post has been updated successfully.')
            return redirect('post', pk=pk)
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blogs/edit_post.html', {'form': form})

# dele post 
def dele_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'form': post}    
    
    if request.method == 'GET':
        return render(request, 'blogs/dele_post.html',context)

    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('blog')

# ...

    # user detail 
# class UserDetailView(DetailView):
#     model = settings.AUTH_USER_MODEL

#     def get_context_data(self):
#         context = super().get_context_data()
#         context['posts'] = self.object.posts.all()
#         return context