from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-data_publicacao')
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)