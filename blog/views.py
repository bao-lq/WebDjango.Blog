from django.shortcuts import render
from .models import Post
from django.http import Http404

# Create your views here.
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