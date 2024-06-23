from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Author, Post, Comment

def index(request):
    qs = Post.objects.order_by("-created_at")[:5]
    post_contents = [q.content for q in qs]
    result = ','.join(post_contents) 
    return HttpResponse(result)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author)
    return render(request, 'posts/author_detail.html', {'author': author, 'posts': posts})